import requests

url = "https://reqres.in/api/users"
param = {"name": "name", "job": "job"}

post_response = requests.post(url, params=param)

assert post_response.status_code == 201
print(post_response.text)