# (показывает преподаватель) 
# Написать класс "комната", у которой есть 
# ширина, длина, высота. Комната должна уметь считать 
# "свою" площадь.
# (показывает преподаватель) 
# Написать класс квартира с массивом комнат, 
# номером (квартиры) и этажом. 
# Квартира должна уметь считать "свою" площадь, 
# используя умения своих комнат.

class Room:

    def __init__(self, width, length, height=3):
        self.width = width
        self.length = length
        self.height = height

    def ploshad(self):
        return self.width * self.length
    
my_room = Room(4, 4)
print('Площадь комнаты: ', my_room.ploshad())

# Написать класс квартира с массивом комнат,
class Flat:

    def __init__(self, number, etage):
        self.rooms = [
            Room(1,  2),  # toilet
            Room(5, 10),  # salon
            Room(2,  3),  # hall,
            Room(2,  2),  # bathroom
            Room(4,  4),  # bedroom
            Room(3,  3)   # kitchen
        ]
        # номером (квартиры) и этажом. 
        self.number = number
        self.etage  = etage
    
    def ploshad(self):
        result = 0
        # Пусть площадь квартиры состоит из суммы площадей всех её комнат
        # НЕПРАВИЛЬНОЕ РЕШЕНИЕ
        for r in self.rooms:
            result += r.width * r.length
        # НУ, ПОЧЕМУ, ВЕДЬ ОТВЕТ ПРАВИЛЬНЫЙ?
        # Потому что мы ВЛЕЗЛИ ВНУТРЬ объекта, а надо заставить его работать!
        
        # Правильное решение:
        result = 0
        for r in self.rooms:
            # !!!!!! используя умения своих комнат.
            result += r.ploshad()  # мы заставили комнату саму посчитать и вернуть свою площадь
        return result

one_flat = Flat(1, 1)
print(one_flat.ploshad())