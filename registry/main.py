from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import time

app = FastAPI()


class ServiceInstance(BaseModel):
    name: str
    host: str
    port: int
    last_heartbeat: float


registry: Dict[str, ServiceInstance] = {}


@app.post("/register")
def register(service: ServiceInstance):
    registry[service.name] = service
    return {"status": "registered"}


@app.post("/heartbeat/{service_name}")
def heartbeat(service_name: str):
    if service_name in registry:
        registry[service_name].last_heartbeat = time.time()
        return {"status": "alive"}
    return {"error": "service not found"}


@app.get("/discover/{service_name}")
def discover(service_name: str):
    service = registry.get(service_name)
    if not service:
        return {"error": "service not found"}

    return {"host": service.host, "port": service.port}
