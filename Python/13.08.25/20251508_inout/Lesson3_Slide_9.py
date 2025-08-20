from datetime import datetime, timedelta

def calculate_vacation_stats():
    start_date_str = input("Введите дату начала работы (в формате ДД.ММ.ГГГГ): ")
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    current_date = datetime.now()
    
    initial_salary = float(input("Введите начальную зарплату: "))
    
    work_duration = current_date - start_date
    
    full_months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
    
    if current_date.day < start_date.day:
        full_months -= 1
    
    current_salary = initial_salary + 100 * full_months
    
    full_two_week_periods = work_duration.days // 14
    
    vacation_pay = (initial_salary + 100 * (full_months - 1)) * full_two_week_periods if full_months > 0 else 0
    
    print("\nРезультаты расчета:")
    print(f"Дата начала работы: {start_date.strftime('%d.%m.%Y')}")
    print(f"Текущая дата: {current_date.strftime('%d.%m.%Y')}")
    print(f"Отработано полных месяцев: {full_months}")
    print(f"Текущая зарплата: {current_salary:.2f} руб.")
    print(f"Накоплено дней отпуска: {full_two_week_periods}")
    print(f"Сумма отпускных: {vacation_pay:.2f} руб.")

calculate_vacation_stats()