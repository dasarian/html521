count = 0
while True:
    try:
        x = float(input("Введите вещественное число (или 0 для выхода): "))
        if x == 0:
            break
        print(1 / x)
        count += 1
    except ValueError:
        print("Ошибка: введено не вещественное число.")
        break
print(f"Расчёт окончен. Введено чисел: {count}")