def get_apple_price():
    while True:
        try:
            price = float(input('Сколько стоит килограмм яблок? '))
            if price <= 0:
                raise ValueError('Цена должна быть больше нуля.')
            if price > 1000:
                print('Мне дорого')
            elif 100 <= price <= 1000:
                print('Мне 1 килограмм')
            else:
                print('Мне 5 кг')
            break
        except ValueError:
            print('Пожалуйста, введите корректное число.')

get_apple_price()