from book_class import Book
from library_class import Library
from user_class import User


library = Library()


book1 = Book(title="Harry Potter", author="J.K. Rowling", genre="Fantasy")
book2 = Book(title="1984", author="J. Orwell", genre="dystopia")
book3 = Book(title="Мастер и Маргарита", author="М.Булгаков", genre="roman")

library.add_book(book1)
library.add_book(book2)

books = library.get_books()
print("Книги библиотеки: ", books)


user1 = User(name="Hamit")

print(f"Юзер {user1.name} берет книгу {book1}")
user1.take_book(book1)

print("Книги у юзера: ", user1.get_books())

print(f"Юзер {user1.name} возвращает книгу {book1}")
user1.return_book(book1)
print("Книги у юзера: ", user1.get_books())












# print(book1.get_available())
# book1.set_available(True)
# print("После изменения: ", book1.get_available())
# book1 = [book1]
# print(book1)