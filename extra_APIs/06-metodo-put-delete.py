
import requests

# GET = get
# POST = post 
# PUT = put 
# DELETE = delete 

URL = 'http://httpbin.org/delete'
# URL = 'http://httpbin.org/put'

# response = requests.put(URL, 
response = requests.delete(URL, 
                        params={'name': 'Jorge'}, 
                        headers={'version': '2.0'}, 
                        data={'id': 1})

if response.status_code == 200:
    print(response.text)
else:
    print("A ocurrido un error")