# Сделать сеттеры и геттеры для имени и оценок

class Student:
    def __init__(self, name):
        self.__name = name
        self.__marks = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError()
        self.__name = name

    def get_marks(self):
        return self.__marks.copy()  

    def set_marks(self, marks):
        if not isinstance(marks, list):
            raise TypeError()
        self.__marks = marks.copy()  

    def add_mark(self, mark):
        if not isinstance(mark, (int, float)) or mark < 0 or mark > 12:
            raise ValueError()
        self.__marks.append(mark)

    def average_mark(self):
        if not self.__marks:
            return 0.0
        return sum(self.__marks) / len(self.__marks)

    def __str__(self):
        return f"student: {self.__name}, average grade: {self.average_mark():.1f}"


student = Student("Иван")
print(student)  

student.set_name("Иван Иванов")
student.add_mark(10)
student.add_mark(11)
student.add_mark(9)

print(student)  
print(student.get_marks())  

student.set_marks([12, 11, 10])
print(student.get_marks())  
print(student)  


