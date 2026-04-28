from book import Book
from magazine import Magazine


book = Book(
    "Война и мир",
    "Лев Толстой",
    1869,
    "978-5-389-06254-2",
    1225
)

magazine = Magazine(
    "National Geographic",
    "Сьюзан Голдберг",
    2021,
    8,
    "Наука"
)

publications = [book, magazine]

for publication in publications:
    print(publication.get_info())

print(book.read_pages(100))
print(book.read_pages(50))