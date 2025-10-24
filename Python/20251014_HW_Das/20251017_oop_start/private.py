from datetime import datetime

class Human:
    def __init__(self, name, birthday):
        self.__name = name
        # self.__birthday = birthday
        self.set_BD(birthday)

    def get_BD(self):
        return self.__birthday

    # Напишем медот изменения даты рождения:
    def set_BD(self, new_bd):
        if not isinstance(new_bd, datetime):
            raise TypeError(
                'Новая дата рождения должна быть типа datetime, Вы передали: ' + str(type(
                    new_bd)))
        if new_bd > datetime.now():
            raise ValueError(
                'Новая дата рождения превышает текущую, ' + str(new_bd))
        self.__birthday = new_bd

h = Human('Wera', datetime(1986, 8, 6))
# Приватность - ненастоящая!
# print(h._Human__name)
# Ошибка: приватное поле
# print(h.__name)

# Выдаст нашу ошибку: неверный тип
# h.set_BD('Лучший день на свете')

# Выдаст нашу ошибку: неверное значение - превышает текущее
# h.set_BD(datetime(2567, 6, 3))

def get_name(self):
        return self.__name

def set_name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError(
                f'Name must be of type `str`, got: {type(new_name)}'
            )
        self.__name = new_name

def __str__(self):
        return f"Human(name={self.__name}, birthday={self.__birthday.strftime('%Y-%m-%d')})"

h.set_BD(datetime(1986, 8, 6))
print(h.get_BD())

