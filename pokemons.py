from __future__ import annotations
from multiprocessing.sharedctypes import Value


class Pokemons(object):
    _nom: str
    _hp: int
    _atk: int

    def __init__(self, nom, hp, atk):
        self._atk = atk
        self._hp = hp
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,value):
        self._hp= value

    @property
    def atk(self):
        return self._atk

    def is_dead(self):
        if(self.hp == 0):
            print("Pokemon is dead")
        else:
            print("Pokemon is not dead")

    def attaquer_pokemons(self, p: Pokemons):
        #while(self.is_dead()=="pokemon is not dead"):
            p.hp = p.hp-self.atk
            print( f"{p.nom} deduit {self.atk} points d'une vie de {p.hp} du pokemon attaqué ")

    def __str__(self) -> str:
        return self
