# Передача аргументов по позиции и по имени

print(1, 2, 3, 4, 5, sep='-=-=-=-', end='\n\n\nWOW!!!!\n')

# Правило первое: если у функции есть аргументы с именами, 
# их можно вызывать по именам 
# Правило второе: аргументы, переданные по именам, можно менять 
# местами, но нельзя указывать многократно или раньше, чем аргументы, 
# которые мы передаем по позиции

# Задача: есть словарь, в котром указаны полные имена людей
# Надо написать функцию, которая получает имя или фамилию и возвращает телефон
phonebook = {
    'Баринова Вера Олеговна': '+79169574385',
    'Чебурашка' : '+12367632',
    'Крокодил Гена' : '647547654'
}

def find_phone(name, surname=''):
    print('name', name)
    print('surname', surname)
    for full_name in phonebook:
        if name in full_name or surname in full_name:
            return phonebook[full_name]  # phone
        

# Решить проблему: при указании Гена Баринова должны быть возвращены два телефона

# Передача параметров по позиции
print(find_phone('Вера'))
# Передача параметров по имени:
print(find_phone(surname='Баринова', name='Вера'))

print()

# Решить проблему: при указании Гена Баринова должны быть возвращены два телефона

phonebook = {
    'Баринова Вера Олеговна': '+79169574385',
    'Чебурашка': '+12367632',
    'Крокодил Гена': '647547654'
}
def find_phones(query):
    query_parts = query.split()
    matching_phones = []
    
    for name, phone in phonebook.items():
        if any(part.lower() in name.lower() for part in query_parts):
            matching_phones.append(phone)
    return matching_phones

query = "Гена Баринова"
phones = find_phones(query)
print(f"Телефоны для '{query}': {phones}")

