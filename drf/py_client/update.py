import requests

# endpoint = "https://httpbin.org/"

data = {
    "title":"updated Title",
    "content":"updated content"
}
endpoint = "http://127.0.0.1:8000/api/products/1/update/"
getResponse = requests.put(endpoint,json = data)
print(getResponse.json())