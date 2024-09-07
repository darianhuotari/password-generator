#!/bin/bash

# Create cluster, port forward 8081 to 80 on the k3d lb

k3d cluster create argocd --api-port 6550 -p "8081:80@loadbalancer" --agents 2

# Install argocd, create configmap for use in k3d and ingress
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
# this can also be done via something like kubectl patch deploy argocd-server -n argocd --type json -p '[{"op": "replace", "path": "/spec/template/spec/containers/0/command", "value": ["argocd-server", "--insecure", "--staticassets","/shared/app"]}]'
# since we have to create an ingress, we use the configmap in the same file
kubectl apply -f cm-and-ingress.yaml

# Redeploy to apply configmap changes
kubectl -n argocd rollout restart deploy argocd-server

# Wait for pod
kubectl wait pods --timeout=120s --for=condition=Ready -n argocd -l app.kubernetes.io/name=argocd-server

# Fetch default password
defaultPass=`kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`
echo "##### DEFAULT PASSWORD FOR ADMIN IS $defaultPass #####"

# Powershell can use something like:
# $defaultpass=kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}"
# [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String("$defaultpass"))

# ArgoCD will now be available in via http://localhost:8081/argocd