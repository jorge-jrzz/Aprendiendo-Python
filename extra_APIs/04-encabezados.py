
import requests

URL = 'http://httpbin.org/post'

# 1. Query -> GET
# 2. Cuerpo de la petición  -> POST
# 3. Encabezado -> ALL

headers = {
    'course': 'Curso de Python', 
    'version': '2.0', 
    'author': 'Eduardo Ismael'
}

params = {
    'platform': 'codigoFacilito'
}

data = {
    'username': 'jorge', 
    'password': '1234'
}

response = requests.post(URL, headers=headers, params=params, data=data)

if response.status_code == 200:
    print(response.text)
    print(response.url)