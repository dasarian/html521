# 1. С помощью range вывести все нечётные числа от 77 до 777 включительно
for i in range(77, 778, 2):
    print(i, end=' ')



# 2. А теперь - используя переменные
start_number = 77
end_number = 777

for number in range(start_number, end_number + 1, 2):
    print(number, end=' ')



# 3. А теперь, получив диапазон от пользователя
start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

if start % 2 == 0:
    start += 1  

print(f"Нечётные числа от {start} до {end}:")
for number in range(start, end + 1, 2):
    print(number, end=' ')

