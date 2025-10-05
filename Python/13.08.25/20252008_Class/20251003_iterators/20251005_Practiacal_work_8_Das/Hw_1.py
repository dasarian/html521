text = "Первая строка\nВторая строка\nТретья строка"
def iterate_text_lines(text):
    lines_iterator = iter(text.split('\n'))
    print("Обход строк текста:")
    while True:
        try:
            line = next(lines_iterator)
            print(line)
        except StopIteration:
            print("Текст завершён")
            break
iterate_text_lines(text)

