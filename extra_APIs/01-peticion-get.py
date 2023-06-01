
import requests

URL = 'http://httpbin.org/get'

# Realiza una peticio a travez de del metodo get
response = requests.get(URL)

print(response)
print(response.status_code)
print(response.text)    # Objeto de tipo string
print(response.json())  # Objeto de tipo diccionario

payload = response.json()
print(payload.get('origin'))

print(response.url)