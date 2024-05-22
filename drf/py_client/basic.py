import requests

# endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/"
getResponse = requests.post(endpoint,json={"title":"Hello world of Tea"})
print(getResponse.json())

