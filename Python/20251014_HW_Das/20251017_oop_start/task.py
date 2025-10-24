from datetime import datetime, timedelta

class Task:

    def __init__(self, 
            description,  # Обязательный параметр
            dt_till=datetime.now() + timedelta(1)):
            # Необязательный параметр: если его не указать, 
            # будет выбрана дата сразу за созданием задачи
        self.dt           = datetime.now()  # Время постановки задачи
        self.deadline     = dt_till         # Срок окончания работы
        self.description  = description     # Описание (суть) задачи
        self.done         = False           # Завершена ли задача?

    def later(self, more_days):
        self.deadline += timedelta(more_days)

    # Делает задачу завершённой
    def finish(self):  # в отличие от функций, у методов, если не предполагается 
        # передача параметров извне, для работы с полями класса обязательно self
        self.done = True

    # Проверяет, завершена ли задача?
    def is_done(self):
        return self.done
    # Устанавливает новое описание.
    # Устанавливает новый дедлайн


t = Task('Написать классы Автомобиль, Человек, Одежда, Товар')
print(t.deadline)  # какой получился срок у задачи?
t.later(3)         # отсрочить задачу на три дня. Какой теперь срок? Напечатайте
print(t.is_done)   # Метод требуется вызвать, чтобы он работал. Так он напечатается "это метод" 
print(t.finish())  # завершает задачу!
print(t.is_done()) # Вызывает метод проверки, завершена ли задача