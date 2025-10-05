def squares(num):
    return [str(i**2) for i in range(1, num + 1)]

# Объявляем список
lst = [8, 3, 23, 5, 5]
# Создаем итератор
iterator = iter(lst)
# Берем первый элемент...
first = next(iterator)
print("Квадраты чисел от 1 до", first, ": ", ", ".join(squares(first)))

print()

def squares(num):
    return [str(i**2) for i in range(1, num + 1)]

def filled_square(size):
    result = ''
    for _ in range(size):
        result += '*' * size + '\n'
    return result

# Объявляем список
lst = [8, 3, 23, 5, 5]
# Создаем итератор
iterator = iter(lst)
# Берем первый элемент...
first = next(iterator)
print("Квадраты чисел от 1 до", first, ": ", ", ".join(squares(first)))
second = next(iterator)
print(filled_square(second))

print()


max_num = 23
def print_non_divisible_numbers(max_num):
    iterator = iter(range(1, max_num + 1))

    try:
        while True:
            num = next(iterator)
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                print(num)
    except StopIteration:
        pass  
print_non_divisible_numbers(max_num) 

print ()

# 4. 
initial_str = '8'
length = 5 
def generate_doubling_strings(initial_str, length):
    strings = []
    current_str = initial_str
    strings_iterator = iter(range(length))

    try:
        while True:
            next(strings_iterator)  
            strings.append(current_str)
            current_str += current_str  
    except StopIteration:
        pass

    return strings 
result = generate_doubling_strings(initial_str, length)
print(result)

print ()
