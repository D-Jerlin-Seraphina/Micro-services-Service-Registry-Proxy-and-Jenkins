# Deploy Service A
docker build -t service-a service-a
docker stop service-a-container
docker rm service-a-container
docker run -d -p 5001:5001 --name service-a-container --network microservices-network service-a

Write-Host "Service A deployed successfully"
