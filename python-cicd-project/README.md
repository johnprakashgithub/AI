# python-cicd-project/python-cicd-project/README.md

# Python CI/CD Project

This project is a containerized application consisting of multiple services: core, insights, salt-manager, test-runner, and edge-cdn. Each service is designed to perform specific functionalities and can be deployed independently or as part of a larger system.

## Project Structure

```
python-cicd-project
├── core
│   ├── src
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── insights
│   ├── src
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── salt-manager
│   ├── src
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── test-runner
│   ├── src
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── edge-cdn
│   ├── src
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── .gitignore
├── docker-compose.yml
├── ci
│   └── pipeline.yml
└── README.md
```

## Services

### Core
- **Description**: Contains the core logic and functionality of the application.
- **Entry Point**: `core/src/main.py`
- **Dependencies**: Listed in `core/requirements.txt`
- **Docker**: Built using `core/Dockerfile`

### Insights
- **Description**: Processes and generates insights from data.
- **Entry Point**: `insights/src/main.py`
- **Dependencies**: Listed in `insights/requirements.txt`
- **Docker**: Built using `insights/Dockerfile`

### Salt Manager
- **Description**: Manages salt configurations for the application.
- **Entry Point**: `salt-manager/src/main.py`
- **Dependencies**: Listed in `salt-manager/requirements.txt`
- **Docker**: Built using `salt-manager/Dockerfile`

### Test Runner
- **Description**: Runs tests for the application services.
- **Entry Point**: `test-runner/src/main.py`
- **Dependencies**: Listed in `test-runner/requirements.txt`
- **Docker**: Built using `test-runner/Dockerfile`

### Edge CDN
- **Description**: Handles content delivery and caching.
- **Entry Point**: `edge-cdn/src/main.py`
- **Dependencies**: Listed in `edge-cdn/requirements.txt`
- **Docker**: Built using `edge-cdn/Dockerfile`

## Getting Started

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd python-cicd-project
   ```

2. **Build the Docker images**:
   ```
   docker-compose build
   ```

3. **Run the services**:
   ```
   docker-compose up
   ```

## CI/CD Pipeline

The CI/CD pipeline is defined in `ci/pipeline.yml`. It automates the processes of building, testing, and deploying the services.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.