# Задание №5 (среда, 24 сентября)
# Пусть есть строка. Создать список тех её слов, у которых чётная длина
# Например
# 'Мама читала книгу'
# ['Мама', 'читала']

text = 'Я люблю программировать на Python'
words = text.split()
even_length = []

for word in words:
    if len(word) % 2 == 0:
        even_length.append(word)

print(even_length)