# 1. Создайте класс Печатное Издание, у него есть название и год издания
# 2. Унаследуйте печатное издание, создав классы
# Книга : У книги есть автор
# Журнал : у журнала есть издательство, номер и периодичность выхода
# 3. Создайте массив за 5 лет ежемесячных журналов "Работница" c 2015 года
# 4. Создайте массив из 3 разных книг
# 5. Запишите массивы в файл, создайте функции записи в файл

# Печатного издания, книги, журнала, используя super()

# надо написать с 
# self.__name и @property





class PechatnoeIzdanie:
    def __init__(self, name, year):
        self.__name = name       # закрытые поля
        self.__year = year

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    def write_to_file(self, file):
        file.write(f"Название: {self.name}, Год: {self.year}\n")


class Kniga(PechatnoeIzdanie):
    def __init__(self, name, year, author):
        super().__init__(name, year)
        self.__author = author

    @property
    def author(self):
        return self.__author

    def write_to_file(self, file):
        super().write_to_file(file)      # вызываем метод родителя
        file.write(f"Автор: {self.author}\n\n")


class Zhurnal(PechatnoeIzdanie):
    def __init__(self, name, year, publisher, number, periodicity):
        super().__init__(name, year)
        self.__publisher = publisher
        self.__number = number
        self.__periodicity = periodicity

    @property
    def publisher(self):
        return self.__publisher

    @property
    def number(self):
        return self.__number

    @property
    def periodicity(self):
        return self.__periodicity

    def write_to_file(self, file):
        super().write_to_file(file)
        file.write(f"Издательство: {self.publisher}, "
                   f"Номер: {self.number}, "
                   f"Периодичность: {self.periodicity}\n\n")


# 3. Массив журналов "Работница" за 5 лет ежемесячно с 2015
journals = []
for year in range(2015, 2020):
    for month in range(1, 13):
        journals.append(Zhurnal("Работница", year, "Издательство Ромашка", month, "ежемесячно"))

# 4. Массив из 3 книг
books = [
    Kniga("Война и мир", 1869, "Л.Н. Толстой"),
    Kniga("Преступление и наказание", 1866, "Ф.М. Достоевский"),
    Kniga("Мастер и Маргарита", 1967, "М.А. Булгаков")
]

# 5. Запись в файл
with open("library_room.txt", "w", encoding="utf-8") as f:
    f.write("=== КНИГИ ===\n")
    for b in books:
        b.write_to_file(f)

    f.write("\n=== ЖУРНАЛЫ ===\n")
    for j in journals:
        j.write_to_file(f)

print("Файл library_room.txt успешно создан!")
