def process_list(lst):
    iterator = iter(lst)
    first = next(iterator)
    squares = [str(i**2) for i in range(1, first + 1)]
    print("Квадраты чисел от 1 до", first, ": ", ", ".join(squares))

    # Обработка второго элемента: заполненный квадрат из звёздочек
    second = next(iterator)
    for _ in range(second):
        print('*' * second)

    # Обработка третьего элемента: числа, которые не делятся на 2, 3, 5
    third = next(iterator)
    result = [num for num in range(1, third + 1) if num % 2 != 0 and num % 3 != 0 and num % 5 != 0]
    print(f"Числа от 1 до {third}, не делящиеся на 2, 3, 5: {result}")

    # Обработка четвёртого элемента: список строк, каждая вдвое длиннее
    fourth = next(iterator)
    strings = []
    current = str(fourth)
    for _ in range(fourth):
        strings.append(current)
        current += current
    print(f"Список строк для {fourth}: {strings}")

    # Обработка пятого элемента: пустой треугольник
    fifth = next(iterator)
    for i in range(1, fifth + 1):
        spaces = ' ' * (fifth - i)
        if i == fifth:
            stars = '*' * (2 * i - 1)
        else:
            stars = '*' + ' ' * (2 * (i - 1) - 1) + '*' if i > 1 else '*'
        print(spaces + stars)

# Пример использования
lst = [8, 3, 23, 5, 5]
process_list(lst)
