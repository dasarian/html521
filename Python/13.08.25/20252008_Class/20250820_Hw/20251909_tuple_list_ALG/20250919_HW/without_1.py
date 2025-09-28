# 4. Создать список чисел, в состав которых не входит единичка

numbers = range(101)
numbers_without_1 = []
for num in numbers:
    if '1' not in str(num):
        numbers_without_1.append(num)
print(numbers_without_1)
