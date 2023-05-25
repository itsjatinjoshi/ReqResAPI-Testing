import requests

url = "https://reqres.in/api/users/"
param = {"id":795}

put_request = requests.put(url, params=param)

assert put_request.status_code ==200
print(put_request.text)