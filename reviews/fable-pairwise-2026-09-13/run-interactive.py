"""Supervise fresh interactive pair reads and invoke the authorized slash command."""
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import pty
import select
import signal
import sys
import threading
import time
import uuid

RUN = Path(__file__).resolve().parent
MANIFEST = RUN / 'manifest.json'
LOGS = Path('/Users/brettreynolds/.claude/projects/-Users-brettreynolds-projects-LLM-CLI-projects-papers-queue-determinatives-as-nouns')
state = json.loads(MANIFEST.read_text())
lock = threading.Lock()
stop = threading.Event()
failures = 0


def now():
    return datetime.now(timezone.utc).isoformat()


def save():
    temp = RUN / 'manifest.tmp'
    temp.write_text(json.dumps(state, indent=2) + '\n')
    temp.replace(MANIFEST)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def events(path):
    if not path.exists():
        return []
    result = []
    for line in path.read_text().splitlines():
        try:
            result.append(json.loads(line))
        except ValueError:
            pass
    return result


def completed(entries):
    messages = {}
    last_text_index = -1
    last_finished_index = -1
    for index, entry in enumerate(entries):
        if entry.get('type') == 'system' and entry.get('subtype') == 'turn_duration':
            last_finished_index = index
        message = entry.get('message', {})
        if entry.get('type') != 'assistant' or not isinstance(message, dict) or 'fable' not in message.get('model', '').lower():
            continue
        texts = [part for part in message.get('content', []) if isinstance(part, dict) and part.get('type') == 'text']
        if texts:
            last_text_index = index
            # Preserve every answer-text block and its provider metadata. The full
            # original provider log remains at its private path, recorded by hash.
            messages[entry.get('uuid', str(index))] = {**message, 'content': texts, 'timestamp': entry.get('timestamp'), 'uuid': entry.get('uuid')}
    if last_text_index < 0 or last_finished_index <= last_text_index:
        return None
    text = '\n\n'.join(part['text'] for message in messages.values() for part in message['content'])
    return text, list(messages.values())


