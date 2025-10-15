# создайте программу, которая симулирует систему управления задачами. 
# Задачи организуются в виде стека. Реализуйте возможность добавления задач с приоритетами (обычная и высокая). 
# Задачи с высокой приоритетностью должны выполняться первыми, но обычные задачи сохраняются в порядке добавления.

def main():
    high_priority_tasks = []  # Стек для задач с высоким приоритетом
    normal_priority_tasks = []  # Стек для обычных задач

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу с высоким приоритетом")
        print("2. Добавить обычную задачу")
        print("3. Выполнить задачу")
        print("4. Просмотреть все задачи")
        print("5. Выйти из программы")

        choice = input("Введите команду: ").strip()

        if choice == "1":
            task = input("Введите описание задачи с высоким приоритетом: ")
            high_priority_tasks.append(task)
            print(f"Задача '{task}' добавлена с высоким приоритетом.")

        elif choice == "2":
            task = input("Введите описание обычной задачи: ")
            normal_priority_tasks.append(task)
            print(f"Обычная задача '{task}' добавлена.")

        elif choice == "3":
            if high_priority_tasks:
                task = high_priority_tasks.pop()
                print(f"Выполнена задача с высоким приоритетом: '{task}'.")
            elif normal_priority_tasks:
                task = normal_priority_tasks.pop()
                print(f"Выполнена обычная задача: '{task}'.")
            else:
                print("Нет задач для выполнения.")

        elif choice == "4":
            print("\nЗадачи с высоким приоритетом:")
            for task in reversed(high_priority_tasks):
                print(f"- {task}")
            print("\nОбычные задачи:")
            for task in reversed(normal_priority_tasks):
                print(f"- {task}")

        elif choice == "5":
            print("Завершение работы программы.")
            break

        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
