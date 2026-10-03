#!/usr/bin/env bash
# Usage: run.sh <model> <run-number> <document.md>
# Runs the bake-off prompt on one document with no tools, no project settings, no MCP servers.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
model="$1"; n="$2"; doc="$3"
tag="$(basename "$(dirname "$doc")")"; mkdir -p "$here/runs/$tag"
out="$here/runs/$tag/${model}-${n}.json"
work="${TMPDIR:-/tmp}/t027-$tag-$model-$n"; mkdir -p "$work"
start=$(date +%s)
cat "$here/prompt.md" "$doc" | (cd "$work" && claude -p --model "$model" --output-format json \
  --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence) > "$out"
echo "$model run $n: $(( $(date +%s) - start )) s wall -> $out"
