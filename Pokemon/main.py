import pokemon_sprite
import pokemon_details
import pokemon_fetcher
import sys


def main(name):
    try:
        fetcher = pokemon_fetcher.PokemonFetcher(name)
        data = fetcher.get_data()
        details = pokemon_details.PokemonDetails(data)
        details.display()
        sprite = pokemon_sprite.PokemonSprite(data)
        sprite.download_sprite()
        print("Sprite downloaded successfully as sprite.png")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
