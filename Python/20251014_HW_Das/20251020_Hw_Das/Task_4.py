# Дополнить класс "комната" функцией, считающей площадь её стен (без учета окон и дверей).
# Дополнить класс "квартира" такой же функцией.
class Room:
    def __init__(self, length, width, height, windows_area=0, doors_area=0):
        self.length = length
        self.width = width
        self.height = height
        self.windows_area = windows_area
        self.doors_area = doors_area

    def walls_area(self):
        total_walls = 2 * self.height * (self.length + self.width)
        clean_walls = total_walls - (self.windows_area + self.doors_area)
        return clean_walls

class Apartment:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def walls_area(self):
        total_area = 0
        for room in self.rooms:
            total_area += room.walls_area()
        return total_area


room1 = Room(length=5, width=4, height=3, windows_area=2, doors_area=1)
room2 = Room(length=6, width=3, height=3, windows_area=1.5, doors_area=1)

apartment = Apartment()
apartment.add_room(room1)
apartment.add_room(room2)

print("Room 1 wall area:", room1.walls_area())
print("Room 2 wall area:", room2.walls_area())
print("Total apartment wall area:", apartment.walls_area())
