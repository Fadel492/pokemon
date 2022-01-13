from pokemons import Pokemons
class PokemonPlante(Pokemons):
    def __init__(self,nom,hp,atk):
        super().__init__(nom,hp,atk)

    def cattaquer_pokemon(self,cible):
        if type(cible)=="PokemonFeu" or type(cible)=="PokemonPlante":
            degat = self.atk*0.5
        else:
            degat = self.atk*2
        return degat

    