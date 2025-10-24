# Надо реализовать у комнаты метод _ _ sub _ _
# он должен получать на вход комнату и проверять, можно ли такой "кусок" отрезать по прямой, перпендикулярной одной из стен? Т.е. из комнаты нельзя вырезать уголок - у нас пока что нет способа описывать комнату фигурной формы

# Потом реализовать метод sub для квартиры: он должен подбирать подходящую по размеру комнату (любую)

class Room:
    def __init__(self, width, length, height=3):
        self.width = width
        self.length = length
        self.height = height

    def ploshad(self):
        return self.width * self.length
    
    def __str__(self):
        return 'Комната %ix%i, высотой %iм\nПлощадь %i' % (
            self.width, self.length, self.height, self.ploshad()
        )
    
    def __add__(self, other):
        if self.width == other.width:
            return Room(self.width, self.length + other.length)
        if self.width == other.length:
            return Room(self.width, self.length + other.width)
        if self.length == other.length:
            return Room(self.width + other.width, self.length)
        if self.length == other.width:
            return Room(self.width + other.length, self.length)
        raise ValueError()

    def __sub__(self, other):
        if not isinstance(other, Room):
            raise ValueError()
        if (other.width <= self.width and other.length <= self.length):
            new_width = self.width - other.width
            new_length = self.length
            if new_width >= 0:
                return Room(new_width, new_length, self.height)
        if (other.length <= self.width and other.width <= self.length):
            new_width = self.width
            new_length = self.length - other.width  
            if new_length >= 0:
                return Room(new_width, new_length, self.height)
        
        raise ValueError()

class Flat:
    def __init__(self, number, etage):
        self.rooms = [
            Room(1, 2),   # toilet
            Room(5, 10),  # salon
            Room(2, 3),   # hall
            Room(2, 2),   # bathroom
            Room(4, 4),   # bedroom
            Room(3, 3)    # kitchen
        ]
        self.number = number
        self.etage = etage
    
    def ploshad(self):
        result = 0
        for r in self.rooms:
            result += r.ploshad()  
        return result

    def __sub__(self, other):
        if not isinstance(other, Room):
            raise ValueError()
        
        for i, room in enumerate(self.rooms):
            try:
                new_room = room - other  
                new_rooms = self.rooms.copy()
                new_rooms[i] = new_room
                return Flat(self.number, self.etage)
            except ValueError:
                continue  
        raise ValueError()


my_room = Room(4, 3)
print('Площадь комнаты: ', my_room.ploshad())
print('Так печатается комната: \n', my_room, sep='')

your_room = Room(5, 4)
print(my_room + your_room)  

room_to_cut = Room(2, 1)  
new_room = my_room - room_to_cut
print('Новая комната после отрезания:\n', new_room, sep='')


one_flat = Flat(1, 1)
print('Площадь квартиры: ', one_flat.ploshad())
print('Попытка отрезать комнату из квартиры:')
new_flat = one_flat - room_to_cut
print('Площадь новой квартиры: ', new_flat.ploshad())