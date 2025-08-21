vacation_database = {
    "Иван": 14,
    "Мария": 10,
    "Алексей": 7,
    "Ольга": 21,
}

name = input("Введите ваше имя: ")

if name in vacation_database:
    days = vacation_database[name]
    print(f"{name}, вы взяли {days} дней отпуска.")

