# Кортежи. Отличие списков от кортежей

# 1 отличие:
# Список []
# Кортеж ()

zamk_elems = (0, 4, 6, 8, 9)

# просто кортеж можно записать просто без скобок:
nezamk_elems = 1, 2, 3, 5, 7
print(type(zamk_elems), type(nezamk_elems))
# Печать типов покажет, что перед нами один и тот же тип данных - tuple


# Из кортежей можно читать данные, как из списков (по номеру позиции):
print('На позиции 3 в этом кортеже', zamk_elems, ' расположено ', zamk_elems[3])

# Отличие: на первый уровень кортежа нельзя выполнить присваивание:
import traceback
try: 
    zamk_elems[2] = 9
except:
    traceback.print_exc()

# Если на первом уровне кортежа расположен объект, допускающий изменения,
# его поменять будет можно:
two_lists = ([1, 2], [3, 4])
two_lists[0][0] = 111
print(two_lists)

# Вывод: кортеж - не абсолютная защита, а только некоторое ограничение

# Удаление элемента
try: 
    del two_lists[1]
except:
    traceback.print_exc()

# Что делать? 
# Создавать новый кортеж, в котром отсутствует желаемый к удаленю элемент
# Slice разрешен
# Сложение разрешено
# Создать кортеж из чисел от 1 до 8
# Показать, что это кортеж
# Удалить числа 4 и 7

# Создать кортеж из чисел от 1 до 8
numbers = tuple(range(1, 9))
print("Исходный кортеж:", numbers)  
print("Тип объекта:", type(numbers))  

# Slice
slice_example = numbers[2:5]
print("Срез с 3-го по 5-й элемент:", slice_example)  

# Сложение :
additional_numbers = (10, 11)
combined_tuple = numbers + additional_numbers
print("Объединённый кортеж:", combined_tuple)  

# Удалить числа 4 и 7 
new_numbers = tuple(x for x in numbers if x not in (4, 7))
print("Кортеж без чисел 4 и 7:", new_numbers)  

