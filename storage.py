import json
from pathlib import Path

from models import Book


DATA_FILE = Path("books.json")


def load_books(file_path: Path | str = DATA_FILE) -> list[Book]:
    path = Path(file_path)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [Book.from_dict(item) for item in data]


def save_books(books: list[Book], file_path: Path | str = DATA_FILE) -> None:
    path = Path(file_path)
    with path.open("w", encoding="utf-8") as file:
        json.dump(
            [book.to_dict() for book in books],
            file,
            ensure_ascii=False,
            indent=2,
        )


def find_book(books: list[Book], author: str, title: str) -> Book | None:
    normalized_author = author.strip().casefold()
    normalized_title = title.strip().casefold()

    for book in books:
        same_author = book.author.casefold() == normalized_author
        same_title = book.title.casefold() == normalized_title
        if same_author and same_title:
            return book

    return None


def add_book(book: Book, file_path: Path | str = DATA_FILE) -> bool:
    books = load_books(file_path)
    if find_book(books, book.author, book.title) is not None:
        return False

    books.append(book)
    save_books(books, file_path)
    return True


def delete_book(author: str, title: str, file_path: Path | str = DATA_FILE) -> bool:
    books = load_books(file_path)
    book_to_delete = find_book(books, author, title)

    if book_to_delete is None:
        return False

    books.remove(book_to_delete)
    save_books(books, file_path)
    return True
