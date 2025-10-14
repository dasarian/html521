f = open("user_data.txt", 'a', encoding='utf-8') 
while True:
        user_input = input("Введите строку (или 'exit' для завершения): ")
        if user_input.lower() == 'exit':
            break
f.write(user_input + '\n')
f.close()
print("\nСодержимое файла:")
f = open("user_data.txt", 'r', encoding='utf-8') 
content = f.read()
print (content)
f.close()

