# попадали ли в дни выполнения сб, вс, праздники? 
# Сколько дней было на задачу с учётом праздников и выходных?

from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.dt = datetime.now()  
        self.deadline = deadline  
        self.description = description  
        self.done = False  
    
    
