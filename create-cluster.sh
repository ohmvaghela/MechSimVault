#!/bin/bash

mode=$1

if [ "$mode" != "gke" ] && [ "$mode" != "minikube" ]; then
  echo "Invalid mode. Only 'gke' and 'minikube' are supported."
  exit 1
fi

kubectl apply -f kubernetes/configs/namespace.yaml
kubectl apply -f kubernetes/configs/cm.yaml
kubectl apply -f kubernetes/configs/secret.yaml

if [ "$mode" = "gke" ]; then

  gcloud compute addresses create mechsimvault-backend --global --ip-version=IPV4
  gcloud compute addresses create mechsimvault-frontend --global --ip-version=IPV4

  kubectl apply -f kubernetes/configs/ingress.yaml
  kubectl apply -f kubernetes/configs/mcrt.yaml
  kubectl apply -f kubernetes/configs/pvc.yaml

elif [ "$mode" = "minikube" ]; then
  kubectl apply -f kubernetes/configs/pvc-minikube.yaml
  kubectl apply -f kubernetes/configs/storage-class.yaml
fi

kubectl apply -f kubernetes/deploy/mysql-statefulset.yaml
kubectl apply -f kubernetes/deploy/server.yaml
kubectl apply -f kubernetes/deploy/client.yaml
kubectl apply -f kubernetes/deploy/nginx.yaml