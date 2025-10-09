# oop/book_class.py

class Book:
    def __init__(self, title, author, year):
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __del__(self):
        # print exactly as the checker expects
        print(f"Deleting {self.title}")

    def __str__(self):
        # human-friendly text
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # recreate-able representation
        return f"Book('{self.title}', '{self.author}', {self.year})"
