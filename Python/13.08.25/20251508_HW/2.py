# Ввод данных от пользователя
salary = float(input("Введите зарплату за месяц: "))
credit = float(input("Введите сумму платежа по кредиту: "))
utilities = float(input("Введите задолженность за коммунальные услуги: "))

# Расчет остатка
remaining = salary - credit - utilities

# Вывод результата
print(f"После всех выплат останется: {remaining:.2f} руб.")