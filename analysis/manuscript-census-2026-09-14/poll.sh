#!/bin/zsh
PROJ=7ff7f952-176b-4512-a065-1b99c9cdf34d
cd "$(dirname "$0")"
: > status-history.jsonl
for i in $(seq 1 160); do
  st=$(aristotle tasks $PROJ 2>&1 | sed -n '3p' | awk '{print $NF}')
  print -r -- "{\"t\":\"$(date -u +%FT%TZ)\",\"poll\":$i,\"status\":\"$st\"}" >> status-history.jsonl
  if [[ "$st" != "IN_PROGRESS" && "$st" != "QUEUED" && -n "$st" ]]; then
    print -r -- "TERMINAL: $st"
    aristotle download $PROJ --destination result.tar.gz > download-output.txt 2>&1
    exit 0
  fi
  sleep 30
done
print -r -- "TIMEOUT"
exit 1
