def get_birth_year():
    while True:
        year = input('Введите год рождения: ')
        try:
            year = int(year)
            return year
        except ValueError:
            print('Некорректный ввод. Пожалуйста, введите числовой год.')

birth_year = get_birth_year()
print(f'Ваш год рождения: {birth_year}')