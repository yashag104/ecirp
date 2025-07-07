import requests


class PokemonFetcher:
    def __init__(self, name):
        self.name = name.lower()
        self.data = None

    def get_data(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()
        elif response.status_code == 404:
            raise ValueError("Invalid Pokémon name")
        else:
            response.raise_for_status()
        return self.data
