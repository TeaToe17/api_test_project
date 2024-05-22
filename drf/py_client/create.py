import requests

headers = {'Authorization': 'Bearer 9416606a6bba4f744238a0a86d99e6f8a6a71b1a'}

# endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title":"Test Title 333"
}
getResponse = requests.post(endpoint,json = data,headers=headers)
print(getResponse.json())