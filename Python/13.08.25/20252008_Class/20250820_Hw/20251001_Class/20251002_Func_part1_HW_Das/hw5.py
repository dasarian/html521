# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров. Если границы диапазона перепутаны (например, 5- верхняя граница, 25- нижняя граница), их нужно поменять местами.  


def product_in_range(start, end):
    if start > end:
        start, end = end, start

    product = 1
    for number in range(start, end + 1):
        product *= number

    return product

result = product_in_range(5, 3)
print(f"Произведение чисел в диапазоне: {result}")
