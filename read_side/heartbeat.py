import requests
import threading
import time

def start_heartbeat(service_name, registry_url):
    def beat():
        while True:
            requests.post(f"{registry_url}/heartbeat/{service_name}")
            time.sleep(10)

    thread = threading.Thread(target=beat, daemon=True)
    thread.start()
