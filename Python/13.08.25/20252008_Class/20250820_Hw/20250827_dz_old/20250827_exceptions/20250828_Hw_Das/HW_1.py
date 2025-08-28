from datetime import datetime
try:
    age = int(input("Введите ваш возраст: "))
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным.")

    current_year = datetime.now().year
    birth_year = current_year - age

    print(f"Ваш год рождения: {birth_year}")
except ValueError as e:
    print(f"Ошибка: {e}")
