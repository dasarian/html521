# Создать класс Студент
# Ваш класс студент должен содержать массив оценок.
# Магический метод "добавить" принимает на вход оценку и вписывает её в массив
# Магический метод "напечатать" печатает студента в виде: "Вася, средний балл 10.3"

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def __add__(self, grade):
        self.grades.append(grade)
        return self  

    def average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name}, средний балл {self.average_grade():.1f}"


student = Student("Вася")
student + 10
student + 11
student + 10

print(student)  

