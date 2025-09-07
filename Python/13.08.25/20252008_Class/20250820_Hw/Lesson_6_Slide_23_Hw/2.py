dimensions = input("Enter field dimensions (x*y): ")
x, y = map(int, dimensions.split('x'))
row = 1
while row <= y:
    print('o' * x)
    row += 1