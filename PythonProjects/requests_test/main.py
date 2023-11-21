import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                        json={
                             "name": "Котик",
                             "photo": "https://dolnikov.ru/pokemons/albums/012.png"
                             },
                             headers={'Content-Type': 'application/json','trainer_token': '02bac806dea7865bf0c50f473c4b15e8'}, timeout=5)

print(response)

response = requests.patch(url='https://api.pokemonbattle.me:9104/pokemons',
                        json={
                             "pokemon_id": "12704",
                             "name": "New Name"
                             },
                             headers={'trainer_token': '02bac806dea7865bf0c50f473c4b15e8', 'Content-Type': 'application/json'}, timeout=5)

print(response)

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                        json={
                             "pokemon_id": "20054",
                             },
                             headers={'trainer_token': '02bac806dea7865bf0c50f473c4b15e8', 'Content-Type': 'application/json'}, timeout=5)

print(response)