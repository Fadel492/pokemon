from re import I
from pokemons import Pokemons
from abc import ABC
class Combat(ABC):
    @staticmethod
    def attaquer(attaquant:Pokemons,defenseur:Pokemons):
        i=0
        j=0
        while(defenseur.hp>0 and attaquant.hp>0):
            attaquant.attaquer_pokemons(defenseur)
            i=i+1
            print(i)
            defenseur.attaquer_pokemons(attaquant)
            j=j+1
            print(j)
        if(defenseur.hp>0):
            print(f"{defenseur.nom} a gagne")
        else:
            print(f"{attaquant.nom} a gagné")
        

