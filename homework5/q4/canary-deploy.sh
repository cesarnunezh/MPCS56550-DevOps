#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

print_sep() {
  echo "=========================================================================="
}

# Creating the stable environment
print_sep
echo "Creating the Stable deployment and service..."
kubectl apply -f ./stable-deployment.yaml
kubectl apply -f ./stable-service.yaml 
kubectl rollout status deployment/h5-q4-stable
echo
sleep 5

# Initial state of stable deployment
print_sep
echo "Initial state of stable deployment..."
kubectl get deploy h5-q4-stable
echo
kubectl get pods -l app=h5-q4,type=stable -o wide
echo

# Creating the canary environment
print_sep
echo "Creating the canary deployment, service and ingress manifests..."
kubectl apply -f ./canary-deployment.yaml
kubectl apply -f ./canary-service.yaml
kubectl apply -f ./canary-ingress.yaml
kubectl rollout status deployment/h5-q4-canary
echo

# Current state of stable and canary deployment
print_sep
echo "Stable + canary running:"
kubectl get deployments
kubectl get pods -l app=h5-q4 -o wide
echo

# Initiating canary split with 20/80 distribution
print_sep
echo "Showing initial canary split: 20/80..."
kubectl annotate ingress canary-ingress nginx.ingress.kubernetes.io/canary-weight="20" --overwrite
kubectl describe ingress canary-ingress
kubectl -n ingress-nginx port-forward svc/ingress-nginx-controller 18081:80

# Deleting all
kubectl delete -n default deployment h5-q4-canary
kubectl delete -n default deployment h5-q4-stable
kubectl delete -n default service canary-service
kubectl delete -n default service stable-service
kubectl delete -n default ingress stable-ingress
kubectl delete -n default ingress canary-ingress
