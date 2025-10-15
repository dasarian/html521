# напишите программу, которая моделирует очередь. 
# Пользователь может добавлять элементы в конец очереди, обслуживать (удалять) элементы из начала и просматривать текущую очередь. 
# Реализуйте обработку ошибок, если очередь пуста.

def main():
    queue = []

    while True:
        print("\nВыберите действие:")
        print("1. enqueue - Добавить элемент в очередь")
        print("2. dequeue - Обслужить элемент (удалить из начала)")
        print("3. view - Просмотреть текущую очередь")
        print("4. exit - Выйти из программы")

        choice = input("Введите команду: ").strip().lower()

        if choice == "enqueue":
            element = input("Введите элемент для добавления в очередь: ")
            queue.append(element)
            print(f"Элемент '{element}' добавлен в очередь.")

        elif choice == "dequeue":
            if queue:
                removed_element = queue.pop(0)
                print(f"Обслужен элемент: '{removed_element}'.")
            else:
                print("Ошибка: очередь пуста, нечего обслуживать.")

        elif choice == "view":
            if queue:
                print("Текущая очередь (с начала до конца):")
                for element in queue:
                    print(element)
            else:
                print("Очередь пуста.")

        elif choice == "exit":
            print("Завершение работы программы.")
            break

        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
