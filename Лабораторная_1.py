import doctest


class Meat:
    """
    Документация на класс.
    Класс описывает мясо в магазине.
    """

    def __init__(self, packs: int, time_in_stock: int):
        """
        Создание и подготовка к работе объекта "Мясо".

        :param packs: Количество пачек на складе
        :param time_in_stock: Время хранения на складе (в днях)
        :return: None

        Пример:
        >>> meat = Meat(500, 2)
        >>> meat.packs
        500
        """

        if not isinstance(packs, int):
            raise TypeError("Количество пачек должно быть целым числом!")
        if packs <= 0:
            raise ValueError("Количество пачек должно быть положительным!")
        self.packs = packs

        if not isinstance(time_in_stock, int):
            raise TypeError("Время хранения должно быть целым числом!")
        if time_in_stock <= 0:
            raise ValueError("Время хранения должно быть положительным!")
        self.time_in_stock = time_in_stock

    def add_time(self, days: int) -> None:
        """
        Увеличивает количество дней хранения мяса на складе.

        :param days: Количество добавляемых дней
        :return: None

        Пример:
        >>> meat = Meat(100, 5)
        >>> meat.add_time(3)
        >>> meat.time_in_stock
        8
        """

        if not isinstance(days, int):
            raise TypeError("Количество дней должно быть целым числом!")
        if days <= 0:
            raise ValueError("Количество дней должно быть положительным!")

        self.time_in_stock += days

    def print_info(self) -> None:
        """
        Выводит информацию о мясе в консоль.

        :return: None

        Пример:
        >>> meat = Meat(10, 2)
        >>> meat.print_info()
        10 2
        """
        print(self.packs, self.time_in_stock)


class Book:
    """
    Документация на класс.
    Класс описывает книгу в библиотеке.
    """

    def __init__(self, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param author: Автор книги
        :param pages: Количество страниц
        :return: None

        Пример:
        >>> book = Book("Пушкин А. С.", 500)
        >>> book.pages
        500
        """

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой!")
        if author == "":
            raise ValueError("Имя автора не может быть пустым!")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом!")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным!")
        self.pages = pages

    def add_pages(self, extra_pages: int) -> None:
        """
        Увеличивает количество страниц книги.

        :param extra_pages: Количество добавляемых страниц
        :return: None

        Пример:
        >>> book = Book("Пушкин А. С.", 500)
        >>> book.add_pages(20)
        >>> book.pages
        520
        """

        if not isinstance(extra_pages, int):
            raise TypeError("Количество страниц должно быть целым числом!")
        if extra_pages <= 0:
            raise ValueError("Добавляемые страницы должны быть положительными!")

        self.pages += extra_pages

    def print_info(self) -> None:
        """
        Выводит информацию о книге в консоль.

        :return: None

        Пример:
        >>> book = Book("Пушкин А. С.", 500)
        >>> book.print_info()
        Автор: Пушкин А. С.
        Страниц: 500
        """
        print("Автор:", self.author)
        print("Страниц:", self.pages)


class Phone:
    """
    Документация на класс.
    Класс описывает телефон в магазине электроники.
    """

    def __init__(self, brand: str, price: int):
        """
        Создание и подготовка к работе объекта "Телефон".

        :param brand: Название бренда телефона
        :param price: Цена телефона
        :return: None

        Пример:
        >>> phone = Phone("Samsung", 50000)
        >>> phone.price
        50000
        """

        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой!")
        if brand == "":
            raise ValueError("Название бренда не может быть пустым!")
        self.brand = brand

        if not isinstance(price, int):
            raise TypeError("Цена должна быть целым числом!")
        if price <= 0:
            raise ValueError("Цена должна быть положительной!")
        self.price = price

    def discount(self, percent: int) -> None:
        """
        Делает скидку на телефон.

        :param percent: Процент скидки (1–99)
        :return: None

        Пример:
        >>> phone = Phone("Samsung", 50000)
        >>> phone.discount(10)
        >>> phone.price
        45000
        """

        if not isinstance(percent, int):
            raise TypeError("Процент скидки должен быть целым числом!")
        if percent <= 0 or percent >= 100:
            raise ValueError("Скидка должна быть от 1 до 99 процентов!")

        self.price -= self.price * percent // 100

    def print_info(self) -> None:
        """
        Выводит информацию о телефоне в консоль.

        :return: None

        Пример:
        >>> phone = Phone("Samsung", 50000)
        >>> phone.print_info()
        Бренд: Samsung
        Цена: 50000 руб.
        """
        print("Бренд:", self.brand)
        print("Цена:", self.price, "руб.")


if __name__ == "__main__":
    doctest.testmod()
