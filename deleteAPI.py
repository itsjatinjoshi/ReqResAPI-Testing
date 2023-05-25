import requests

url = "https://reqres.in/api/users/"
param = {"id": 795}

delete_request = requests.delete(url, params=param)
assert delete_request.status_code == 204

print(delete_request.text)
