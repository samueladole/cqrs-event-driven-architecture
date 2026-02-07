import time
from registry.main import registry

def remove_dead_services(ttl=30):
    now = time.time()
    for name, service in list(registry.items()):
        if now - service.last_heartbeat > ttl:
            del registry[name]
