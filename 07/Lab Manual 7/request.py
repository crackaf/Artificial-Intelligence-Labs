import requests

url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={'income':20000, 'age':4, 'rooms':5,'brooms':2,'population':12000})

print("from request file : ", r.json())