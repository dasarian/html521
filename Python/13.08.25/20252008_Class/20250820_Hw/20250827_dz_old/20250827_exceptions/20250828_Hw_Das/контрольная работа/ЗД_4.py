from datetime import datetime
name = input("Введите ваше имя: ")
birth_year = int(input("Введите ваш год рождения: "))
current_year = datetime.now().year
age = current_year - birth_year

if age < 10:
    print(f"Привет, {name}!")
elif 10 <= age <= 20:
    print(f"Здравствуйте, {name}!")
else:
    print(f"Не подскажете, как вас по отчеству, {name}?")
