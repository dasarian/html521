def process_numbers():
    numbers_str = input("Введите числа через пробел: ")
    numbers = [int(num) for num in numbers_str.split()]
    iterator = iter(numbers)
    total = 0

    while True:
        try:
            num = next(iterator)
            print(num)
            total += num
        except StopIteration:
            print(f"Все числа выведены. Сумма: {total}")
            break

process_numbers()