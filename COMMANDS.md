# Module 3 - Command Reference for Screenshots

## Initial Setup
```powershell
# Create directory structure
mkdir module3
cd module3
mkdir service-a, service-b, proxy
```

## Service A - Basic Flask Application
```powershell
cd service-a

# Create app.py with Flask application
# Install Flask
pip install flask

# Test locally (before Docker)
python app.py
# Verify: http://localhost:5001
```

## Dockerize Service A
```powershell
# Create Dockerfile
# Build Docker image
docker build -t service-a .

# Run container
docker run -p 5001:5001 service-a
# Verify: http://localhost:5001
```

## Service B - Second Microservice
```powershell
cd ../service-b

# Create app.py with /data endpoint
# Create Dockerfile
docker build -t service-b .
docker run -p 5002:5002 service-b
# Verify: http://localhost:5002/data
```

## Service Registry Implementation
```powershell
cd ../service-a

# Updated app.py with requests library and registry.json support
# Created registry.json with Service B location
# Updated Dockerfile to include requests and registry.json

# Create Docker network
docker network create microservices-network

# Rebuild and run with network
docker build -t service-a .
docker stop service-a-container; docker rm service-a-container
docker run -d -p 5001:5001 --name service-a-container --network microservices-network service-a

docker stop service-b-container; docker rm service-b-container
docker run -d -p 5002:5002 --name service-b-container --network microservices-network service-b
```

## Proxy Service (API Gateway)
```powershell
cd ../proxy

# Create app.py with routes for /service-a and /service-b
# Create Dockerfile
docker build -t proxy .
docker run -d -p 8000:8000 --name proxy-container --network microservices-network proxy

# Verify:
# http://localhost:8000/service-a
# http://localhost:8000/service-b
```

## Deployment Automation
```powershell
cd ..

# Create deploy.sh (Linux/Mac)
# Create deploy.ps1 (Windows)

# Test deployment script
.\deploy.ps1
```

## Jenkins CI/CD
```powershell
# Run Jenkins container
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-container -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

# Get initial password
docker exec jenkins-container cat /var/jenkins_home/secrets/initialAdminPassword

# Access Jenkins: http://localhost:8080
# Create Pipeline with Jenkinsfile
```

## Git Repository
```powershell
# Initialize Git
git init
git add .
git commit -m "Module 3: Microservices with Service Registry, Proxy and Jenkins"

# Add remote and push
git remote add origin https://github.com/D-Jerlin-Seraphina/Micro-services-Service-Registry-Proxy-and-Jenkins.git
git branch -M main
git push -u origin main
```

## Verification Commands
```powershell
# Check running containers
docker ps

# View container logs
docker logs service-a-container
docker logs service-b-container
docker logs proxy-container

# Test endpoints
Invoke-WebRequest -UseBasicParsing http://localhost:5001
Invoke-WebRequest -UseBasicParsing http://localhost:5002/data
Invoke-WebRequest -UseBasicParsing http://localhost:8000/service-a
Invoke-WebRequest -UseBasicParsing http://localhost:8000/service-b

# View network
docker network ls
docker network inspect microservices-network
```

## Key Information

### Jenkins Access
- **URL**: http://localhost:8080
- **Initial Password**: a582ae32ddd947c1b90ca844ab3cadfc

### Service Endpoints
- **Service A**: http://localhost:5001
- **Service B**: http://localhost:5002/data
- **Proxy → Service A**: http://localhost:8000/service-a
- **Proxy → Service B**: http://localhost:8000/service-b

### GitHub Repository
https://github.com/D-Jerlin-Seraphina/Micro-services-Service-Registry-Proxy-and-Jenkins.git

### Docker Network
All services communicate through: `microservices-network`

## Screenshots Checklist

✓ 1. Directory structure (service-a, service-b, proxy folders)
✓ 2. Service A app.py code
✓ 3. Service A Dockerfile
✓ 4. Docker build service-a output
✓ 5. Docker run service-a output
✓ 6. Service A running in browser (http://localhost:5001)
✓ 7. Service B app.py code
✓ 8. Service B Dockerfile
✓ 9. Docker build service-b output
✓ 10. Service B running in browser (http://localhost:5002/data)
✓ 11. Updated Service A with registry.json
✓ 12. registry.json content
✓ 13. Docker network creation
✓ 14. All containers running (docker ps)
✓ 15. Proxy app.py code
✓ 16. Proxy Dockerfile
✓ 17. Proxy service running
✓ 18. Proxy accessing Service A (http://localhost:8000/service-a)
✓ 19. Proxy accessing Service B (http://localhost:8000/service-b)
✓ 20. deploy.sh / deploy.ps1 script
✓ 21. Deployment script execution
✓ 22. Jenkinsfile content
✓ 23. Jenkins container running
✓ 24. Jenkins initial setup page
✓ 25. Git repository initialization
✓ 26. Git commit output
✓ 27. Git push to GitHub
✓ 28. GitHub repository page
✓ 29. All services verification
✓ 30. Final docker ps showing all containers
