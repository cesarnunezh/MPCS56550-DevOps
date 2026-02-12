#!/usr/bin/env bash
set -euo pipefail

# Usage: ./rollback.sh <old_version>
old_version="${1:-}"
new_version="${2:-}"

if [[ -z "$new_version" ]]; then
  echo "Usage: $0 <old_version> <new_version>"
  echo "Example: $0 v1.0 v1.1"
  exit 1
fi


# Creating the blue deployment environment
echo "=========================================================================="
echo "Creating the Blue deployment from blue-deployment.yaml..."
kubectl apply -f ./blue-deployment.yaml
echo
sleep 5

# Initial state of deployment
echo "Initial state of blue deployment..."
kubectl get deploy h5-q3-blue
echo
sleep 5
kubectl get pods -l app=nginx,color=blue -o wide
echo

# Exposing the app 
echo "Exposing the app..."
kubectl apply -f ./blue-green-service.yaml 
echo
echo "Current image running: $(kubectl get deploy h5-q3-blue -o=jsonpath='{.spec.template.spec.containers[0].image}'; echo)"

echo "=========================================================================="
echo "Describing service..."
kubectl describe service h5-q3-service
echo

echo "=========================================================================="
# Creating the green deployment environment
echo "Initializing Blue-Green Deployment..."
echo "Creating the Green deployment from green-deployment.yaml..."
kubectl apply -f ./green-deployment.yaml
echo

# Initial state of deployment
echo "=========================================================================="
echo "Initial state of deployment after the creation of Green environment..."
kubectl get pods -l app=nginx -o wide
echo

echo "=========================================================================="
echo "Final state of deployment after the creation of Green environment..."
sleep 10
kubectl get pods -l app=nginx -o wide

# Migrating the services 
echo "=========================================================================="
echo "Migrating service to Green environment..."
./switch-traffic.sh $new_version
echo

if kubectl get pods -l app=nginx,color=green -o json \
  | jq -e '(.items | length) > 0 and all(.items[]; all(.status.containerStatuses[]?; .ready == true))' \
  >/dev/null
then
  echo "=========================================================================="
  echo "Green is Ready with 2 pod running. Safe to clean up blue pods."
  kubectl scale deployment h5-q3-blue --replicas=0
  echo "Showing all available pods"
  kubectl get pods -l app=nginx -o wide
else
  echo "Green failed. Rolling back to blue."
  ./rollback.sh $old_version
fi
echo

echo "=========================================================================="
echo "Describing service..."
kubectl describe service h5-q3-service