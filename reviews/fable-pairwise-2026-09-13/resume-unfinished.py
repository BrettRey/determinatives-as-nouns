"""Resume provider-refused reads after the interactive batch has shut down."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import sys

run = Path(__file__).resolve().parent
manifest = run / 'manifest.json'
state = json.loads(manifest.read_text())
assert not any(x['status'] == 'running' for x in state['pairs']), 'Batch is still active.'
resumed = []
for item in state['pairs']:
    if item['status'] != 'failed':
        continue
    assert "Lower-priority mode isn't available" in item.get('error', ''), item
    log = Path(item['provider_log_path'])
    entries = [json.loads(line) for line in log.read_text().splitlines()]
    assert not any(
        entry.get('type') == 'assistant'
        and 'fable' in entry.get('message', {}).get('model', '').lower()
        for entry in entries
    ), 'A provider answer may exist; inspect it before retrying.'
    assert not (run / item['pair'] / 'report.md').exists(), 'Completed review already exists.'
    preserve = {key: value for key, value in item.items() if key not in ['attempts']}
    item.setdefault('attempts', []).append(preserve)
    for key in ['started_at', 'finished_at', 'session_id', 'pid', 'provider_log_path',
                'low_priority_command_at', 'low_priority_confirmed', 'error']:
        item.pop(key, None)
    item['status'] = 'pending'
    item['resumed_at'] = datetime.now(timezone.utc).isoformat()
    resumed.append(item['pair'])
state.pop('finished_at', None)
temporary = run / 'manifest.tmp'
temporary.write_text(json.dumps(state, indent=2) + '\n')
temporary.replace(manifest)
print('Resuming unfinished pairs: ' + ', '.join(resumed), flush=True)
os.execv(sys.executable, [sys.executable, '-u', str(run / 'run-interactive.py')])
