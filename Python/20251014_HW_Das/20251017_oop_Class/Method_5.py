# Проверяет, сколько осталось дней до срока выполнения? Часов?

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False  
    
    def days_until_deadline(self):
        """Возвращает количество дней до дедлайна."""
        delta = self.deadline - datetime.now()
        return delta.days

    def hours_until_deadline(self):
        """Возвращает количество часов до дедлайна."""
        delta = self.deadline - datetime.now()
        return delta.total_seconds() // 3600