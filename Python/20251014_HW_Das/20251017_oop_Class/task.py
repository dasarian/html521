from datetime import datetime, timedelta

def __init__(self, description):
    self.dt = datetime.now()
    self.deadline = datetime.now() + timedelta(days=365)
    self.description = description
    self.done = False

