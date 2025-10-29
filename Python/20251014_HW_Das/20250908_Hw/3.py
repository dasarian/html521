# 3. Нарисовать только границу поля и пустую серединку.

size = input("Введите размеры поля (например 7x8): ")
x, y = map(int, size.split('x'))

top_bottom = "о" * x
middle = "о" + " " * (x - 2) + "о"
field = top_bottom + "\n" + (middle + "\n") * (y - 2) + top_bottom

print(field)
