# создание видимости обычного присваивания или чтения,
# которые на самом деле подменяются функциями getter, setter(accessor, mutator), 
# которые позволяют контролировать чтение или присваивание

# Дополните класс human двумя свойствами:
# name, birthday

from datetime import datetime

class Human:
    def __init__(self, name, birthday):
        self.__name = name
        self.birthday = birthday  

    def name(self):
        return self.__name

    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError()
        self.__name = new_name

    def birthday(self):
        return self.__birthday

    def birthday(self, new_bd):
        if not isinstance(new_bd, datetime):
            raise TypeError()
        if new_bd > datetime.now():
            raise ValueError()
        self.__birthday = new_bd


h = Human('Вера', datetime(1986, 8, 6))
print(h.name)  
print(h.birthday)  


h.name = 'Вера Ивановна'
print(h.name)  

h.birthday = datetime(1985, 7, 5)
print(h.birthday)  

try:
    h.birthday = datetime(2567, 6, 3)
except ValueError as e:
    print(f"Ошибка: {e}")  

try:
    h.name = 123
except TypeError as e:
    print(f"Ошибка: {e}")  

