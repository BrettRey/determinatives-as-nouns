"""One reduced, streaming extraction attempt after the larger batch timed out."""
import json
import time
import urllib.request
from pathlib import Path

import jsonschema

root = Path(__file__).resolve().parent
if (root / "small-response.json").exists():
    raise SystemExit("Reduced response already exists; no automatic rerun.")
request = json.loads((root / "small-request.json").read_text())
started = time.monotonic()
fragments = []
final = {}
first_token_seconds = None
print("Sending reduced streaming request", flush=True)
http = urllib.request.Request(
    "http://localhost:11434/api/chat",
    data=json.dumps(request).encode(),
    headers={"Content-Type": "application/json"},
)
try:
    with urllib.request.urlopen(http, timeout=180) as response:
        for line in response:
            chunk = json.loads(line)
            content = chunk.get("message", {}).get("content", "")
            if content and first_token_seconds is None:
                first_token_seconds = round(time.monotonic() - started, 2)
                print(f"First output after {first_token_seconds}s", flush=True)
            fragments.append(content)
            if chunk.get("done"):
                final = chunk
                break
except Exception as error:
    final = {"error": f"{type(error).__name__}: {error}"}
content = "".join(fragments)
result = {
    "elapsed_seconds": round(time.monotonic() - started, 2),
    "first_token_seconds": first_token_seconds,
    "content": content,
    "final": final,
}
(root / "small-response.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
if "error" in final:
    raise SystemExit(final["error"])
records = json.loads(content)
(root / "small-records.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
errors = [e.message for e in jsonschema.Draft202012Validator(request["format"]).iter_errors(records)]
print(json.dumps({"elapsed_seconds": result["elapsed_seconds"], "first_token_seconds": first_token_seconds, "output_tokens": final.get("eval_count"), "done_reason": final.get("done_reason"), "schema_errors": errors}, indent=2), flush=True)
