def iterate_range():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    step = int(input("Введите шаг: "))

    if step == 0:
        print("Шаг не может быть равен нулю.")
        return

    iterator = iter(range(start, end, step))
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("Диапазон завершён")
            break
iterate_range()

