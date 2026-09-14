from pathlib import Path
import os
import sys

run = Path(__file__).resolve().parent
pair = sys.argv[1]
folder = run / pair
prompt = (folder / 'prompt.md').read_text()
session_id = (folder / 'interactive-session-id.txt').read_text().strip()
args = [
    '/Users/brettreynolds/.local/share/claude/versions/2.1.269', '--model', 'fable', '--effort', 'max',
    '--safe-mode', '--restricted', '--tools', '',
    '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}',
    '--setting-sources', '', '--permission-mode', 'manual', '--session-id', session_id,
    '--system-prompt',
    'You are an independent academic reader reviewing two supplied sections. '
    'Perform the bounded pairwise task and return a precise Markdown report. '
    'You have no tools and no access to other reviews.',
    prompt,
]
os.execvp(args[0], args)
