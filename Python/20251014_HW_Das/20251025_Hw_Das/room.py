# Вернуться к геомтрическим фигурам, комнатам и квартирам.
# Дополнить перечисленные классы свойствами.

class Room:
    def __init__(self, width, length, height=3):
        self.__width = width
        self.__length = length
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError()
        self.__width = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError()
        self.__length = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError()
        self.__height = value

    @property
    def area(self):
        return self.__width * self.__length

    @property
    def volume(self):
        return self.area * self.__height

    def __str__(self):
        return f'Room {self.width}x{self.length}, height {self.height}m, area {self.area}m², volume {self.volume}m³'


class Flat:
    def __init__(self, number, floor):
        self.__number = number
        self.__floor = floor
        self.__rooms = []

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError()
        self.__number = value

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError()
        self.__floor = value

    @property
    def rooms(self):
        return self.__rooms

    def add_room(self, room):
        if not isinstance(room, Room):
            raise TypeError()
        self.__rooms.append(room)

    @property
    def total_area(self):
        return sum(room.area for room in self.__rooms)

    def __str__(self):
        rooms_info = "\n".join(str(room) for room in self.__rooms)
        return f'Apartment {self.number} on floor {self.floor}\nTotal Area: {self.total_area}m²\nRooms:\n{rooms_info}'


room1 = Room(4, 3)
room2 = Room(5, 4)


room1.width = 5
room2.height = 2.7


flat = Flat(101, 5)
flat.add_room(room1)
flat.add_room(room2)


print(flat)

