class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Library:
    def __init__(self, books=None):
        """Инициализирует библиотеку с заданным списком книг или пустым списком по умолчанию."""
        if books is None:
            books = []
        self.books = books

    def add_book(self, book):
        """Добавляет книгу в библиотеку."""
        self.books.append(book)

    def get_book_by_id(self, book_id):
        """Возвращает книгу по её идентификатору."""
        for book in self.books:
            if book.id == book_id:
                return book
        raise ValueError(f"Книги с id {book_id} не существует")

    def get_index_by_book_id(self, book_id):
        """Возвращает индекс книги в списке по её идентификатору."""
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с id {book_id} не существует")

    def get_next_book_id(self):
        """Возвращает следующий доступный идентификатор для новой книги."""
        if not self.books:  # Если список книг пустой
            return 1
        else:
            # Если книги есть, возвращаем максимальный id + 1
            return max(book.id for book in self.books) + 1

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пусто
    list_books = [Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in
                  BOOKS_DATABASE]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
