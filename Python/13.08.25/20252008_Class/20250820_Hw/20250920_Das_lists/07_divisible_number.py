lst = [7, 3, 13, 17, 14, 12, 21, 45, 77, 23, 16]
divisible_numbers = []

for num in lst:
    if num % 7 != 0 and num % 3 != 0:
        divisible_numbers.append(num)

print(divisible_numbers)