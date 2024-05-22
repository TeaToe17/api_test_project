import requests

# endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/products/123456789098765432/"
getResponse = requests.get(endpoint)
print(getResponse.json())