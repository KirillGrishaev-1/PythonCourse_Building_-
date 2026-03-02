class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    def author(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # вызов setter

    def __str__(self):
        return f"Бумажная книга '{self.name}', автор {self.author}, {self.pages} стр."
    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError("pages должно быть целым числом")
        if pages <= 0:
            raise ValueError("pages должно быть больше 0")
        self._pages = pages

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # вызов setter

    def __str__(self):
        return f"Аудиокнига '{self.name}', автор {self.author}, {self.duration} ч."
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (int, float)):
            raise TypeError("duration должно быть числом")
        if duration <= 0:
            raise ValueError("duration должно быть больше 0")
        self._duration = float(duration)
