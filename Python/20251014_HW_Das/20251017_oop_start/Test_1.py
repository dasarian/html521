# Написать свойства для человека и для студента.
# Для студента создать свойство для среднего, а человеку - для возраста, 
# не создавая отдельных полей для хранения!

from datetime import datetime

class Human:
    def __init__(self, name, birthday):
        self.__name = name
        self.birthday = birthday  

    @property
    def name(self):   #Геттер для name
        return self.__name

    @name.setter
    def name(self, new_name):  #Сеттер для name
        if not isinstance(new_name, str):
            raise TypeError()
        self.__name = new_name

    @property
    def birthday(self):  #Геттер для HBD
        return self.__birthday

    @birthday.setter
    def birthday(self, new_bd):   # Сеттер для DOB
        if not isinstance(new_bd, datetime):
            raise TypeError()
        if new_bd > datetime.now():
            raise ValueError()
        self.__birthday = new_bd

    @property
    def age(self):
        today = datetime.now()
        years = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            years -= 1
        return years

class Student:
    def __init__(self, name, birthday):
        self.__human = Human(name, birthday)  
        self.__marks = []  

    @property
    def name(self):
        return self.__human.name

    @name.setter
    def name(self, new_name):
        self.__human.name = new_name

    @property
    def birthday(self):
        return self.__human.birthday

    @birthday.setter
    def birthday(self, new_bd):
        self.__human.birthday = new_bd

    @property
    def age(self):
        return self.__human.age

    @property
    def marks(self):
        return self.__marks [:]

    def add_mark(self, mark):
        if not isinstance(mark, (int, float)) or mark < 0 or mark > 12:
            raise ValueError()
        self.__marks.append(mark)

    @property
    def average_mark(self):
        if not self.__marks:
            return 0.0
        return sum(self.__marks) / len(self.__marks)


human = Human('Иван', datetime(1990, 5, 15))
print(f"Name: {human.name}, Age: {human.age}")  


student = Student('Мария', datetime(2000, 8, 20))
student.add_mark(10)
student.add_mark(11)
student.add_mark(9)

print(f"Name: {student.name}, Age: {student.age}, Average Grade: {student.average_mark:.1f}")
