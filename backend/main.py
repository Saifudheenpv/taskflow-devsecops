from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="TaskFlow API", version="1.0.0")

@app.get("/")
def root():
    return {
        "message": "Welcome to TaskFlow API",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "UP",
        "time": datetime.utcnow()
    }

@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "task": "Learn DevOps", "status": "In Progress"},
        {"id": 2, "task": "Build Kubernetes Project", "status": "Pending"}
    ]
