address_example = "ул. {street}, дом {house}, квартира {apartment}"

address_1 = address_example.format(street="Ленина", house=12, apartment=34)
address_2 = address_example.format(street="Пушкина", house=5, apartment=2)
address_3 = address_example.format(street="Гагарина", house=10, apartment=1)

print(address_1)
print(address_2)
print(address_3)