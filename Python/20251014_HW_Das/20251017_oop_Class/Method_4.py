# Устанавливает новый дедлайн

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False
    
    def set_deadline(self, new_deadline):
        """Устанавливает новый дедлайн задачи."""
        self.deadline = new_deadline