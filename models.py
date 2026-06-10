from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Book:
    """Book read by the user."""

    author: str
    title: str
    rating: int
    read_date: str

    def __post_init__(self) -> None:
        author = self.author.strip()
        title = self.title.strip()
        read_date = self.read_date.strip()

        if not author:
            raise ValueError("Автор не может быть пустым")
        if not title:
            raise ValueError("Название не может быть пустым")
        if not 1 <= int(self.rating) <= 5:
            raise ValueError("Оценка должна быть целым числом от 1 до 5")

        try:
            datetime.strptime(read_date, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Дата прочтения должна быть в формате ГГГГ-ММ-ДД") from exc

        object.__setattr__(self, "author", author)
        object.__setattr__(self, "title", title)
        object.__setattr__(self, "rating", int(self.rating))
        object.__setattr__(self, "read_date", read_date)

    def to_dict(self) -> dict[str, str | int]:
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "read_date": self.read_date,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str | int]) -> "Book":
        return cls(
            author=str(data["author"]),
            title=str(data["title"]),
            rating=int(data["rating"]),
            read_date=str(data["read_date"]),
        )
