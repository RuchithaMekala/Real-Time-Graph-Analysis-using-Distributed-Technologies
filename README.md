# README

1. To install Minikube:
   1. `brew install minikube` to install.
   2. `minikube config set driver docker` to set docker as my default driver

2. To deploy:
   1. Configured the service and deployment sections in the yaml file
   2. `minikube start -p CSE511-project2-phase2` to start the cluster
   3. `kubectl apply -f ./kafka-setup.yaml` and `kubectl apply -f ./zookeeper-setup.yaml` to deploy the pods.

3. Verified the deployment in two ways:

Sending data from local host to Kafka using the following command:

    kubectl port-forward <kafka-pod-name> 29092
    echo "hello Kafka" | kcat -P -b localhost:29092 -t test
    kcat -C -b localhost:29092 -t test

Checking connectivity between zookeeper and kafka and listing the kafka broker id and topics.

    kubectl exec -it <kafka-pod-name> -- /bin/bash
    zookeeper-shell.sh zookeeper-service:2181
    ls /brokers/ids
    ls /brokers/topics


