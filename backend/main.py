import os
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


APP_NAME = os.getenv("APP_NAME", "k8s-cloud-native-demo")
APP_ENV = os.getenv("APP_ENV", "local")
APP_VERSION = os.getenv("APP_VERSION", "v1")
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
SECRET_TOKEN = os.getenv("SECRET_TOKEN", "local-token")


app = FastAPI(
    title="K8S Cloud Native Demo",
    description="A simple FastAPI backend for Docker and Kubernetes learning.",
    version=APP_VERSION
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {
        "message": "Hello from FastAPI backend",
        "app": APP_NAME,
        "env": APP_ENV,
        "version": APP_VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": int(time.time())
    }


@app.get("/ready")
def ready():
    return {
        "ready": True
    }


@app.get("/api/info")
def info():
    return {
        "app": APP_NAME,
        "env": APP_ENV,
        "version": APP_VERSION,
        "log_level": LOG_LEVEL,
        "description": "Backend service running with FastAPI. This is version v2."
    }


@app.get("/api/secret-check")
def secret_check():
    return {
        "secret_loaded": SECRET_TOKEN != "",
        "secret_preview": SECRET_TOKEN[:3] + "***"
    }
