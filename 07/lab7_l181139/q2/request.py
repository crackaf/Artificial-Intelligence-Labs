import requests

url = 'http://127.0.0.1:5000/'

r = requests.post(
    url, json={'open': 120, 'High': 122, 'Low': 118, 'Change': 0.04})

print("from request file : ", r.json())
