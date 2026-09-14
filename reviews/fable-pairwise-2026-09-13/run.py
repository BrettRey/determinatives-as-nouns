"""Run the authorized independent Fable pair reads, preserving every response."""
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import threading
import time

RUN = Path(__file__).resolve().parent
MANIFEST = RUN / 'manifest.json'
state = json.loads(MANIFEST.read_text())
lock = threading.Lock()
stop = threading.Event()
consecutive_failures = 0


def now():
    return datetime.now(timezone.utc).isoformat()


def save():
    temporary = RUN / 'manifest.tmp'
    temporary.write_text(json.dumps(state, indent=2) + '\n')
    temporary.replace(MANIFEST)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def review(item):
    global consecutive_failures
    if stop.is_set():
        return
    folder = RUN / item['pair']
    command = [
        'claude', '-p', '--model', 'fable', '--effort', 'max',
        '--safe-mode', '--restricted', '--tools', '',
        '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}',
        '--setting-sources', '', '--no-session-persistence',
        '--output-format', 'json', '--system-prompt',
        'You are an independent academic reader reviewing two supplied sections. '
        'Perform the bounded pairwise task and return a precise Markdown report. '
        'You have no tools and no access to other reviews.'
    ]
    with lock:
        item.update(status='running', started_at=now(), command=command)
        save()
        print(f"START {item['pair']}", flush=True)
    begun = time.monotonic()
    try:
        with (folder / 'prompt.md').open('rb') as prompt, (folder / 'raw-response.json').open('wb') as output, (folder / 'stderr.log').open('wb') as error:
            process = subprocess.Popen(command, stdin=prompt, stdout=output, stderr=error, cwd=RUN.parent.parent)
            with lock:
                item['pid'] = process.pid
                save()
            try:
                code = process.wait(timeout=2700)
            except subprocess.TimeoutExpired:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
                raise RuntimeError('Fable call exceeded the 45-minute bound; partial output retained.')
        response = json.loads((folder / 'raw-response.json').read_text())
        models = list(response.get('modelUsage', {}))
        if code != 0 or response.get('is_error') or not isinstance(response.get('result'), str) or not response['result'].strip():
            raise RuntimeError(f"Incomplete Fable result: exit={code}, subtype={response.get('subtype')}, result={str(response.get('result'))[:300]}")
        fable_models = [model for model in models if 'fable' in model.lower()]
        if not fable_models:
            raise RuntimeError(f'Expected Fable; result records {models}')
        report = folder / 'report.md'
        report.write_text(response['result'].rstrip() + '\n')
        with lock:
            item.update(status='complete', finished_at=now(), duration_seconds=round(time.monotonic()-begun, 1), actual_models=models, reviewer_model=fable_models[-1], raw_output_path=str((folder/'raw-response.json').relative_to(RUN)), raw_output_sha256=digest(folder/'raw-response.json'), report_path=str(report.relative_to(RUN)), report_sha256=digest(report), reported_cost_usd=response.get('total_cost_usd'), usage=response.get('usage'), session_id=response.get('session_id'), exit_code=code)
            consecutive_failures = 0
            save()
            print(f"DONE {item['pair']} ({sum(x['status']=='complete' for x in state['pairs'])}/28), {item['duration_seconds']}s", flush=True)
    except Exception as exc:
        with lock:
            item.update(status='failed', finished_at=now(), error=str(exc), duration_seconds=round(time.monotonic()-begun, 1))
            if (folder/'raw-response.json').exists():
                item['raw_output_sha256'] = digest(folder/'raw-response.json')
            consecutive_failures += 1
            if consecutive_failures >= 3:
                stop.set()
            save()
            print(f"FAILED {item['pair']}: {exc}", flush=True)


if __name__ == '__main__':
    state['cli_version'] = subprocess.check_output(['claude', '--version'], text=True).strip()
    priority = ['4-5', '2-5', '2-4', '2-3', '2-6', '3-6', '1-5', '5-6', '5-7', '1-7', '3-5', '4-6', '1-2', '2-7', '3-4', '4-7', '1-6', '1-3', '1-4', '3-7', '6-7', '1-A', '2-A', '3-A', '4-A', '5-A', '6-A', '7-A']
    pending = [next(x for x in state['pairs'] if x['pair']==pair) for pair in priority]
    pending = [item for item in pending if item['status']=='pending']
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(review, item) for item in pending}
        while futures:
            finished, futures = wait(futures, timeout=50, return_when=FIRST_COMPLETED)
            for future in finished:
                future.result()
            if not finished:
                with lock:
                    active = ', '.join(item['pair'] for item in state['pairs'] if item['status']=='running')
                    print(f"IN PROGRESS: {active}; {sum(item['status']=='complete' for item in state['pairs'])}/28 complete", flush=True)
    with lock:
        state['finished_at'] = now()
        save()
        print(json.dumps({'complete':sum(item['status']=='complete' for item in state['pairs']), 'failed':sum(item['status']=='failed' for item in state['pairs']), 'pending':sum(item['status']=='pending' for item in state['pairs'])}), flush=True)
