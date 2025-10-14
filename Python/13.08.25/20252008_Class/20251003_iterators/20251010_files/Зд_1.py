f = open('my_numbers.txt', 'w', encoding='utf-8') 
f.write("Birds of\nthe same\nfeather flocks together\n-goes\nthe saying\n")
f = open('my_numbers.txt', 'r', encoding='utf-8') 
max_length = 0
longest_line = ""
for line in f:
        stripped_line = line.strip()  
        if len(stripped_line) > max_length:
            max_length = len(stripped_line)
            longest_line = stripped_line

print("Самая длинная строка:", longest_line)
