from datetime import datetime

def calculate_transport_fare():
    current_year = datetime.now().year
    
    birth_year = int(input("Введите год вашего рождения: "))
    tariff = input("Выберите тариф ('час', 'неделя', 'месяц', 'год'): ").lower()
    
    age = current_year - birth_year
    
    tariffs = {
        'час': 60,
        'неделя': 300,
        'месяц': 1000,
        'год': 20000
    }
    
    if tariff not in tariffs:
        print("Ошибка: выбран неверный тариф")
        return
    
    if age > 50 or age < 14:
        price = 0
        discount = "100% (бесплатно)"
    elif 14 <= age <= 24:
        price = tariffs[tariff] * 0.5
        discount = "50%"
    else:
        price = tariffs[tariff]
        discount = "0% (полная стоимость)"
    
    print(f"\nВозраст: {age} лет")
    print(f"Тариф: {tariff}")
    print(f"Льгота: {discount}")
    print(f"Стоимость проездного: {price:.2f} руб.")

calculate_transport_fare()