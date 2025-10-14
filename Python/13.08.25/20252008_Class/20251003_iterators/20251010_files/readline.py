f = open('mylist.txt', 'r', encoding='utf-8') 
content = f.readlines()
f.close()
print(content)


