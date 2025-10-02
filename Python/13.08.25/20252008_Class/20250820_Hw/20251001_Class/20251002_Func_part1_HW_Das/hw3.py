# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# 1. если она равна True, квадрат заполненный;
# 2. если False, квадрат пустой.

def draw_square(side_length, symbol, filled):
    for i in range(side_length):
        for j in range(side_length):
            if filled or i == 0 or i == side_length - 1 or j == 0 or j == side_length - 1:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print()  

print("Заполненный квадрат:")
draw_square(5, '*', True)

print("\nПустой квадрат:")
draw_square(5, '*', False)
