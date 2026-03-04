#!/usr/bin/env bash
set -euo pipefail

TOTAL=50

print_sep() {
  echo "=========================================================================="
}

run_test() {
  echo "Showing sample responses..."
  for i in $(seq 1 10); do
    RESPONSE=$(curl -s --resolve h5-q4.local:18081:127.0.0.1 http://h5-q4.local:18081/)
    printf "Request %2d → %s\n" "$i" "$RESPONSE"
  done
  echo
  echo "Showing summary results..."
  for i in $(seq 1 $TOTAL); do
    curl -s --resolve h5-q4.local:18081:127.0.0.1 http://h5-q4.local:18081/
  done | sort | uniq -c | awk -v total=$TOTAL '
  {
    percent = ($1/total)*100
    printf "%-12s : %2d (%.0f%%)\n", $2" "$3, $1, percent
  }'
}

# Testing for initial canary split
print_sep
echo "Showing initial canary split: 20/80..."
run_test

# Promoting to 50%
print_sep
echo "Promoting canary to 50%..."
kubectl annotate ingress canary-ingress nginx.ingress.kubernetes.io/canary-weight="50" --overwrite
kubectl describe ingress canary-ingress
sleep 5
run_test

# Promoting to 100%
print_sep
echo "Promoting canary to 100%..."
kubectl annotate ingress canary-ingress nginx.ingress.kubernetes.io/canary-weight="100" --overwrite
kubectl describe ingress canary-ingress
sleep 5
run_test