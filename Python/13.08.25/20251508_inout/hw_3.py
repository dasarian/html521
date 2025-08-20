from datetime import datetime, timedelta

def calculate_vacation():
    start_date_str = input("Введите дату поступления на работу (ДД.ММ.ГГГГ): ")
    initial_salary = float(input("Введите начальную зарплату: "))
    current_date = datetime.now()
    
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    
    months_worked = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
    
    current_salary = initial_salary + 100 * months_worked
    
    days_worked = (current_date - start_date).days
    weeks_worked = days_worked // 7
    
    vacation_days = weeks_worked // 2
    
    vacation_pay = current_salary * vacation_days
    
    print(f"\nКоличество накопленных дней отпуска: {vacation_days}")
    print(f"Сумма отпускных: {vacation_pay:.2f} руб.")
    print(f"Текущая зарплата: {current_salary:.2f} руб.")
    print(f"Отработано месяцев: {months_worked}")

calculate_vacation()