print(list('abcd'))

# 1. Перечисление
fruit = ['strawberry', 'qiwi', 'plum']
print(fruit)

# 2. Получение в результате деления строки
words = 'Теперь раму мыл папа'.split()
print(words)

# 3. Генерация
squares = [x * x for x in range(10)]
print(squares)

fruit = ['strawberry', 'qiwi', 'plum']
print(fruit[0])

fruit = ['strawberry', 'qiwi', 'plum']
print("Остальные элементы:")
print(fruit[1])  
print(fruit[2])  


fruit = ['strawberry', 'qiwi', 'plum']
print(fruit[len(fruit) - 1])

fruit = ['strawberry', 'qiwi', 'plum']
fruit[0] = 'pear'         
fruit.append('banana')    
breakfast = fruit.pop()   
del fruit[1]              
fruit += ['mango', 'melon']  
print("Удален фрукти: 'qiwi'")
print("Осталось фрукти:", fruit)

# 1. 
fruit = ['pear', 'plum', 'mango', 'melon']
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1
print()

# 2. 
fruit = ['pear', 'plum', 'mango', 'melon']
for i in range(len(fruit)):
    print(fruit[i])

print()

#3. 
fruit = ['pear', 'plum', 'mango', 'melon']
for f in fruit:
    print(f)

