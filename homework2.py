from datetime import date


class LibraryBook:

    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self._unavailable_since = None if available else date.today()


class LibraryCatalogManager:

    def __init__(self):
        self._books = []

    def add_book_to_library(self, title, author, year):
        """Добавляет книгу в каталог и возвращает её."""
        book = LibraryBook(title, author, year)
        self._books.append(book)
        return book

    def borrow_book(self, title):
        """Выдаёт первую доступную книгу с указанным названием."""
        for book in self._books:
            if book.title == title and book.available:
                book.available = False
                book._unavailable_since = date.today()
                return True
        return False

    def oldest_books(self, n):
        """Возвращает до n самых старых книг."""
        if n < 0:
            raise ValueError("Количество книг не может быть отрицательным.")

        return sorted(self._books, key=lambda book: book.year)[:n]

    def remove_missing_books(self):
        """Удаляет книги, недоступные более одного календарного года."""
        today = date.today()

        try:
            cutoff = today.replace(year=today.year - 1)
        except ValueError:
            cutoff = today.replace(year=today.year - 1, day=28)

        books_before = len(self._books)
        self._books = [
            book
            for book in self._books
            if book._unavailable_since is None
            or book._unavailable_since >= cutoff
        ]
        return books_before - len(self._books)

if __name__ == "__main__":
    catalog = LibraryCatalogManager()
    catalog.add_book_to_library("Мастер и Маргарита", "М. Булгаков", 1967)
    catalog.add_book_to_library("Война и мир", "Л. Толстой", 1869)

    catalog.borrow_book("Мастер и Маргарита")

    for book in catalog.oldest_books(2):
        status = "в наличии" if book.available else "выдана"
        print(f"{book.title} ({book.year}) — {status}")