def count_args(*args1, **args2):
    total_args = len(args1) + len(args2)
    named_args = list(args2.keys())
    return total_args, named_args

total, named = count_args(1, 2, 3, name="Alice", age=25, city="Moscow")
print(f"Общее количество аргументов: {total}")
print(f"Список названий именованных аргументов: {named}")
