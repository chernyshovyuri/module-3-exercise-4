import constants as con


class Spell:

    name: str
    effect: str
    mana = con.MANANONE

    def __init__(self, name: str, effect: str, mana = con.MANANONE):

        self.__name = name
        self.__effect = effect
        self.__mana = mana


    def __str__(self):
        return f'Name:{self.__name}\nEffect:{self.__effect}\nMana:{self.__mana}'

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








