```python
from publication import Publication


class Magazine(Publication):
    def __init__(self, title, editor, year, issue_number, category):
        super().__init__(title, editor, year)
        self.issue_number = issue_number
        self.category = category

    def get_info(self):
        return f'"{self.title}" (Ред. {self._author}, {self._year}), Выпуск №{self.issue_number}, категория: {self.category}'