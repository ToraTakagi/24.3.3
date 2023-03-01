import requests
import json


url = 'https://petstore.swagger.io/v2'

# Создание пользователя (POST)
data_post = json.dumps({"id": 0, "username": "ToraTakagi", "firstName": "Tora", "lastName": "Takagi", "email": "zahard@inbox.ru", "password": "Qwerty123", "phone": "123", "userStatus": 0})
res = requests.post('https://petstore.swagger.io/v2/user', headers={'Content-type': 'application/json', 'accept': 'application/json'}, data=data_post)
print("POST new user ToraTakagi\n", res.status_code, res.json())

# Проверка наличия пользователя (GET)
res = requests.get(f'{url}/user/ToraTakagi', headers={'accept': 'application/json'})
print("GET new user ToraTakagi\n", res.status_code, res.json())
print("res_id = ", res.json)

# Аутотентификация (GET)
res = requests.get(f'{url}/user/login', params={'username' : 'ToraTakagi', 'password' : 'Qwerty123'}, headers={'accept': 'application/json'})
print("GET for logs user ToraTakagi", res.status_code, res.json())

# Изменение данных пользователя (PUT)
data_put = json.dumps({"id": 0, "username": "ZaHard", "firstName": "Za", "lastName": "Hard", "email": "zahard@mail.ru", "password": "Qwerty123", "phone": "(921)9000001", "userStatus": 0})
res = requests.put('https://petstore.swagger.io/v2/user/ToraTakagi', headers={'Content-type': 'application/json', 'accept': 'application/json'}, data=data_put)
print("PUT user ToraTakagi to ZaHard\n", res.status_code, res.json())

# Проверка изменений (GET)
res = requests.get(f'{url}/user/ZaHard', headers={'accept': 'application/json'})
print("GET user ZaHard\n", res.status_code, res.json())

# Удаление пользователя  (DELETE)
res = requests.delete(f'{url}/user/ZaHard')
print("DELETE user\n", res.status_code, res.json())

# Проверка удаления (GET)
res = requests.get(f'{url}/user/ZaHard', headers={'accept': 'application/json'})
print("GET deleted user ZaHard\n", res.status_code, res.json())

# Проверка наличия пользователя (GET)
res = requests.get(f'{url}/user/ToraTakagi', headers={'accept': 'application/json'})
print("GET user ToraTakagi\n", res.status_code, res.json())

# Удаление пользователя  (DELETE)
res = requests.delete(f'{url}/user/ToraTakagi')
print("DELETE user\n", res.status_code, res.json())

# Проверка удаления (GET)
res = requests.get(f'{url}/user/ToraTakagi', headers={'accept': 'application/json'})
print("GET user ToraTakagi\n", res.status_code, res.json())