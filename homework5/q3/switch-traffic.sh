#!/usr/bin/env bash
set -euo pipefail

# Usage: ./switch-traffic.sh <new_version>
new_version="${1:-}"
if [[ -z "$new_version" ]]; then
  echo "Usage: $0 <new_version>"
  echo "Example: $0 v1.1"
  exit 1
fi

kubectl patch service h5-q3-service -p "$(jq -n --arg v "$new_version" \
  '{spec:{selector:{app:"nginx",version:$v,color:"green"}}}')"

kubectl get pods -l app=nginx,version="$new_version"