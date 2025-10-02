import user_manager

def main():
    users = {}

    while True:
        print("\n=== Управление пользователями ===")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Показать список пользователей")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            name = input("Введите имя пользователя: ")
            try:
                age = int(input("Введите возраст пользователя: "))
                user_manager.add_user(users, name, age)
                print(f"Пользователь {name} успешно добавлен.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            name = input("Введите имя пользователя для удаления: ")
            try:
                user_manager.remove_user(users, name)
                print(f"Пользователь {name} успешно удалён.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            user_manager.list_users(users)

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
