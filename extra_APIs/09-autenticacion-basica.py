
import requests
from getpass import getpass

URL = "http://httpbin.org/basic-auth/jorge/123"

password = getpass("Ingresa la contraseña: ")

session = requests.Session()
session.auth = ('jorge', password)

reponse = session.get(URL)

if reponse.status_code == 200:
    print(reponse.json())
elif reponse.status_code == 401:
    print("Unsuccessful authentication.")
