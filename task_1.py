class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = None
        self._author = None
        self.set_name(name)
        self.set_author(author)

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Название должно быть типа str')
        else:
            self._name = name

    def set_author(self, author: str):
        if not isinstance(author, str):
            raise TypeError('Автор должно быть типа str')
        else:
            self._author = author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Число страниц должно быть типа int')
        elif pages <= 0:
            raise ValueError('Число страниц должно быть больше 0')
        else:
            self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Длительность должна быть типа float')
        elif duration <= 0:
            raise ValueError('Длительность должна быть больше 0')
        else:
            self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
