import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'
      
def test_status_code():
    response = requests.get(url=f'{HOST}/trainer', params={'trainer_id' : 2673}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code for /trainers'
    assert response.json()['trainer_name'] =='мур' 


def test_parametrize():
    response = requests.get(url=f'{HOST}/trainer', params={'trainer_id' : 2673}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code for /trainers'

    response = requests.get(url=f'{HOST}/trainer', params={'trainer_id' : 2674}, timeout=5)
    assert response.status_code == 400, 'Unexpected status code for /trainers'