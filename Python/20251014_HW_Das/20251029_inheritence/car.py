# Создать класс "машина", у неё приватные поля: марка, цвет, число колес, скорость. 
# Методы "ехать" (изменяет скорость машины), "остановиться" (обнуляет скорость), 
# Скорость должна быть свойством. Цвет - изменяемым свойством.


class Car:
    def __init__(self, brand, color, num_wheels):
        self.__brand = brand  
        self.__color = color  
        self.__num_wheels = num_wheels  
        self.__speed = 0  # Приватное поле: текущая скорость

    def drive(self, speed):
        """
        Устанавливает скорость машины.

        Args:
            speed (int): Новая скорость машины.
        """
        self.__speed = speed

    def stop(self):
        """
        Останавливает машину (обнуляет скорость).
        """
        self.__speed = 0

    @property
    def speed(self):
        """
        Свойство для получения текущей скорости машины.

        Returns:
            int: Текущая скорость машины.
        """
        return self.__speed

    @property
    def color(self):
        """
        Получить цвет машины
        """
        return self.__color

    @color.setter
    def color(self, new_color):
        """
        Установить новый цвет машины.
        """
        self.__color = new_color


# Пример использования класса
my_car = Car("Toyota", "Red", 4)
print(f"Цвет машины: {my_car.color}") #Вывод: Цвет машины: Red
my_car.color = "Blue"
print(f"Цвет машины: {my_car.color}") #Вывод: Цвет машины: Blue
my_car.drive(60)
print(f"Текущая скорость: {my_car.speed}") #Вывод: Текущая скорость: 60
my_car.stop()
print(f"Текущая скорость: {my_car.speed}") #Вывод: Текущая скорость: 0
