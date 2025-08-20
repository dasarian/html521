age = input('Сколько Вам лет? ')
age = int(age)   # Приводим к числу!
student = age > 14 and age < 24   # логи
adult = age >  24 and  age < 50
senior = age > 50
child = age<14

if child:
    print('Едешь бесплатно!')