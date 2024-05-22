import requests
from getpass import getpass

# endpoint = "localhost:8000/api/products/"
auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()

auth_response = requests.post(auth_endpoint, json = {"username":"user","password":password})
my_token = auth_response.json()
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"

    getResponse = requests.get(endpoint,headers = headers)
    print(getResponse.json())
print(my_token)