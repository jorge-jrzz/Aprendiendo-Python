import requests

URL = 'https://randomuser.me/api/'

count = int(input("Ingresa la cantidad de usuarios que desea visualizar: "))

response = requests.get(URL, params={'results': count})

if response.status_code == 200:
    payload = response.json()
    results = payload.get('results')

    for user in results:
        name = user.get('name') # diccionario
        
        print("{title}, {first} {last}".format(**name))
        # print(f"{name['title']}, {name['first']} {name['last']}")