# напишите программу, которая моделирует работу стека. 
# Пользователь должен уметь добавлять числа в стек, удалять верхний элемент и просматривать содержимое стека. 
# Программа завершает работу по команде exit.

def main():
    stack = []

    while True:
        print("\nВыберите действие:")
        print("1. push - Добавить число в стек")
        print("2. pop - Удалить верхний элемент")
        print("3. view - Просмотреть содержимое стека")
        print("4. exit - Выйти из программы")

        choice = input("Введите команду: ").strip().lower()

        if choice == "push":
            try:
                number = int(input("Введите число для добавления в стек: "))
                stack.append(number)
                print(f"Число {number} добавлено в стек.")
            except ValueError:
                print("Ошибка: введите корректное число.")

        elif choice == "pop":
            if stack:
                removed = stack.pop()
                print(f"Удалён верхний элемент: {removed}.")
            else:
                print("Стек пуст, нечего удалять.")

        elif choice == "view":
            if stack:
                print("Содержимое стека (сверху вниз):")
                for i in range(len(stack) - 1, -1, -1):
                    print(stack[i])
            else:
                print("Стек пуст.")

        elif choice == "exit":
            print("Завершение работы программы.")
            break

        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
