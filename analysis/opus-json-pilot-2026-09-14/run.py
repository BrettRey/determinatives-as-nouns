"""Run the original 20-case extraction pilot with Opus at xhigh effort."""
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def save(name, obj):
    (ROOT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


if (ROOT / "raw-response.json").exists():
    raise SystemExit("Output already exists; no automatic rerun.")
command = [
    "claude", "-p", "--model", "opus", "--effort", "xhigh",
    "--safe-mode", "--restricted", "--tools", "",
    "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
    "--setting-sources", "", "--no-session-persistence",
    "--output-format", "json",
    "--json-schema", json.dumps(json.loads((ROOT / "schema.json").read_text())),
    "--system-prompt", (ROOT / "system-prompt.txt").read_text(),
]
manifest = {
    "requested_model": "opus",
    "requested_effort": "xhigh",
    "added_timeout": None,
    "started_at": datetime.now(timezone.utc).isoformat(),
    "cli_version": subprocess.check_output(["claude", "--version"], text=True).strip(),
    "status": "running",
    "input_sha256": {
        name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        for name in ("prompt.json", "system-prompt.txt", "schema.json", "sources.json", "queries.json")
    },
    "command": command,
}
save("manifest.json", manifest)
started = time.monotonic()
print("Starting Opus xhigh on the full 20-case pilot; no added timeout", flush=True)
with (ROOT / "prompt.json").open("rb") as prompt, (ROOT / "raw-response.json").open("wb") as out, (ROOT / "stderr.txt").open("wb") as err:
    process = subprocess.Popen(command, stdin=prompt, stdout=out, stderr=err, cwd=ROOT)
    manifest["pid"] = process.pid
    save("manifest.json", manifest)
    code = process.wait()
manifest.update(exit_code=code, elapsed_seconds=round(time.monotonic() - started, 2), finished_at=datetime.now(timezone.utc).isoformat())
try:
    response = json.loads((ROOT / "raw-response.json").read_text())
    manifest.update(actual_models=list(response.get("modelUsage", {})), reported_cost_usd=response.get("total_cost_usd"), usage=response.get("usage"))
    if code or response.get("is_error"):
        raise RuntimeError(str(response.get("result", response.get("subtype"))))
    records = response.get("structured_output")
    if not isinstance(records, dict):
        content = response.get("result", "").strip()
        if content.startswith("```"):
            content = "\n".join(content.splitlines()[1:-1])
        records = json.loads(content)
    save("records.json", records)
    manifest["status"] = "complete"
except Exception as error:
    manifest.update(status="failed", error=str(error))
save("manifest.json", manifest)
print(json.dumps({k:manifest.get(k) for k in ("status", "elapsed_seconds", "actual_models", "reported_cost_usd", "error")}, indent=2), flush=True)
