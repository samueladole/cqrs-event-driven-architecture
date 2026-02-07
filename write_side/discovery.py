import requests

REGISTRY_URL = "http://localhost:9000"

def discover_read_service():
    response = requests.get(f"{REGISTRY_URL}/discover/read-service")
    data = response.json()

    return f"http://{data['host']}:{data['port']}"


# Example usage
# read_service_url = discover_read_service()
# requests.get(f"{read_service_url}/accounts/{account_id}")
