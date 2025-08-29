import random

def generate_secret_number():
    """Generate a random four-digit number with unique digits"""
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def count_bulls_and_cows(guess, secret):
    """Counting bulls and cows"""
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_game():
    """Basic logic of the game"""
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to the game 'Bulls and Cows'!")
    print("I thought of a four-digit number with unique digits")
    print("Your task is — guess it. After each attempt I will say, how many bulls and cows")

    while True:
        guess = input("Please enter four digit number: ").strip()

        # Проверка корректности ввода
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Error: enter a four digit number with unique digits.")
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(guess, secret_number)

        if bulls == 4:
            print(f"Congratulations! You guessed the number {secret_number} for {attempts} attempts!")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")

if __name__ == "__main__":
    play_game()
