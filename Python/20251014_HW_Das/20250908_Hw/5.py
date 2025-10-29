# 5. С помощью только while сделать задачи 2, 3, 4

# Задача 2

x, y = map(int, input("Размеры (например 7x8): ").split("x"))
i = 0
while i < y:
    print("о" * x)
    i += 1

# Задача 3

x, y = map(int, input("Размеры (например 7x8): ").split("x"))

print("о" * x)  # верх

i = 0
while i < y - 2:
    print("о" + " " * (x - 2) + "о")
    i += 1

print("о" * x)  # низ


# Задача 4

items = [("Хлеб", 45), ("Молоко", 60), ("Сыр", 350)]
i = 0
total = 0

while i < len(items):
    print(items[i][0], items[i][1])
    total += items[i][1]
    i += 1

print("Сумма:", total)


