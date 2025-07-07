import requests


class PokemonSprite:
    def __init__(self, data):
        self.data = data

    def download_sprite(self):
        if not self.data:
            raise ValueError("No data available. Ensure data is fetched first.")
        sprite_url = self.data['sprites']['other']['official-artwork']['front_default']
        img_response = requests.get(sprite_url)
        if img_response.status_code == 200:
            with open("sprite.png", "wb") as f:
                f.write(img_response.content)
        else:
            raise Exception("Failed to download sprite")
