# oop/book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = int(year)

    def __del__(self):
        # print exactly as specified
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        # human-friendly
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # recreate-able
        return f"Book('{self.title}', '{self.author}', {self.year})"
