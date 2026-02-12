# Creating the deployment from an nginx image
echo "=========================================================================="
echo "Deployment application from rolling-update-deployment.yaml..."
kubectl apply -f ./rolling-update-deployment.yaml
echo
sleep 5
# Initial state of deployment
echo "Initial state of deployment..."
kubectl get deploy h5-q2
echo
sleep 5
kubectl get pods -l app=nginx -o wide
echo

# Exposing the app 
echo "Exposing the app..."
kubectl apply -f ./rolling-update-service.yaml
echo
echo "Current image running: $(kubectl get deploy h5-q2 -o=jsonpath='{.spec.template.spec.containers[0].image}'; echo)"
echo


echo "=========================================================================="
# Updating to nginx:stable-alpine-perl
echo "Initializing Rolling update to nginx:stable-alpine-perl..."
kubectl set image deployments/h5-q2 nginx=nginx:stable-alpine-perl

# Watch the rollout status 
kubectl rollout status deployment/h5-q2 --watch=true
echo

echo "=========================================================================="
echo "Rolling update completed..."
kubectl get pods -l app=nginx -o wide
echo "Current image running: $(kubectl get deploy h5-q2 -o=jsonpath='{.spec.template.spec.containers[0].image}'; echo)"
echo
echo "=========================================================================="

echo "=========================================================================="
echo "Initializing Rollback"
kubectl rollout undo deployment/h5-q2
kubectl rollout status deployment/h5-q2
echo "Rollback completed..."
echo "Current image running: $(kubectl get deploy h5-q2 -o=jsonpath='{.spec.template.spec.containers[0].image}'; echo)"
echo

# echo "=========================================================================="
# echo "Accessing to the app"
# minikube service h5-q2 --url
# sleep 5
# curl http://127.0.0.1:46661
# echo "=========================================================================="

# Delete all
# echo "Deleting all deployments and services..."
# kubectl delete -n default service h5-q2
# kubectl delete -n default deployment h5-q2