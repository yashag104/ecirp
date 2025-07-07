class PokemonDetails:
    def __init__(self, data):
        self.data = data

    def display(self):
        if not self.data:
            raise ValueError("No data available. Ensure data is fetched first.")
        national_number = self.data['id']
        name = self.data['name'].capitalize()
        type_ = ', '.join([t['type']['name'].capitalize() for t in self.data['types']])
        abilities = ', '.join([a['ability']['name'].capitalize() for a in self.data['abilities']])
        height = self.data['height'] / 10
        weight = self.data['weight'] / 10
        stats = {stat['stat']['name']: stat['base_stat'] for stat in self.data['stats']}
        base_stats = f"HP: {stats['hp']} Attack: {stats['attack']} Defense: {stats['defense']} Special Attack: {stats['special-attack']} Special Defense: {stats['special-defense']} Speed: {stats['speed']}"
        print(f"Name: {name}")
        print(f"National Number: {national_number}")
        print(f"Type: {type_}")
        print(f"Abilities: {abilities}")
        print(f"Height: {height} m")
        print(f"Weight: {weight} kg")
        print("Base Stats:", base_stats)
