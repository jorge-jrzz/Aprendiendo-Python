
import requests

URL = 'http://httpbin.org/post'

data = {
    'username': 'jorge', 
    'password': 'pasword123'
}

response = requests.post(URL, data=data)

if response.status_code == 200:
    payload = response.json()
    print(response.text)

    print(response.url)

