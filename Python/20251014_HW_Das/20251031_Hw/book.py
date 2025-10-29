# Создайте класс Печатное Издание, у него есть название и год издания
# Унаследуйте печатное издание, создав классы
# Книга 
# У книги есть автор
# Журнал  
# у журнала есть издательство, 
# номер 
# и периодичность выхода
# Создайте массив за 5 лет ежемесячных журналов "Работница" c 2015 года
# Создайте массив из 3 разных книг
# Запишите массивы в файл, создайте функции записи в файл

# Печатного издания, книги, журнала, используя super()



class PechatnoeIzdanie:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    def write_to_file(self, file):
        file.write(f"Название: {self.__name}, Год издания: {self.__year}\n")


class Kniga(PechatnoeIzdanie):
    def __init__(self, name, year, author):
        super().__init__(name, year)  
        self.__author = author

    def write_to_file(self, file):
        super().write_to_file(file)  
        file.write(f"Автор: {self.__author}\n\n")


class Zhurnal(PechatnoeIzdanie):
    def __init__(self, name, year, publisher, number, periodicity):
        super().__init__(name, year)
        self.__publisher = publisher
        self.__number = number
        self.__periodicity = periodicity

    def write_to_file(self, file):
        super().write_to_file(file)
        file.write(f"Издательство: {self.__publisher}, Номер: {self.__number}, "
                   f"Периодичность: {self.__periodicity}\n\n")


journals = []
for year in range(2015, 2020):       
    for month in range(1, 13):       
        journals.append(Zhurnal("Работница", year, "Издательство A", month, "ежемесячно"))

books = [
    Kniga("Война и мир", 1869, "Л.Н. Толстой"),
    Kniga("Мастер и Маргарита", 1967, "М.А. Булгаков"),
    Kniga("Преступление и наказание", 1866, "Ф.М. Достоевский")
]

with open("library.txt", "w", encoding="utf-8") as file:
    file.write("=== КНИГИ ===\n")
    for book in books:
        book.write_to_file(file)

    file.write("\n=== ЖУРНАЛЫ ===\n")
    for journal in journals:
        journal.write_to_file(file)

print("Файл 'library.txt' успешно создан!")
