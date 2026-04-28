class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self._author = author
        self._year = year

    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year})'