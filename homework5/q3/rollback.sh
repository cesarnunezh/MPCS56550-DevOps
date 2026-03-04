#!/usr/bin/env bash
set -euo pipefail

# Usage: ./rollback.sh <old_version>
old_version="${1:-}"
if [[ -z "$old_version" ]]; then
  echo "Usage: $0 <old_version>"
  echo "Example: $0 v1.0"
  exit 1
fi

echo "=========================================================================="
echo "Restoring 2 replicas at blue environment..."
kubectl scale deployment h5-q3-blue --replicas=2
sleep 5

echo "Rolling back service to blue pods"
kubectl patch service h5-q3-service -p "$(jq -n --arg v "$old_version" \
  '{spec:{selector:{app:"nginx",version:$v,color:"blue"}}}')"

echo "Final state of deployment after the rollback..."
kubectl get pods -l app=nginx
echo "Describing service..."
kubectl describe service h5-q3-service