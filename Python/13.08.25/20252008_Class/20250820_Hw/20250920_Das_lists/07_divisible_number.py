lst = [7, 3, 13, 17, 14, 12, 21, 45, 77, 23, 16]
divisible_numbers = []

for x in lst:
    if x % 7 != 0 and x % 3 != 0:
        divisible_numbers.append(x)

print(divisible_numbers)