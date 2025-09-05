# Escape (эс - кейп) - побег, выход, избавление, спасение
#\n - перенос строки
#\t - табуляция
#\x - 16-ричный код символа
print('\x6d\x61\x6d\x61 \x6d\x79\x6c\x61 \x72\x61\x6d\x75')
# print('It's a wonderfull life') - ошибка! одинарная кавычка внутри строки!
print('It\'s a wonderfull life')  # Экранировали кавычку
# print('C:\Users\Student')   ошибка - несуществующие эскейп-последовательности
print('C:\\Users\\Student') # Забэкслешили - экранировали
print(r'C:\Users\Student')  # Использовали raw-строку
