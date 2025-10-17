# Делает задачу завершённой

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False  

def mark_as_done(self):
        """Делает задачу завершённой."""
        self.done = True
