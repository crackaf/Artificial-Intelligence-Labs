import requests

url = 'http://127.0.0.1:5000/'

r = requests.post(url, json={'Pclass': 1, 'Sex': 0, 'Age': 30,
                  'SiSp': 0, 'Parch': 0, 'Fare': 100, 'Embarked': 0})

print("from request file : ", r.json())
