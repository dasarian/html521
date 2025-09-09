for i in range(10):
     print(i, end=' ')


start = int(input("Enter starting number : ") or 6)
end = int(input("Enter ending number : ") or 18)

for i in range(start, end):
    print(i, end=' ')

# 1. вывести все двузначные числа с нулем на конце
# 2. вывести все трехзначные числа, которые делятся на 13
# 3. вывести в обратном порядке все числа меньше тысячи, которые делятся на 13, но не делятся на 14

# 1.
for i in range(10, 100, 10):
    print(i, end=' ')

# 2. 
for i in range(100, 1000):
    if i % 13 == 0:
        print(i, end=' ')

#3. 
for i in range(999, 0, -1):
    if i % 13 == 0 and i % 14 != 0:
        print(i, end=' ')