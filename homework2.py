from datetime import date


class LibraryBook:

    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self._unavailable_since = None if available else date.today()


