# Сколько дней было дано на задачу?

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False  
    
    def total_days_given(self):
        """Возвращает общее количество дней, данных на выполнение задачи."""
        delta = self.deadline - self.dt
        return delta.days
    