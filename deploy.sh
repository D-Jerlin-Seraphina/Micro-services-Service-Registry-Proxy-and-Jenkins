#!/bin/bash
# Deploy Service A
docker build -t service-a service-a
docker stop service-a-container || true
docker rm service-a-container || true
docker run -d -p 5001:5001 --name service-a-container --network microservices-network service-a

echo "Service A deployed successfully"
