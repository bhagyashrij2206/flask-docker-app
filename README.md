# Flask Docker App

A small Python Flask web app packaged as a Docker image.

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

## Tech
Python 3.12 · Flask · Gunicorn · Docker
