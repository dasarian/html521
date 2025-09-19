import random

def word_form(number, words):
    if number % 100 not in range(11, 19):
        if number % 10 == 1:
            return words['one']
        elif number % 10 in (2, 3, 4):
            return words['few']
    return words['many']

kubiki = [str(i) for i in range(0, 10)]
zagadka = []

for i in range(4):
    pos = random.randint(i == 0, len(kubiki) - 1)
    kubik = kubiki[pos]
    del kubiki[pos]
    zagadka.append(kubik)

zagadka_str = ''.join(zagadka)


while True:
    popitka = input('Введи своё 4-х значное число: ')

    if len(popitka) != 4 or not popitka.isdigit() or len(set(popitka)) != 4:
        print('Некорректный ввод. Введите 4-х значное число с неповторяющимися цифрами.')
        continue

    bulls = 0
    cows = 0

    for i in range(4):
        if popitka[i] == zagadka_str[i]:
            bulls += 1
        elif popitka[i] in zagadka_str:
            cows += 1

    bulls_word = word_form(bulls, {'one': 'бык', 'few': 'быка', 'many': 'быков'})
    cows_word = word_form(cows, {'one': 'корова', 'few': 'коровы', 'many': 'коров'})

    print(f"{bulls} {bulls_word}, {cows} {cows_word}")

    if bulls == 4:
        print('Ура, ты выиграл!')

