from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from models import Book
from stats import calculate_average_rating, count_books_by_author
from storage import add_book, delete_book, load_books


class BookTrackerTestCase(unittest.TestCase):
    def test_book_validates_rating(self) -> None:
        with self.assertRaises(ValueError):
            Book("Автор", "Книга", 6, "2026-01-01")

    def test_stats_calculate_average_and_author_counts(self) -> None:
        books = [
            Book("Автор 1", "Книга 1", 5, "2026-01-01"),
            Book("Автор 1", "Книга 2", 3, "2026-01-02"),
            Book("Автор 2", "Книга 3", 4, "2026-01-03"),
        ]

        self.assertEqual(calculate_average_rating(books), 4.0)
        self.assertEqual(count_books_by_author(books), {"Автор 1": 2, "Автор 2": 1})

    def test_storage_adds_loads_blocks_duplicates_and_deletes_books(self) -> None:
        with TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "books.json"
            book = Book("Автор", "Книга", 5, "2026-01-01")

            self.assertTrue(add_book(book, file_path))
            self.assertFalse(add_book(book, file_path))
            self.assertEqual(load_books(file_path), [book])

            self.assertTrue(delete_book("Автор", "Книга", file_path))
            self.assertEqual(load_books(file_path), [])
            self.assertFalse(delete_book("Автор", "Книга", file_path))


if __name__ == "__main__":
    unittest.main()
