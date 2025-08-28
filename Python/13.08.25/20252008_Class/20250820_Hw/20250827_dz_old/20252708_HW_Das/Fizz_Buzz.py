start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    print("Ошибка: начало диапазона должно быть меньше или равно концу.")
else:
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
