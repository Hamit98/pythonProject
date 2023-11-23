from book_class import Book
from library_class import Library
from user_class import User

user1 = User(name="Hamit")

library = Library()

book1 = Book(title="Harry Potter", author="J.K. Rowling", genre="Fantasy")
book2 = Book(title="1984", author="J. Orwell", genre="dystopia")
book3 = Book(title="Мастер и Маргарита", author="М.Булгаков", genre="roman")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print(f"Меню библиотеки:\n"
      f"1. Список всех книг\n"
      f"2. Взять книгу\n"
      f"3. Поиск книг по жанру\n\n")

user_input = input("Выберите действие [1-3]: ")

if user_input == '1':
    print(library.get_books())
elif user_input == '2':
    books = library.get_books()
    for i in range(len(books)):
        print(f"{i}. {books[i]}")

    book_number = int(input("Выберите книгу: "))
    user1.take_book(books[book_number])

elif user_input == "3":
    genre = input("Введите жанр для поиска: ")
    matching_books = library.search_books_by_genre(genre)
    if matching_books:
        print(f"Найденные книги по жанру '{genre}':")
        for book in matching_books:
            print(book)
    else:
        print(f"Книги по жанру '{genre}' не найдены.")


