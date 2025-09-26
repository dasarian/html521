# Задание №8 (суббота, 27 сентября)
# Выбрать из списка чисел те, которые не делятся на семь и на 3
# lst = [7, 3, 13, 17, 14, 12, 21, 45, 77, 23, 16]
# ответ должен быть: [13, 17, 23, 16]


lst = [7, 3, 13, 17, 14, 12, 21, 45, 77, 23, 16]
divisible_numbers = []

for num in lst:
    if num % 7 != 0 and num % 3 != 0:
        divisible_numbers.append(num)

print(divisible_numbers)