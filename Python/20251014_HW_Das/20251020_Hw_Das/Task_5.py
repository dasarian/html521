# Рассчитать стоимость обоев, 
# если задать ширину, длину и стоимость рулона (тоже класс) и 
# количество рулонов должно быть строго целым.

class WallpaperRoll:
    def __init__(self, width, length, price_per_roll):
        self.width = width  
        self.length = length  
        self.price_per_roll = price_per_roll  

class Room:
    def __init__(self, length, width, height, num_windows=0, window_area=0, num_doors=0, door_area=0):
        self.length = length  
        self.width = width  
        self.height = height  
        self.num_windows = num_windows  
        self.window_area = window_area  
        self.num_doors = num_doors  
        self.door_area = door_area  

    def wall_area(self):
        perimeter = 2 * (self.length + self.width)
        total_wall_area = perimeter * self.height
        total_window_area = self.num_windows * self.window_area
        total_door_area = self.num_doors * self.door_area
        return total_wall_area - total_window_area - total_door_area

class Apartment:
    def __init__(self, rooms):
        self.rooms = rooms  

    def total_wall_area(self):
        total_area = 0
        for room in self.rooms:
            total_area += room.wall_area()
        return total_area

def calculate_wallpaper_cost(apartment, wallpaper_roll):
    total_area = apartment.total_wall_area()
    roll_area = wallpaper_roll.width * wallpaper_roll.length
    num_rolls = int(total_area // roll_area)
    if total_area % roll_area != 0:
        num_rolls += 1

    total_cost = num_rolls * wallpaper_roll.price_per_roll
    return num_rolls, total_cost


room1 = Room(length=5, width=4, height=3, num_windows=2, window_area=1.5, num_doors=1, door_area=2)
room2 = Room(length=4, width=3, height=3, num_windows=1, window_area=1.5, num_doors=1, door_area=2)

apartment = Apartment(rooms=[room1, room2])

wallpaper_roll = WallpaperRoll(width=0.53, length=10, price_per_roll=20)
num_rolls, total_cost = calculate_wallpaper_cost(apartment, wallpaper_roll)

print(f"Number of rolls needed: {num_rolls}")
print(f"Total cost: {total_cost}")