def review(item, adopt=False):
    global failures
    if stop.is_set():
        return
    folder = RUN / item['pair']
    fd = pid = None
    begun = time.monotonic()
    low_sent = bool(item.get('low_priority_confirmed'))
    if not adopt:
        session_id = str(uuid.uuid4())
        (folder / 'interactive-session-id.txt').write_text(session_id + '\n')
        with lock:
            item.update(status='running', started_at=now(), session_id=session_id, transport='interactive CLI', requested_service_mode='low-priority when session-limited')
            save()
        pid, fd = pty.fork()
        if pid == 0:
            os.chdir(RUN.parent.parent)
            os.execv(sys.executable, [sys.executable, str(RUN/'launch-interactive.py'), item['pair']])
        with lock:
            item['pid'] = pid
            save()
    log = LOGS / (item['session_id'] + '.jsonl')
    terminal_path = Path('/tmp') / ('fable-pair-' + item['session_id'] + '.terminal.log')
    with lock:
        item['provider_log_path'] = str(log)
        save()
        print(('WATCH ' if adopt else 'START ') + item['pair'], flush=True)
    try:
        with terminal_path.open('ab') as terminal:
            while time.monotonic() - begun < 2700:
                if fd is not None:
                    ready, _, _ = select.select([fd], [], [], 1)
                    if ready:
                        try:
                            chunk = os.read(fd, 65536)
                        except OSError:
                            chunk = b''
                        terminal.write(chunk)
                        terminal.flush()
                        if not chunk:
                            raise RuntimeError('Interactive CLI exited before a complete report was saved.')
                else:
                    time.sleep(1)
                entries = events(log)
                answer = completed(entries)
                if answer:
                    text, messages = answer
                    report = folder / 'report.md'
                    report.write_text(text.rstrip() + '\n')
                    raw = folder / 'raw-response.json'
                    raw.write_text(json.dumps({'transport':'interactive CLI', 'result':text, 'assistant_messages':messages}, ensure_ascii=False, indent=2) + '\n')
                    with lock:
                        item.update(status='complete', finished_at=now(), duration_seconds=round(time.monotonic()-begun, 1), actual_models=list(dict.fromkeys(message['model'] for message in messages)), reviewer_model=messages[-1]['model'], raw_output_path=str(raw.relative_to(RUN)), raw_output_sha256=digest(raw), report_path=str(report.relative_to(RUN)), report_sha256=digest(report), provider_log_sha256=digest(log), service_mode='low-priority' if low_sent else 'standard after reset', usage=messages[-1].get('usage'))
                        failures = 0
                        save()
                        print(f"DONE {item['pair']} ({sum(x['status']=='complete' for x in state['pairs'])}/28)", flush=True)
                    if fd is not None:
                        os.write(fd, b'/exit\r')
                    break
                synthetic = [entry for entry in entries if entry.get('isApiErrorMessage')]
                if synthetic:
                    error = synthetic[-1]
                    text = str(error.get('message', {}).get('content', ''))
                    if 'session limit' in text and not low_sent:
                        # The slash command is a terminal-only built-in. Wait for
                        # the failed turn's duration record, then select it.
                        if entries.index(error) < max((i for i,x in enumerate(entries) if x.get('subtype')=='turn_duration'), default=-1):
                            if fd is None:
                                raise RuntimeError('Adopted session needs manual low-priority activation.')
                            os.write(fd, b'/low-priority\r')
                            low_sent = True
                            with lock:
                                item['low_priority_command_at'] = now()
                                save()
                                print('LOW-PRIORITY ' + item['pair'], flush=True)
                    elif 'session limit' not in text:
                        raise RuntimeError(text[:500])
                for entry in entries:
                    if entry.get('subtype')=='local_command':
                        content = str(entry.get('content', ''))
                        if 'Continuing now at lower priority' in content:
                            with lock:
                                if not item.get('low_priority_confirmed'):
                                    item['low_priority_confirmed'] = True
                                    save()
                        if "Lower-priority mode isn't available" in content or 'weekly limit resets' in content:
                            raise RuntimeError(content[:500])
            else:
                raise RuntimeError('Interactive read exceeded the 45-minute bound; provider log retained.')
    except Exception as exc:
        with lock:
            item.update(status='failed', finished_at=now(), error=str(exc))
            failures += 1
            if failures >= 3:
                stop.set()
            save()
            print(f"FAILED {item['pair']}: {exc}", flush=True)
        if pid is not None:
            os.kill(pid, signal.SIGTERM)
    finally:
        if pid is not None:
            # The child stays supervised through its normal /exit shutdown.
            deadline = time.monotonic() + 10
            while time.monotonic() < deadline:
                if os.waitpid(pid, os.WNOHANG)[0]:
                    break
                if fd is not None and select.select([fd], [], [], .2)[0]:
                    try:
                        os.read(fd, 65536)
                    except OSError:
                        pass
            else:
                os.kill(pid, signal.SIGTERM)
                os.waitpid(pid, 0)
        if fd is not None:
            os.close(fd)


if __name__ == '__main__':
    priority = ['3-6','1-5','5-6','5-7','1-7','3-5','4-6','1-2','2-7','3-4','4-7','1-6','1-3','1-4','3-7','6-7','1-A','2-A','3-A','4-A','5-A','6-A','7-A']
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = set()
        for pair in priority:
            item = next(x for x in state['pairs'] if x['pair']==pair)
            if item['status']=='pending':
                futures.add(pool.submit(review, item))
            elif item['status']=='running' and pair=='3-6':
                futures.add(pool.submit(review, item, True))
        while futures:
            done, futures = wait(futures, timeout=50, return_when=FIRST_COMPLETED)
            for future in done:
                future.result()
            if not done:
                with lock:
                    print('IN PROGRESS: ' + ', '.join(x['pair'] for x in state['pairs'] if x['status']=='running') + f"; {sum(x['status']=='complete' for x in state['pairs'])}/28 complete", flush=True)
    with lock:
        state['finished_at'] = now()
        save()
        print(json.dumps({s:sum(x['status']==s for x in state['pairs']) for s in ['complete','failed','pending']}), flush=True)
