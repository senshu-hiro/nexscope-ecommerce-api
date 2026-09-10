#!/usr/bin/env bash
# Requires curl 7.76+ and Python 3.10+. Run from any working directory.
set -euo pipefail
client_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../python" && pwd)"
if [[ $# -ne 2 && $# -ne 3 ]]; then
  echo 'Usage: bash examples/curl/run.sh SLUG PAYLOAD.json | SLUG --task TASK_ID' >&2
  exit 1
fi
: "${NEXSCOPE_API_KEY:?Set NEXSCOPE_API_KEY before calling the API}"
endpoint="$(python3 "$client_dir/run.py" "$@" --endpoint-only)"
if [[ "${2:-}" == '--task' ]]; then
  curl --silent --show-error --fail-with-body --max-time 120 "$endpoint" \
    -H "Authorization: Bearer $NEXSCOPE_API_KEY" -H 'Content-Type: application/json'
else
  curl --silent --show-error --fail-with-body --max-time 120 -X POST "$endpoint" \
    -H "Authorization: Bearer $NEXSCOPE_API_KEY" -H 'Content-Type: application/json' \
    --data-binary "@$2"
fi
printf '\n'
