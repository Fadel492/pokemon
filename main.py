from combat import Combat
from pokemon_eau import PokemonEau
from pokemon_plante import PokemonPlante
from pokemon_feu import PokemonFeu
from pokemons import Pokemons

weavile = PokemonPlante ('PokemonPlante', 150,10) 
garchomp = PokemonEau ('PokemonEau', 250,20)
roserade = PokemonFeu ('PokemonFeu', 160,5)

Combat.attaquer(weavile,garchomp)