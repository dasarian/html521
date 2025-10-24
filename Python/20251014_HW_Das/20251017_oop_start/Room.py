# Дополнить класс "комната" функцией, 
# считающей площадь её стен (без учета окон и дверей).

class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def area(self):
        return self.width * self.length

    def wall_area(self):
        return 2 * (self.width + self.length) * self.height





