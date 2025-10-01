# Опциональные аргументы
# Передача аргументов по позиции и по имени

# Опциональные аргументы - аргументы, для которых есть значение 
# по умолчанию, которое можно использовать

# Задача: посчитать остаток на счету. 
# По умолчанию начальная сумма будет равна нулю, 
# но будет возможность указать начальную сумму

def sum_rest(difference, start_sum=0):
    return start_sum + difference

# Работа функции. Обычный вариант: передаем оба параметра
print(sum_rest(-20, 100))

# Вызов с одним параметром - второй параметр будет передан по умолчанию - 0
print(sum_rest(40))

# Задание: Доставка пиццы (вернуть строку). 
# Параметры адреса: улица, дом, квартира. 
# Если пользователь не указал квартиру, появляется строка: до подъезда 
# Если пользователь указал город, он появляется перед адресом, иначе - Москва
# до 20:40

def pizza_delivery(street, house, apartment=None, city=None):
    delivery_city = city if city else "Москва"
    apartment_str = f", кв. {apartment}" if apartment else " до подъезда"
    address = f"{delivery_city}, ул. {street}, д. {house}{apartment_str}"
    return f"Доставка по адресу: {address}"

print(pizza_delivery("Ленина", 10, 5, "Санкт-Петербург"))
print(pizza_delivery("Ленина", 10, 5))
print(pizza_delivery("Ленина", 10))
print(pizza_delivery("Ленина", 10, city="Казань"))


def pizza(street, building, flat_number='до подъезда', city='Москва'):
    return f'Город: {city}, Дом: {building}, Улица: {street}, {flat_number}'

print(pizza(street='Махровая', building=7, flat_number=199, city='Зелепук'))
print(pizza(street='Махровая', building=7))
print(pizza('Махровая', 7))
