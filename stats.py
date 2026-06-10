from collections import Counter

from models import Book


def calculate_average_rating(books: list[Book]) -> float:
    if not books:
        return 0.0

    total_rating = sum(book.rating for book in books)
    return round(total_rating / len(books), 2)


def count_books_by_author(books: list[Book]) -> dict[str, int]:
    return dict(Counter(book.author for book in books))
