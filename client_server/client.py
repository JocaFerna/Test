import requests

def request_server():
    response = requests.get("http://localhost:8080")
    print(f"Client received: {response.text}")

if __name__ == "__main__":
    request_server()