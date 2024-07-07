# Project Details

- I developed a scalable and highly available data processing pipeline using Kubernetes and Kafka to process document streams in real-time, integrating with a distributed Neo4j setup.
- Initially we had a setup to process the data using docker and neo4j, however this setup failed to handle increased data loads, ensure system reliability. Hence we moved the infrastructure from docker to an environment where scalability and reliability can be ensured.
- We used the NYC Taxi Cab dataset, which includes extensive trip records of New York City cabs. This dataset provides pick-up and drop-off locations, trip duration, distance, fare amount etc.
- The process began with ingesting data into kafka in small batches, where kafka acted as data ingestion layer.
- While setting up kafka, minikube acted as orchestrator and zookeeper ensured reliability. When the data was published to kafka topics, kafka Connect is used to facilitate seamless transfer of data from kafka to neo4j. The connector also mapped the data in the required format, i. e locations were nodes and routes were the relationships in graph database.
- Neo4j is deployed in kubernetes environment. One the data is in Neo4j, realtime analytics were performed. The project included performing page rank and breadth first algorithm to analyze graph data. Page Rank enabled to evaluate the significance of locations in the graph in our case it would be popular pickups, Breadth first search was implemented to identify optimized traversal between locations.





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


