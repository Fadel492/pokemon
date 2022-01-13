from pokemons import Pokemons
class PokemonEau(Pokemons):
    
    def __init__(self, nom, hp, atk):
        super().__init__(nom, hp, atk)

    def attaquer_pokemon(self,cible):
        if type(cible)=="PokemonPlante" or type(cible)=="PokemonEau":
            degat = self.atk*0.5
        else:
            degat = self.atk*2
        return degat

    