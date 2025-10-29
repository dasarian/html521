from datetime import datetime

class Human:
   
    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

    @property
    def age(self):
        return (datetime.now()- self.__birthday).days // 365
    
h = Human('вася', datetime(1970, 1, 1))
print(h.age)
class student(Human):
    pass

s = student('Слава', datetime(1986, 2, 5))
print(s.age)
