# Задание №4 (вторник, 23 сентября)
# Пусть есть список строк. Сделать два списка:
# список тех же строк, написанных капсом (заглавными)
# список тех же строк, написанных строчными (маленькими)
#  Например:
#  ['abc', 'Def', 'GHi']
#  ['ABC', 'DEF', 'GHI']
#  ['abc', 'def', 'ghi']

strings = ['abc', 'Def', 'GHi']
upper_strings = [s.upper() for s in strings]
lower_strings = [s.lower() for s in strings]

print("Заглавные:", upper_strings)
print("Строчные:", lower_strings)