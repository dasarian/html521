def bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
    
    for digit in set(guess):  
        cows += min(secret.count(digit), guess.count(digit))  
    
    cows -= bulls
    
    return bulls, cows

secret = input("Введите загаданное число: ")
guess = input("Введите предложенное число: ")

if len(secret) != len(guess) or not (secret.isdigit() and guess.isdigit()):
    print("Ошибка: числа должны быть одинаковой длины и содержать только цифры!")
else:
    bulls, cows = bulls_and_cows(secret, guess)
    print(f"Быков: {bulls}, Коров: {cows}")