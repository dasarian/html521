# Неявное использование итератора - встроено в for
arr = [1, 3, 5, 7]
for elem in arr:
    print(elem)

# Явное использование итератора - создание объекта для итерируемого
my_iterator = iter(arr)
print(arr)  # сам список никуда не делся - остался прежним!
print(my_iterator, type(my_iterator))  # Можно напечатать тип полученного итератора
print(next(my_iterator))  # Каждый следующий вызов функции next возвращает текущий элемент и переходит к следующему
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))  # Когда элементов не осталось, возбуждается исключение StopIteration

# Задание: поймать и обработать исключение StopIteration
# Для обхода списка исплользовать цикл while True и break


my_list = [10, 20, 30, 40]
iterator = iter(my_list)
print("Обход элементов списка:")
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        print("Итерация завершена: достигнут конец списка.")
        break




