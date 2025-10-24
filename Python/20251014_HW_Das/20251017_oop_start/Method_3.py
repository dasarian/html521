# Устанавливает новое описание.

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False

def set_description(self, new_description):
        """Устанавливает новое описание задачи."""
        self.description = new_description
    
    
