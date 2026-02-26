#3.4

#1
class Student:

    __name: str
    __surname: str
    __age: int
    __gpa: float


    def __init__(self, name: str, surname: str, age: int, gpa: float):

        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gpa = gpa


    def __str__(self):
        return f'Name: {self.__name}\nSurname: {self.__surname}\nAge: {self.__age}\nGPA: {self.__gpa}'

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa: float) -> float | None:

        if gpa < 0 or gpa > 100:  return None

        self.__gpa = gpa

        return gpa

    gpa = property(get_gpa, set_gpa)

    def __eq__(self, other):
        return self.__gpa == other.__gpa

    def __ne__(self, other):
        return self.__gpa != other.__gpa

    def __lt__(self, other):
        return self.__gpa < other.__gpa

    def __gt__(self, other):
        return self.__gpa > other.__gpa

    def __le__(self, other):
        return self.__gpa <= other.__gpa

    def __ge__(self, other):
        return self.__gpa >= other.__gpa


student = Student('James', 'Smith', 42, 42)
print(student)
print('='*20)

print(student.get_name())
print('='*20)
print(student.get_surname())
print('='*20)
print(student.get_age())
print('='*20)
print(student.get_gpa())
print('='*20)

student_2 = Student('Bob', 'Terminator', 300, 99)



student_2.gpa = 85
print(student_2)
print('='*20)
print(student_2.get_gpa())
print('='*20)


print(student > student_2)
print('='*20)
print(student >= student_2)
print('='*20)





