import requests
import time

REGISTRY_URL = "http://localhost:9000"
SERVICE_NAME = "read-service"
HOST = "127.0.0.1"
PORT = 8001

def register():
    requests.post(
        f"{REGISTRY_URL}/register",
        json={
            "name": SERVICE_NAME,
            "host": HOST,
            "port": PORT,
            "last_heartbeat": time.time()
        }
    )
