from datetime import datetime

class Human:
    def __init__(self, name, birth_day):
        self.__name = name
        self.__birthday = birth_day
        #self.set_BD(birthday)

    @property
    def birthday(self):
        return self.__birthday

    # Напишем медот изменения даты рождения:
    @birthday.setter
    def birthday(self, new_bd):
        if not isinstance(new_bd, datetime):
            raise TypeError(
                'Новая дата рождения должна быть типа datetime, Вы передали: ' + str(type(
                    new_bd)))
        if new_bd > datetime.now():
            raise ValueError(
                'Новая дата рождения превышает текущую, ' + str(new_bd))
        self.__birthday = new_bd

h = Human('Wera', datetime(1986, 8, 6))
print(h.birthday)  # обращаюсь к методу, а скобки - не ставлю! Потому что property
h.birthday = 'mew'

# Выдаст нашу ошибку: неверный тип
# h.set_BD('Лучший день на свете')

# Выдаст нашу ошибку: неверное значение - превышает текущее
# h.set_BD(datetime(2567, 6, 3))

