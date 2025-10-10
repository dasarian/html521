def range_with_step(start, end, step):
    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step

if __name__ == "__main__":
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    step = int(input("Введите шаг: "))

    for number in range_with_step(start, end, step):
        print(number)
