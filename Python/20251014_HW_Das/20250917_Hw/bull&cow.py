# Написать (можно с функцией, но можно и отдельным файлом)
# проверку числа и выбор верной формы существительного с числительным
# 0 коров
# 1 корова
# 2,3,4, коровы
# 5 коров
# 11 коров
# 21 корова



def choose_cow_form(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError()

    if number % 100 in (11, 12, 13, 14):
        return f"{number} коров"
    elif number % 10 == 1:
        return f"{number} корова"
    elif number % 10 in (2, 3, 4):
        return f"{number} коровы"
    else:
        return f"{number} коров"


print(choose_cow_form(0))   
print(choose_cow_form(1))   
print(choose_cow_form(2))   
print(choose_cow_form(3))   
print(choose_cow_form(4))   
print(choose_cow_form(5))   
print(choose_cow_form(11))  
print(choose_cow_form(21))  
print(choose_cow_form(22))  
print(choose_cow_form(25))  
print(choose_cow_form(101)) 
print(choose_cow_form(111)) 
print(choose_cow_form(121)) 
