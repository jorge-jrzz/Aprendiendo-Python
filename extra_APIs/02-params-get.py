
import requests

URL = 'http://httpbin.org/get'

params = {
    'name': 'Jorge Juarez',
    'password': '123', 
    'email': 'jorgeang33@gmail.com'
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    payload = response.json()
    params = payload['args']

    print(params['name'])
    print(params['password'])
    print(params['email'])