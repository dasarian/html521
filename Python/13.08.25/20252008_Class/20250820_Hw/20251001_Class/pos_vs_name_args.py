# Позиционные аргументы - это не просто те аргументы, которые 
# переданы по позиции. Это те аргументы, которые по-другому 
# передать нельзя!

# Задача: написать функцию, которая из слов делает предложение: 
# дописывает точку в конце и первое слово пишет с большой буквы. 
# Между словами вставляются пробелы.

def make_text(*words):
    # НЕПРАВИЛЬНО! result = ' '.join(words)
    result = words[0][0].upper() + words[0][1:] + ' '
    result += ' '.join(words[1:]) + '.'
    return result

my_story = make_text('мама', 'мыла', 'раму')
print(my_story)

# До 21:50 Задача: даны слова и "ширина страницы" в буквах. 
# Например, известно, что на страницу помещается 20 букв. 
# Разрывать слово нельзя, переносить - сложно. Реализовать
# функцию, которая отформатирует ваш текст по "ширине страницы":
# 
12345678901234567890
# Мама мыла раму с 
# мылом и долго терла
# потом его сухой 
# тряпкой.

# Слова - позиционные аргументы.
# Про ширину страницы поговорим потом


def format_text(text, page_width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0  

    for word in words:
        word_length = len(word)
        space_length = 1 if current_line else 0

        if current_length + word_length + space_length <= page_width:
            current_line.append(word)
            current_length += word_length + space_length
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = word_length

    if current_line:
        lines.append(' '.join(current_line))
    return '\n'.join(lines)

text = "Мама мыла раму с мылом и долго терла потом его сухой тряпкой."
formatted_text = format_text(text, 20)
print(formatted_text)
