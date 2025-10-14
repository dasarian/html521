def main():
    file_name = "notes.txt"

    while True:
        print("\nВыберите действие:")
        print("create - Создать новый файл")
        print("add - Добавить заметку")
        print("view - Просмотреть заметки")
        print("exit - Выйти")

        choice = input("Введите команду: ").strip().lower()

        if choice == "create":
            try:
                with open(file_name, 'w', encoding='utf-8') as f:
                    print(f"Файл '{file_name}' создан или очищен.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == "add":
            try:
                note = input("Введите заметку: ")
                with open(file_name, 'a', encoding='utf-8') as f:
                    f.write(note + '\n')
                print("Заметка добавлена.")
            except FileNotFoundError:
                print(f"Файл '{file_name}' не найден. Сначала создайте файл.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == "view":
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    notes = f.readlines()
                    if not notes:
                        print("Заметок нет.")
                    else:
                        print("Список заметок:")
                        for i, note in enumerate(notes, start=1):
                            print(f"{i}. {note.strip()}")
            except FileNotFoundError:
                print(f"Файл '{file_name}' не найден. Сначала создайте файл.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == "exit":
            print("Выход из программы.")
            break

        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()


