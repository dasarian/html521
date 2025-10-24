# Проверяет, завершена ли задача?

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False

def is_done(self):
        """Проверяет, завершена ли задача."""
        return self.done