import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3b899bc63a1fbc071556ef7fe7f58739'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 28640

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
  
def test_status_code_1():
    response_1 = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_1.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'

def test_part_of_response_1():
    response_get_1 = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get_1.json()["data"][0]["trainer_name"] == 'Учитель'


@pytest.mark.parametrize('key, value', [{'name', 'Бульбазавр'}, {'trainer_id', TRAINER_ID}, {'id', '23694'}])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value