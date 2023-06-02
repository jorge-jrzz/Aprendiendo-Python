
import requests
import webbrowser

from settings import CLIENT_ID
from settings import SECRET_ID

# Obtener código


def get_url_code():
    url = 'https://github.com/login/oauth/authorize'
    params = {
        'client_id': CLIENT_ID,
        'scope': 'user'
    }

    response = requests.get(url, params=params)

    return response.url

# Obtener accsess Token


def get_access_code(code):
    url = 'https://github.com/login/oauth/access_token'
    params = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'code': code
    }

    headers = {
        'Accept': 'application/json',
    }

    response = requests.post(url, params=params, headers=headers)
    if response.status_code == 200:
        payload = response.json()

        return payload.get('access_token')


# Obtener al usuario verificado
def get_user(access_token):
    url = 'https://api.github.com/user'

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()


if __name__ == '__main__':

    url = get_url_code()
    webbrowser.open_new_tab(url)

    code = input('Ingresa el codigo: ')
    code = code.strip().replace('\n', '')

    access_token = get_access_code(code)
    print(access_token)

    user = get_user(access_token)
    print(user)
