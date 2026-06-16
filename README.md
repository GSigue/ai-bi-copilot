## 🐳 Docker Setup

This project is fully containerized using Docker.

### Build image
docker build -t ai-bi-copilot .

### Run container
docker run -p 8000:8000 ai-bi-copilot

### OR using docker-compose
docker-compose up --build
