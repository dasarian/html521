# 1. Синтаксис объявления функции в Python
def summa(param1, param2):
    # тело
    return param1 + param2

# lambda p1, p2: return p1 + p2

# ЛИБО вызываем lambda однократно
# ЛИБО присваиваем её переменной, передаем в параметр и т.д.

# Обычный вызов функции:
print(summa(9, 13))          #  Можно напечатать
print(summa(9, 13) == 22)    #  Можно использовать в вычислениях 
result = summa(9, 13)        #  Можно результат (ВОЗВРАЩАЕМЫЙ!) присвоить переменной


print('Лямбда: ')
lambda arg1, arg2: arg1 + arg2
# Вызов lambda
# Первые скобки, чтобы ВТОРЫЕ СКОБКИ относились ко всему выражению, а не к arg2
print((lambda arg1, arg2: arg1 + arg2)(9, 13))
print((lambda arg1, arg2: arg1 + arg2)(9, 13) == 22)

# lambda можно присваивать переменной, которая (переменная) становится функцией, 
# которую можно вызвать
mysum = lambda arg1, arg2: arg1 + arg2
print(mysum(9, 13))

# Задание: 
# 1. Написать свою функцию, которая принимает стороны прямоугольника и возвращает периметр 
# 2. Написать функцию площади прямоугольника 
# 3. Написать лямбда-выражения для первых двух задач
# 20:15 сдать


# 1. 
def периметр_прямоугольника(length, width):
    return 2 * (length + width)
length = 5
width = 3
perimeter = периметр_прямоугольника(length, width)
print(f"Периметр прямоугольника: {length} и {width} равен {perimeter}")


# 2. 
def периметр_прямоугольника(length, width):
    return length * width
length = 7
width = 4
area = периметр_прямоугольника(length, width)
print(f"Площадь прямоугольника : {length} и {width} равна {area}")

# 3. 
# для первого задачи :
perimeter = lambda length, width: 2 * (length + width)
length = 5
width = 3
print((lambda length, width: 2*(length+width))(5, 3))
print(f"Периметр прямоугольника : {length} и {width} равен {perimeter(length, width)}")


# для второго задачи :
area = lambda length, width: length * width
length = 7
width = 4
print(f"Площадь прямоугольника : {length} и {width} равна {area(length, width)}")



