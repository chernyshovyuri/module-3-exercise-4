from __future__ import annotations
import constants as con
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


    def __init__(self, name: str, faculty: str, spell: list[Spell] = None):

        if not isinstance(name, str): raise TypeError()
        if not isinstance(faculty, str): raise TypeError()
        if not isinstance(spell, list): raise TypeError()


        self.__name = name
        self.__faculty = faculty
        self.__spell = spell or []
        self.__mana = con.PRIMALMANA


    def __str__(self):
        return f"Name: {self.__name}\nFaculty: {self.__faculty}\nMana: {self.__mana}\nspell: {self.__spell}"

    def __repr__(self):
        return f"{self.__name}"


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


    def try_cast_spell(self, target: HogwardStudent) -> bool:

        if not self.__spell:  return False

        random_spell = random.choice(self.__spell)

        new_mana = random_spell.get_mana()

        if self.__mana >= new_mana:
            self.__mana -= new_mana
            return True

        return False

    @staticmethod
    def copy_student(original):
        return HogwardStudent(original.__name, original.__faculty, original.__mana, original.__spell)


class Hogwarts:

    __students: list[HogwardStudent]
    __spells: list[Spell] = None


    def __init__(self, students: list[HogwardStudent] = None, spells: list[Spell] = None ) -> None:



        if not isinstance(students, list):  raise TypeError()
        if not isinstance(spells, list): raise TypeError()

        self.__students = students or []
        self.__spells = spells or []


    def __str__(self):
        return f"Students:{self.__students}\nSpells:{self.__spells}"

    def __repr__(self):
        return f"Students:{self.__students}\nSpells:{self.__spells}"


    def get_copy_spells(self) -> list[Spell]:

        copy_spells = []

        for spell in self.__spells:
            copy_spells.append(Spell.copy_spell(spell))

        return copy_spells

    def get_copy_students(self) -> list[HogwardStudent]:

        copy_students = []

        for student in self.__students:
            copy_students.append(HogwardStudent.copy_student(student))

        return copy_students



    def add_student(self, new_student: HogwardStudent) -> bool:

        if new_student not in self.__students:
            self.__students.append(new_student)
            return True
        return False

    def add_spell(self, new_spell: Spell) -> bool:

        if new_spell not in self.__spells:
            self.__spells.append(new_spell)
            return True

        return False

    def simulate_duell(self, student_1: HogwardStudent, student_2: HogwardStudent) -> bool:

        if student_1 not in self.__students or student_2 not in self.__students:  return False

        while student_1.get_mana() >= con.EXPELLIARMUS and student_2.get_mana() >= con.EXPELLIARMUS:

            student_1.try_cast_spell(student_2)

            if student_2.get_mana() > con.EXPELLIARMUS:
                student_2.try_cast_spell(student_1)

        if student_1.get_mana() > student_2.get_mana():
            print(f'win student_1 {student_1.get_mana()} ')

        elif student_2.get_mana() > student_1.get_mana():
            print(f'win student_2 {student_2.get_mana()} ')

        else:
            print(f"Draw")

        return True


s1 = Spell('хреновуха','сносит башку с чертям собачьим', 95 )

s2 = Spell('чертовуха', 'отрывает гениталии', 95)

s3 = Spell('ваще злобная штука', "высасвает мозг которого нет", 95)

c1 = HogwardStudent("Garri", "podlizerin", [s3])

c2 = HogwardStudent("Глебати", "podlizerin", [s2])

c3 = HogwardStudent("Germiona", "podlizerin", [s1])


h = Hogwarts([c1,c2, c3], [s1, s2, s3])

print(h)
print('='*20)


d = h.simulate_duell(c1, c2)
print(d)
print('='*20)

d2 = h.simulate_duell(c1, c3)
print(d2)
print('='*20)

d3 = h.simulate_duell(c2, c3)
print(d3)
print('='*20)
























































































