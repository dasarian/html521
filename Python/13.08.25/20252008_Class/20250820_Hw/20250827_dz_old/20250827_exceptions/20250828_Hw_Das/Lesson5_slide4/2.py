count = 0
while True:
    try:
        x = int(input("Введите целое число (или 0 для выхода): "))
        if x == 0:
            break
        print(f"Обратное число: {1/x}")
        count += 1
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        break
    except ValueError:
        print("Ошибка: введите целое число")

print(f"Расчёт окончен. Количество введённых чисел: {count}")