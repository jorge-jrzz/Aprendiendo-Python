
import requests

access_token = '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'

URL = 'https://api.github.com/user'

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {access_token}'
}

# Creamos una aplicacion en GitHub
# Obtenemos el codigo del usuarios -> https://github.com/login/oauth/authorize?client_id=<ClientID>&scope=user
# Realizamos una peticion para obtenes un access token -> https://github.com/login/oauth/access_token

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    username = response.json().get('login')
    print(username)
