import requests

choice = int(input("What's the ID of the object you want to delete: "))

if choice:
    endpoint = f"http://127.0.0.1:8000/api/products/{choice}/delete/"
    getResponse = requests.delete(endpoint)
    if (getResponse.status_code >= 200 and getResponse.status_code < 300):
        print("Deleted")
else:
    print("No object matches that ID")