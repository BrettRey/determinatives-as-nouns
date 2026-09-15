#!/bin/zsh
# Poll the Aristotle task until it leaves IN_PROGRESS, then download.
PROJ=0e33f26b-84fe-4965-b0dc-2479d356b1e0
cd "$(dirname "$0")"
: > status-history.jsonl
for i in $(seq 1 120); do
  line=$(aristotle tasks $PROJ 2>&1 | sed -n '3p')
  st=$(print -r -- "$line" | awk '{print $NF}')
  print -r -- "{\"t\":\"$(date -u +%FT%TZ)\",\"poll\":$i,\"status\":\"$st\"}" >> status-history.jsonl
  if [[ "$st" != "IN_PROGRESS" && "$st" != "QUEUED" && -n "$st" ]]; then
    print -r -- "TERMINAL: $st"
    aristotle download $PROJ --destination result.tar.gz > download-output.txt 2>&1 \
      || aristotle download $PROJ > download-output.txt 2>&1
    exit 0
  fi
  sleep 30
done
print -r -- "TIMEOUT after 60 minutes"
exit 1
