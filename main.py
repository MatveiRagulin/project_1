from models import Book
from stats import calculate_average_rating, count_books_by_author
from storage import add_book, delete_book, load_books


MENU = """
1. Добавить книгу
2. Показать все книги
3. Показать среднюю оценку
4. Статистика по авторам
5. Удалить книгу
6. Выход
"""


def input_rating() -> int:
    while True:
        value = input("Оценка (1-5): ").strip()
        if value.isdigit() and 1 <= int(value) <= 5:
            return int(value)

        print("Введите целое число от 1 до 5.")


def add_book_from_input() -> None:
    author = input("Автор: ")
    title = input("Название: ")
    rating = input_rating()
    read_date = input("Дата прочтения (ГГГГ-ММ-ДД): ")

    try:
        book = Book(author=author, title=title, rating=rating, read_date=read_date)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    if add_book(book):
        print("Книга добавлена.")
    else:
        print("Такая книга уже есть в списке.")


def show_all_books() -> None:
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. {book.author} — {book.title}, "
            f"оценка: {book.rating}, дата: {book.read_date}"
        )


def show_average_rating() -> None:
    average_rating = calculate_average_rating(load_books())
    print(f"Средняя оценка: {average_rating}")


def show_author_statistics() -> None:
    statistics = count_books_by_author(load_books())
    if not statistics:
        print("Статистика пока недоступна: список книг пуст.")
        return

    for author, count in sorted(statistics.items()):
        print(f"{author}: {count}")


def delete_book_from_input() -> None:
    author = input("Автор книги для удаления: ")
    title = input("Название книги для удаления: ")

    if delete_book(author, title):
        print("Книга удалена.")
    else:
        print("Книга не найдена.")


def main() -> None:
    actions = {
        "1": add_book_from_input,
        "2": show_all_books,
        "3": show_average_rating,
        "4": show_author_statistics,
        "5": delete_book_from_input,
    }

    while True:
        print(MENU)
        choice = input("Выберите пункт меню: ").strip()

        if choice == "6":
            print("До свидания!")
            break

        action = actions.get(choice)
        if action is None:
            print("Нет такого пункта меню.")
            continue

        action()


if __name__ == "__main__":
    main()
