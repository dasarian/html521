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


# 1. 
def process_list(lst):
    iterator = iter(lst)
    first = next(iterator)
    squares = [str(i**2) for i in range(1, first + 1)]
    print("Квадраты чисел от 1 до", first, ": ", ", ".join(squares))



