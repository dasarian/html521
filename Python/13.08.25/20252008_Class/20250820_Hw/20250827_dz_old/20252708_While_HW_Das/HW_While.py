from random import randint

max_tasks = 10  
max_errors = 3  
max_error_percent = 20  

correct_answers = 0
wrong_answers = 0
tasks_completed = 0

while tasks_completed < max_tasks and wrong_answers < max_errors:
    a = randint(1, 10)
    b = randint(1, 10)
    result = a + b

    answer = int(input(f'Сколько будет {a} + {b} = '))

    if answer == result:
        print('Верно')
        correct_answers += 1
    else:
        print('Нет, попробуй ещё раз')
        wrong_answers += 1

    tasks_completed += 1

    if tasks_completed > 0:
        error_percent = (wrong_answers / tasks_completed) * 100
        if error_percent > max_error_percent:
            print(f"Процент ошибок превысил {max_error_percent}%! Тест завершён.")
            break

print("\nТест завершён!")
print(f"Верных ответов: {correct_answers}")
print(f"Неверных ответов: {wrong_answers}")
print(f"Процент ошибок: { (wrong_answers / tasks_completed) * 100:.1f}%")
