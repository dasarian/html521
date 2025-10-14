search_word = input("Введите слово для поиска: ")
f = open('my_numbers.txt', 'w', encoding='utf-8') 
f.write("Birds of\nthe same\nfeather flocks together\n-goes\nthe saying\n")
f = open('my_numbers.txt', 'r', encoding='utf-8') 
count = 0
for line in f:
   if search_word in line:
            count += 1

print(f"Количество строк, содержащих слово '{search_word}': {count}")
