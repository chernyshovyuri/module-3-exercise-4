import constants as con
from __future__ import annotations
import random


class Spell:

    __name: str
    __effect: str
    __mana: int

    def __init__(self, name: str, effect: str, mana: int = con.MANANONE):

        if not isinstance(name, str):  raise TypeError()
        if not isinstance(effect, str): raise TypeError()
        if not isinstance(mana, (int, float)): raise TypeError()

        self.__name = name
        self.__effect = effect
        self.__mana = mana


    def __str__(self):
        return f'Name:{self.__name}\nEffect:{self.__effect}\nMana:{self.__mana}'

    def __repr__(self):
        return f"{self.__name}"

    def get_name(self):

        return self.__name

    def get_effect(self):

        return self.__effect

    def get_mana(self):

        return self.__mana

    def set_mana(self, new_mana: int) -> bool:

        if new_mana < 0 or new_mana > con.PRIMALMANA:  return False

        self.__mana = new_mana

        return True


    @staticmethod
    def copy_spell(original):
        return Spell(original.__name, original.__effect, original.__mana)



class HogwardStudent:

    __name: str
    __faculty: str
    __mana: int
    __spell: list[Spell]


    def __init__(self, name: str, faculty: str, mana: int | float = con.PRIMALMANA, spell: list[Spell] = None):

        if not isinstance(name, str): raise TypeError()
        if not isinstance(faculty, str): raise TypeError()
        if not isinstance(mana, (int, float)): raise TypeError()
        if not isinstance(spell, list): raise TypeError()

        self.__name = name
        self.__faculty = faculty
        self.__mana = mana
        self.__spell = spell or []


    def __str__(self):
        return f"Name: {self.__name}\nFaculty: {self.__faculty}\nMana: {self.__mana}\nspell: {self.__spell}"


    def get_name(self):
        return self.__name

    def get_faculty(self):
        return self.__faculty

    def get_mana(self):
        return self.__mana

    def get_spell(self):
        return self.__spell


    def set_mana(self, new_mana: int) -> bool:

        if new_mana < 0 or new_mana > con.PRIMALMANA:  return False

        self.__mana = new_mana

        return True

    def add_spell(self, new_spell: Spell) -> bool:

        if new_spell not in self.__spell:
            self.__spell.append(new_spell)
            return True
        return False

    def cast_spell(self, target: HogwardStudent) -> bool:

        if not self.__spell:  return False

        random_spell = random.choice(self.__spell)

        new_mana = random_spell.get_mana()

        if self.__mana >= new_mana:
            self.__mana -= new_mana
            return True

        return False




































