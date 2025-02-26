class User:
    def __init__(self, username: str, email: str):
        """
        Класс, описывающий пользователя некоторой системы

        :param username: Ник пользователя
        :param email: Электронная почта пользователя

        """
        self._username = None
        self._email = None
        self.set_username(username)
        self.set_email(email)

    def __str__(self) -> str:
        """
        Метод для вывода строки с атрибутами

        :return: Вывод строки с атрибутами
        """
        return f'Пользователь: {self._username!r}, email: {self._email!r}'

    def __repr__(self) -> str:
        """
        Метод для вывода валидной строки для инициализации экземпляра

        :return: Вывод валидной строки для инициализации экземпляра
        """
        return f'{self.__class__.__name__}(username={self._username!r}, email={self._email!r})'

    def set_username(self, new_username) -> None:
        """
        Метод для проверки вводимого ника

        :param new_username: присваиваемый ник

        :raise TypeError: Ник должен быть представлен типом str
        """
        if not isinstance(new_username, str):
            raise TypeError('Ник пользователя должен быть типа str')
        else:
            self._username = new_username

    def set_email(self, new_email) -> None:
        """
        Метод для проверки вводимого имейла

        :param new_email: присваиваемый имейл

        :raise TypeError: Имейл должен быть представлен типом str
        """
        if not isinstance(new_email, str):
            raise TypeError('Почта пользователя должна быть типа str')
        else:
            self._email = new_email

    def start_session(self) -> str:
        """
        Метод, запускающий сессию в системе

        :return: Сообщение о запуске сессии
        """
        return f'Сессия для пользователя {self._username} запущена'

    def end_session(self) -> str:
        """
        Метод, завершающий сессию в системе

        :return: Сообщение о завершении сессии
        """
        return f'Сессия {self._username} завершена'


class Admin(User):
    def __init__(self, username: str, email: str, access_level: str):
        """
        Класс, описывающий пользователя типа "Администратор" в некоторой системе

        :param username: Ник, наследуется из класса User
        :param email: Почта, наследуется из класса User
        :param access_level: Уровень доступа
        """
        super().__init__(username, email)
        self._access_level = None
        self.__set_access_level(access_level)
        self._password = None

    def __repr__(self) -> str:
        """
        Перегрузка магического метода в связи с изменениями
           в вызове экземпляра Admin по сравнению с User

        :return: строка, показывающая как будет инициализирован экземпляр
        """
        return (f'{self.__class__.__name__}(username={self._username!r}, email={self._email!r}, '
                f'access_level={self._access_level!r})')

    def __set_access_level(self, new_access_level: int) -> None:
        """
        Непубличный метод для присваивания введенного уровня доступа.
        Инкапсулирован для ограничения доступа извне.

        :param new_access_level: присваиваемый уровень доступа

        :raise TypeError: Уровень доступа должен быть представлен типом int
        """
        if not isinstance(new_access_level, int):
            raise TypeError('Почта пользователя должна быть типа int')
        elif new_access_level < 1 or new_access_level > 3:
            raise ValueError('Уровень доступа не может быть меньше 1 или больше 3')
        else:
            self._access_level = new_access_level

    def start_session(self) -> str:
        """
        Перегрузка метода start_session в дочернем классе

        :return: сообщение о запуске сессии и уровне доступа
        """
        return f'Сессия для администратора {self._username} запущена, уровень доступа: {self._access_level}'


if __name__ == "__main__":
    user1 = User('Ivan Ivanov', 'ivanov91@mail.ru')  # инициализация пользователя класса User
    print(user1)  # проверка __str__
    print(repr(user1))  # проверка __repr__
    print(user1.start_session())  # проверка метода класса User
    print(user1.end_session())  # проверка метода класса User
    user2 = Admin('Petr Petrov', 'ppetrov85@yandex.ru', 2)  # инициализация пользователя класса Admin
    print(user2)  # проверка наследования __str__
    print(repr(user2))  # проверка перегрузки __repr__
    print(user2.start_session())  # проверка перегрузки метода базового класса
    print(user2.end_session())  # проверка наследования метода базового класса

