# Создать список чисел от 1 до 10 

import random
numbers = [random.randint(1, 10) for _ in range(7)]
print("Список чисел:", numbers)


# 1.1 Написать программу, которая проверяет, есть ли число в списке

user_number = int(input("Введите число для поиска: "))
if user_number in numbers:
    print(f"Число {user_number} найдено в списке.")
else:
    print(f"Число {user_number} не найдено в списке.")


# 1.2 Написать функцию, которая возвращает номер позиции, если число найдено и None, если не найдено


def find_position(number_list, target):
    position = 0
    while position < len(number_list):
        if number_list[position] == target:
            return position
        position += 1
    return None

# функцию

position = find_position(numbers, user_number)
if position is not None:
    print(f"Число {user_number} найдено на позиции {position}.")
else:
    print(f"Число {user_number} не найдено в списке.")




