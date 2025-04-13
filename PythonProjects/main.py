import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3b899bc63a1fbc071556ef7fe7f58739'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "evgeniaorlova1984@yandex.ru",
    "password": "Qastudio2025$"
}

body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change_name = {
    "pokemon_id": "287639",
    "name": "New",
    "photo_id": 2
}
body_add_pokeball = {
    "pokemon_id": "287654"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)


response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

message = response_change_name.json()['message']
print(message)


response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)