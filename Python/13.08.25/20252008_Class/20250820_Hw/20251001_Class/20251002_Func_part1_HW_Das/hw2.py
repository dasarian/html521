# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.

def print_even_numbers_between(start, end):
    if start > end:
        start, end = end, start  

    for number in range(start, end + 1):
        if number % 2 == 0:  
            print(number)

print_even_numbers_between(3, 10)
