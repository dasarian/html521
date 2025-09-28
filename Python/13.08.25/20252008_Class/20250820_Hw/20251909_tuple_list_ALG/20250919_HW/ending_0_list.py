# 1. Создать список из чисел, оканчивающихся нулем максимальным количеством способов (хотя бы три)

# 1. 
numbers = list(range(101))
zero_ending_numbers = [num for num in numbers if num % 10 == 0]
print(zero_ending_numbers)

# 2. 
numbers = list(range(101))
zero_ending_numbers = []
for num in numbers:
    if num % 10 == 0:
        zero_ending_numbers.append(num)
print(zero_ending_numbers)


# 3. 
numbers = list(range(101))
zero_ending_numbers = [num for num in numbers if str(num)[-1] == '0']
print(zero_ending_numbers)


