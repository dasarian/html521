meters = float(input("Введите количество метров: "))

centimeters = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
miles = meters / 1609.34  # 1 миля = 1609.34 метров

print(f"\n{meters} метров равно:")
print(f"{centimeters} сантиметров")
print(f"{decimeters} дециметров")
print(f"{millimeters} миллиметров")
print(f"{miles:.6f} миль")  
