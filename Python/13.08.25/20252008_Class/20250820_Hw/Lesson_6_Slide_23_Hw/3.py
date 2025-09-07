dimensions = input("Enter field dimensions: ")
width, height = map(int, dimensions.split('x'))
row = 0
while row < height:
    col = 0
    while col < width:
        if row == 0 or row == height - 1 or col == 0 or col == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
        col += 1
    print()
    row += 1