# Написать свой класс для хранения информации о человеке: фамилия, имя, отчество, дата рождения

from datetime import date

class Person:
    def __init__(self, surname, name, patronymic, birth_date):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birth_date = birth_date  


# Напишите свой метод :  
# Делает задачу завершённой
# Проверяет, завершена ли задача?
# Устанавливает новое описание.
# Устанавливает новый дедлайн
# Проверяет, сколько осталось дней до срока выполнения? Часов?
# Сколько дней было дано на задачу?
# попадали ли в дни выполнения сб, вс, праздники? Сколько дней было на задачу с учётом праздников и выходных?




    



    
    

    

   

    def working_days_given(self, holidays=None):
        """
        Возвращает количество рабочих дней, данных на выполнение задачи,
        с учётом выходных (сб, вс) и праздников.
        """
        if holidays is None:
            holidays = []

        delta = self.deadline - self.dt
        working_days = 0
        for i in range(delta.days + 1):
            current_day = self.dt + timedelta(days=i)
            if current_day.weekday() < 5 and current_day not in holidays:
                working_days += 1
        return working_days

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = "Выполнена" if self.done else "Не выполнена"
        return (f"Описание: {self.description}\n"
                f"Создана: {self.dt.strftime('%d.%m.%Y %H:%M')}\n"
                f"Дедлайн: {self.deadline.strftime('%d.%m.%Y %H:%M')}\n"
                f"Статус: {status}")
