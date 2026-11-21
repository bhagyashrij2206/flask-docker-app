# Flask Docker App

[![CI/CD](https://github.com/bhagyashrij2206/flask-docker-app/actions/workflows/ci.yml/badge.svg)](https://github.com/bhagyashrij2206/flask-docker-app/actions/workflows/ci.yml)

A small Python Flask web app packaged as a Docker image, with a GitHub Actions CI/CD pipeline.

## CI/CD pipeline
On every push and pull request to `main`, GitHub Actions:
1. Runs the unit tests with pytest
2. Builds the Docker image
3. Starts the container and checks `/health` (smoke test)
4. On push to `main`, publishes the image to GitHub Container Registry as `ghcr.io/bhagyashrij2206/flask-docker-app` (tags `latest` and the short commit SHA)

See [.github/workflows/ci.yml](.github/workflows/ci.yml).

## Endpoints
- `/` – home page
- `/health` – health check, returns `{"status": "ok"}`

## Run locally (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000

## Run with Docker
```powershell
docker build -t flask-docker-app .
docker run -d -p 5000:5000 --name flask-app flask-docker-app
```
Open http://localhost:5000

Stop and remove the container:
```powershell
docker stop flask-app
docker rm flask-app
```

## Run the tests
```powershell
pip install pytest
pytest -v
```

## Tech
Python 3.12 · Flask · Gunicorn · Docker · pytest · GitHub Actions · GHCR
