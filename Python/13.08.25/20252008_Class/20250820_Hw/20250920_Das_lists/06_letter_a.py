# Задание №6 (четверг, 25 сентября)
# Выписать из строки только слова, содержащие букву 'а'

text = 'Мама читала интересную книгу'
words = text.split()
lower_word = []

for word in words:
    if 'а' in word.lower():
        lower_word.append(word)

print(lower_word)