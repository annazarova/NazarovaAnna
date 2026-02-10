# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Optional


class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
    title (str): Название книги
    author (str): Автор книги
    pages (int): Количество страниц
    is_available (bool): Доступность книги для выдачи
    """

    def __init__(self, title: str, author: str, pages: int, is_available: bool = True):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц
        :param is_available: Доступность книги (по умолчанию True)

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 671)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title) == 0:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if len(author) == 0:
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        if not isinstance(is_available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = is_available

    def borrow_book(self) -> bool:
        """
        Выдача книги читателю.

        :return: Успешно ли выдана книга
        :raises ValueError: Если книга уже выдана

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.borrow_book()
        True
        """
        if not self.is_available:
            raise ValueError("Книга уже выдана")
        ...

    def return_book(self) -> None:
        """
        Возврат книги в библиотеку.

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
        >>> book.return_book()
        """
        ...

    def get_book_info(self) -> str:
        """
        Получение информации о книге.

        :return: Строка с информацией о книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.get_book_info()
        'Война и мир, Лев Толстой, 1225 стр.'
        """
        ...


class Smartphone:
    """
    Класс, представляющий смартфон.

    Атрибуты:
    brand (str): Бренд смартфона
    model (str): Модель смартфона
    battery_level (int): Уровень заряда батареи в процентах
    is_on (bool): Включен ли смартфон
    """

    def __init__(self, brand: str, model: str, battery_level: int = 100, is_on: bool = False):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_level: Уровень заряда батареи (по умолчанию 100%)
        :param is_on: Включен ли смартфон (по умолчанию False)

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 85)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand) == 0:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if len(model) == 0:
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(battery_level, int):
            raise TypeError("Уровень заряда должен быть целым числом")
        if not 0 <= battery_level <= 100:
            raise ValueError("Уровень заряда должен быть от 0 до 100 процентов")
        self.battery_level = battery_level

        if not isinstance(is_on, bool):
            raise TypeError("Состояние включения должно быть булевым значением")
        self.is_on = is_on

    def turn_on(self) -> bool:
        """
        Включение смартфона.

        :return: Успешно ли включен смартфон
        :raises ValueError: Если батарея разряжена или смартфон уже включен

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 75)
        >>> phone.turn_on()
        True
        """
        if self.battery_level == 0:
            raise ValueError("Невозможно включить: батарея разряжена")
        if self.is_on:
            raise ValueError("Смартфон уже включен")
        ...

    def charge(self, percentage: int) -> None:
        """
        Зарядка смартфона.

        :param percentage: Процент заряда для добавления
        :raises ValueError: Если процент заряда отрицательный или превышает допустимые пределы

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 30)
        >>> phone.charge(50)
        """
        if not isinstance(percentage, int):
            raise TypeError("Процент заряда должен быть целым числом")
        if percentage < 0:
            raise ValueError("Процент заряда не может быть отрицательным")
        ...

    def make_call(self, phone_number: str) -> str:
        """
        Совершение телефонного звонка.

        :param phone_number: Номер телефона
        :return: Состояние звонка
        :raises ValueError: Если номер телефона некорректен или батарея разряжена

        Примеры:
        >>> phone = Smartphone("Google", "Pixel 7", 60, True)
        >>> phone.make_call("+79161234567")
        'Звонок выполняется...'
        """
        if not isinstance(phone_number, str):
            raise TypeError("Номер телефона должен быть строкой")
        if len(phone_number) < 10:
            raise ValueError("Номер телефона слишком короткий")
        ...


class BankAccount:
    """
    Класс, представляющий банковский счет.

    Атрибуты:
    account_number (str): Номер счета
    owner_name (str): Имя владельца счета
    balance (float): Текущий баланс
    currency (str): Валюта счета
    """

    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0, currency: str = "RUB"):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param owner_name: Имя владельца счета
        :param balance: Начальный баланс (по умолчанию 0.0)
        :param currency: Валюта счета (по умолчанию "RUB")

        Примеры:
        >>> account = BankAccount("40817810099910004312", "Иванов Иван Иванович", 15000.50)
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if len(account_number) < 10:
            raise ValueError("Номер счета слишком короткий")
        self.account_number = account_number

        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должно быть строкой")
        if len(owner_name) == 0:
            raise ValueError("Имя владельца не может быть пустым")
        self.owner_name = owner_name

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = float(balance)

        if not isinstance(currency, str):
            raise TypeError("Валюта должна быть строкой")
        if len(currency) != 3:
            raise ValueError("Код валюты должен состоять из 3 символов")
        self.currency = currency.upper()

    def deposit(self, amount: float) -> float:
        """
        Внесение денег на счет.

        :param amount: Сумма для внесения
        :return: Новый баланс
        :raises ValueError: Если сумма для внесения отрицательная или равна нулю

        Примеры:
        >>> account = BankAccount("1234567890", "Петров Петр Петрович", 5000.0)
        >>> account.deposit(1000.0)
        6000.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")
        ...

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия
        :return: Новый баланс
        :raises ValueError: Если сумма превышает баланс или отрицательная

        Примеры:
        >>> account = BankAccount("0987654321", "Сидоров Сидор Сидорович", 10000.0)
        >>> account.withdraw(3000.0)
        7000.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        ...

    def transfer(self, target_account: 'BankAccount', amount: float) -> None:
        """
        Перевод денег на другой счет.

        :param target_account: Целевой счет для перевода
        :param amount: Сумма перевода
        :raises ValueError: Если валюты счетов не совпадают или сумма превышает баланс

        Примеры:
        >>> account1 = BankAccount("1111111111", "Отправитель", 5000.0)
        >>> account2 = BankAccount("2222222222", "Получатель", 1000.0)
        >>> account1.transfer(account2, 2000.0)
        """
        if not isinstance(target_account, BankAccount):
            raise TypeError("Целевой счет должен быть экземпляром класса BankAccount")
        if self.currency != target_account.currency:
            raise ValueError("Валюты счетов должны совпадать")
        ...
    

if __name__ == "__main__":
    doctest.testmod(verbose=True)# TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
