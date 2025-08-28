import traceback
m = input('Введи номер месяца')
try:
    if int(m) > 12:
        raise ValueError(
            f'Ошибка - слишком большой номер месяца {m}')
except:
    print(traceback.format_exc())

int('uijgiug')#, 35)