import requests

url = "https://reqres.in/api/users?"
param = {'page': 2}

get_response = requests.get(url, params=param)
assert get_response.status_code == 200
print(get_response.text)
