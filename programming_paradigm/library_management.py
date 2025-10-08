# programming_paradigm/library_management.py

class Book:
    """Represents a book with a title/author and checkout state."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title            # public
        self.author = author          # public
        self._is_checked_out = False  # private-ish flag

    # --- small helpers ---
    def is_available(self) -> bool:
        return not self._is_checked_out

    def check_out(self) -> bool:
        """Mark the book as checked out. Return True if it succeeded."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """Mark the book as returned. Return True if it succeeded."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    """Holds a collection of Book objects and basic operations."""

    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def _find_by_title(self, title: str) -> Book | None:
        for b in self._books:
            if b.title == title:
                return b
        return None

    def check_out_book(self, title: str) -> bool:
        """Check out a book by title. Returns True if successful."""
        book = self._find_by_title(title)
        return book.check_out() if book else False

    def return_book(self, title: str) -> bool:
        """Return a book by title. Returns True if successful."""
        book = self._find_by_title(title)
        return book.return_book() if book else False

    def list_available_books(self) -> None:
        """Print each available book as 'Title by Author' (one per line)."""
        for b in self._books:
            if b.is_available():
                print(str(b))
