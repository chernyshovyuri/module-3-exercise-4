from __future__ import annotations
import constants as con
import random


class Spell:

    __name: str
    __effect: str
    __potrency: int

    def __init__(self, name: str, effect: str, potrency: int = con.MANANONE):

        if not isinstance(name, str):  raise TypeError()
        if not isinstance(effect, str): raise TypeError()
        if not isinstance(potrency, (int, float)): raise TypeError()

        self.__name = name
        self.__effect = effect
        self.__potrency = potrency


    def __str__(self):
        return f'Name:{self.__name}\nEffect:{self.__effect}\nMana:{self.__potrency}'

    def __repr__(self):
        return f"{self.__name}"

    def get_name(self):

        return self.__name

    def get_effect(self):

        return self.__effect

    def get_potrency(self):

        return self.__potrency

    def set_potrency(self, new_mana: int) -> bool:

        if new_mana < 0 or new_mana > con.PRIMALMANA:  return False

        self.__potrency = new_mana

        return True


    @staticmethod
    def copy_spell(original):
        return Spell(original.__name, original.__effect, original.__potrency)



class HogwardStudent:

    __name: str
    __faculty: str
    __mana_student: int
    __spell: list[Spell]


    def __init__(self, name: str, faculty: str, spell: list[Spell] = None, mana_student: int = 100):

        if not isinstance(name, str): raise TypeError()
        if not isinstance(faculty, str): raise TypeError()
        if not isinstance(spell, list): raise TypeError()
        if not isinstance(mana_student, int): raise TypeError()


        self.__name = name
        self.__faculty = faculty
        self.__spell = spell or []
        self.__mana_student = mana_student


    def __str__(self):
        return f"Name: {self.__name}\nFaculty: {self.__faculty}\nMana Student: {self.__mana_student}\nspell: {self.__spell}"

    def __repr__(self):
        return f"{self.__name}"


    def get_name(self):
        return self.__name

    def get_faculty(self):
        return self.__faculty

    def get_mana(self):
        return self.__mana_student

    def get_spell(self):
        return self.__spell


    def set_mana(self, new_mana: int) -> bool:

        if new_mana < 0 or new_mana > con.PRIMALMANA:  return False

        self.__mana_student = new_mana

        return True


    def cast_spell(self, target: HogwardStudent) -> bool:

        if not self.__spell:  return False

        random_spell = random.choice(self.__spell)

        new_mana = random_spell.get_potrency()

        if  self.__mana_student >= new_mana:
            self.__mana_student -= new_mana
            return True

        return False


    @staticmethod
    def copy_student(original):
        return HogwardStudent(original.__name, original.__faculty, original.__ana_student, original.__spell)


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

    def try_simulate_duell(self, student_1: HogwardStudent, student_2: HogwardStudent) -> bool:

        if student_1 not in self.__students or student_2 not in self.__students:  return False

        if student_1.get_mana() < con.EXPELLIARMUS or student_2.get_mana() < con.EXPELLIARMUS:
            print(f'Не хватает маныЖ Студент1:{student_1.get_mana()}\nСтудент2:{student_2.get_mana()}')
            return False

        while student_1.get_mana() >= con.EXPELLIARMUS and student_2.get_mana() >= con.EXPELLIARMUS:

            student_1.cast_spell(student_2)

            if student_2.get_mana() > con.EXPELLIARMUS:
                student_2.cast_spell(student_1)

        if student_1.get_mana() > student_2.get_mana():
            print(f'win student_1 {student_1.get_mana()} ')

        elif student_2.get_mana() > student_1.get_mana():
            print(f'win student_2 {student_2.get_mana()} ')

        else:
            print(f"Draw")

        return True


expelliarmus = Spell('expelliarmus', 'лишает всех волов на теле и одежды', 15)
stupefy = Spell('stupefy', 'удар пустым мешком по голове', 30)
protego = Spell('protego', 'защита от заклинания посредством показа среднего пальца руки противнику', 20)
avada_kedavra = Spell('avada_kedavrf', 'словестное унижение апонента, болинг, пока не расплачеться', 80)

print(expelliarmus)
print('='*20)
print(stupefy)
print('='*20)
print(protego)
print('='*20)
print(avada_kedavra)
print('='*20)


garri_potniy = HogwardStudent('garri potni', 'облизарин', [expelliarmus, stupefy, protego, avada_kedavra], 100)
germiona = HogwardStudent("germiona", 'самвшокемизарин', [expelliarmus, stupefy, protego, avada_kedavra], 100)
grizli = HogwardStudent('grizli', 'нифигасеблизарин', [expelliarmus, stupefy, protego, avada_kedavra], 100)

print(garri_potniy)
print('='*20)
print(germiona)
print('='*20)
print(grizli)
print('='*20)




h = Hogwarts([garri_potniy, germiona, grizli], [expelliarmus, stupefy, protego, avada_kedavra])


d1 = h.try_simulate_duell(garri_potniy, germiona)
print(d1)
print('='*20)

d2 = h.try_simulate_duell(grizli, germiona)
print(d2)
print('='*20)

d3 = h.try_simulate_duell(garri_potniy, grizli)
print(d3)
print('='*20)


























































































