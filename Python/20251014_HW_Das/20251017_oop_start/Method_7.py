# попадали ли в дни выполнения сб, вс, праздники? 
# Сколько дней было на задачу с учётом праздников и выходных?

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False  
    
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
