# 3. Создать список из чисел, оканчивающихся на 7

numbers = range(100)
seven_ending_numbers = []
for num in numbers:
    if num % 10 == 7:
        seven_ending_numbers.append(num)
print(seven_ending_numbers)
