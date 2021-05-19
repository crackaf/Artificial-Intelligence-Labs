import requests

url = 'http://127.0.0.1:5000/'

r = requests.post(url, json={'img': "0.jpeg"})

print("from request file : ", r.json())
