# Into the Kubernetes-Verse: Deploying into a Cluster

## Overview

This homework assignment extends homework 5's Redis-Flask application by deploying it in a Kubernetes cluster.

## Files

the files in this project are `app.py` hosting the app scripts and routes, `Dockerfile` to build and containerize the application, and this README. the dataset `ml_data_sample` can be downloaded through this command:

```
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

In addition to these files, the Kubernetes `.yaml` files are also included for kubernetes configuration. They include:

```
aneeshroy-test-redis-pvc.yml
aneeshroy-test-redis-deployment.yml
aneeshroy-test-redis-service.yml
aneeshroy-test-flask-deployment.yml
aneeshroy-test-flask-service.yml
```

## Instructions for Deployment

First, make sure you are in a Kubernetes cluster, which for this class (if logged into the class server) can be done through the command

```
sshar68498@coe332-k8s.tacc.cloud
```

With your own username. After this, with the files ready, simply run

```
kubectl apply -f aneeshroy-test*
```

and the `.yml` files should have all ran. You can check by running `kubctl get pods` and see the different pods the commands have created. Now, run

```
kubectl get services
```
and note the IP address of the `aneeshroy-test-flask-service` service running. You will need this to run commands for the application.

Now, enter any pod's terminal through 

```
kubectl exec -it <pod-name> -- /bin/bash
```
now, to run commands, use

```
curl <flask-service-IP>:5000/data -X POST
```
and the data should be loaded, and run it again minus the `-X POST` to see the data available.
