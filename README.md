# Microservices with Service Registry, Proxy and Jenkins

## Module 3 - DevOps Project

This project demonstrates a complete microservices architecture with:
- **Service A**: Flask microservice on port 5001
- **Service B**: Flask microservice on port 5002
- **Service Registry**: Dynamic service discovery using registry.json
- **Proxy Service**: API Gateway on port 8000
- **Jenkins CI/CD**: Automated deployment pipeline

## Project Structure
```
module3/
├── service-a/
│   ├── app.py
│   ├── Dockerfile
│   └── registry.json
├── service-b/
│   ├── app.py
│   └── Dockerfile
├── proxy/
│   ├── app.py
│   └── Dockerfile
├── deploy.sh
├── deploy.ps1
└── Jenkinsfile
```

## Services

### Service A (Port 5001)
- Endpoint: `http://localhost:5001`
- Features: Service registry integration, calls Service B

### Service B (Port 5002)
- Endpoint: `http://localhost:5002/data`
- Returns: "Data from Service B"

### Proxy (Port 8000)
- Service A via Proxy: `http://localhost:8000/service-a`
- Service B via Proxy: `http://localhost:8000/service-b`

### Jenkins (Port 8080)
- URL: `http://localhost:8080`
- Initial Admin Password: `a582ae32ddd947c1b90ca844ab3cadfc`

## Docker Network
All services run in `microservices-network` for internal communication.

## Deployment
Run the deployment script:
```bash
# Linux/Mac
sh deploy.sh

# Windows
.\deploy.ps1
```

## Jenkins Pipeline
The Jenkinsfile includes:
1. **Build Stage**: Builds Docker images
2. **Deploy Stage**: Deploys services
3. **Verify Stage**: Checks deployment status

## GitHub Repository
https://github.com/D-Jerlin-Seraphina/Micro-services-Service-Registry-Proxy-and-Jenkins.git

## Testing
1. Test Service A: Open `http://localhost:5001`
2. Test Service B: Open `http://localhost:5002/data`
3. Test Proxy to Service A: Open `http://localhost:8000/service-a`
4. Test Proxy to Service B: Open `http://localhost:8000/service-b`
5. Access Jenkins: Open `http://localhost:8080`
