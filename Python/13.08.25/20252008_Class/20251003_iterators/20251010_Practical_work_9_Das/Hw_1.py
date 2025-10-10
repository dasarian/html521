def repeat_message(message, times):
    for _ in range(times):
        yield message
        
if __name__ == "__main__":
    message = input("Введите сообщение: ")
    times = int(input("Введите количество повторений: "))

    for repeated in repeat_message(message, times):
        print(repeated)
