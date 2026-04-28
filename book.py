from publication import Publication


class Book(Publication):
    def __init__(self, title, author, year, isbn, pages):
        super().__init__(title, author, year)
        self.isbn = isbn
        self.pages = pages
        self.read_pages_count = 0

    def read_pages(self, count):
        if count <= 0:
            return "Количество страниц должно быть больше 0"

        if self.read_pages_count + count > self.pages:
            self.read_pages_count = self.pages
            return "Книга дочитана до конца"

        self.read_pages_count += count
        return f"Прочитано страниц: {self.read_pages_count}"

    def get_info(self):
        return f'{super().get_info()}, ISBN: {self.isbn}, страниц: {self.pages}'