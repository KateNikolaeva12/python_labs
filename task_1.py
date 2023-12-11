import doctest


class Computer:
    def __init__(self, ram: int, cores: int):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param ram: Количество оперативной памяти
        :param cores: Количество ядер

        Примеры:
        >>> rocket = Computer(16, 4)  # инициализация экземпляра класса
        """
        if not isinstance(ram, int):
            raise TypeError("Количество оперативной памяти должно быть типа int")
        if ram <= 0:
            raise ValueError("Количество оперативной памяти должно быть положительным числом")
        self.ram = ram

        if not isinstance(cores, int):
            raise TypeError("Количество ядер должно быть int")
        if cores <= 0:
            raise ValueError("Количество ядер должно быть положительным числом")
        self.cores = cores

    def add_ram_to_computer(self, plus_ram: int) -> None:
        """
        Добавление оперативной памяти в компьютер.
        :param plus_ram: Объем добавляемой памяти

        :raise ValueError: Если количество добавляемой памяти отрицательно, вызываем ошибку

        Примеры:
        >>> computer = Computer(16, 4)
        >>> computer.add_ram_to_computer(16)
        """
        if not isinstance(plus_ram, int):
            raise TypeError("Добавляемая память должна быть типа int")
        if plus_ram < 0:
            raise ValueError("Добавляемая память должна положительным числом")
        ...

    def remove_ram_from_computer(self, minus_ram: int) -> None:
        """
        Уменьшения оперативной памяти.

        :param minus_ram: отбираемая память
        :raise ValueError: Если уменьшение памяти превышает текущую память, вызываем ошибку

        :return: Уменьшенная память

        Примеры:
        >>> computer = Computer(16, 4)
        >>> computer.remove_ram_from_computer(8)
        """
        ...


class Website:
    def __init__(self, days: int, users: int):
        """
        Создание и подготовка к работе объекта "Сайт"

        :param days: Временной отрезок (дни)
        :param Users: Количество пользователей, зашедших на сайт за этот временной промежуток

        Примеры:
        >>> website = Website(7, 450)  # инициализация экземпляра класса
        """
        if not isinstance(days, int):
            raise TypeError("Дни должны быть типа int")
        if days <= 0:
            raise ValueError("Дни должны быть больше нуля")
        self.days = days

        if not isinstance(users, int):
            raise TypeError("Количество пользователей должно быть int")
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом")
        self.users = users

    def users_in_day(self) -> float:
        """
        Определение среднего количества пользователей в день

        :return: Среднее кол-во пользователей в день

        Примеры:
        >>> website = Website(7, 490)
        >>> website.users_in_day()
        """
        ...

    def nobody(self) -> bool:
        """
        Функция которая проверяет, заходил ли кто на сайт

        :return: Были ли посетители

        Примеры:
        >>> website = Website(10, 0)
        >>> website.nobody()
        """
        ...


class Ice_rink:
    def __init__(self, people: int, square: (int, float)):
        """
        Создание и подготовка к работе объекта "Каток"

        :param people: Количество людей
        :param square: Площадь катка

        Примеры:
        >>> ice_rink = Ice_rink(50, 1000)  # инициализация экземпляра класса
        """
        if not isinstance(people, int):
            raise TypeError("Количество людей должно быть типа int")
        if people < 0:
            raise ValueError("Количество людей не должно быть отицательным")
        self.people = people

        if not isinstance(square, (int, float)):
            raise TypeError("Площадь катка должна быть int или float")
        if square <= 0:
            raise ValueError("Площадь катка должна быть положительным числом")
        self.square = square

    def density(self) -> float:
        """
        Функция определяет количество людей на единицу площади

        :return: Количество количество людей на единицу площади

        Примеры:
        >>> ice_rink = Ice_rink(50, 1000)
        >>> ice_rink.density()
        """
        ...

    def remove_people(self, minus_peopie) -> None:
        """
        Уменьшение людей на катке.
        :param minus_peopie: Количество убираемых людей
        :raise ValueError: Если количество людей отрицательно, то вызываем ошибку

        Примеры:
        >>> ice_rink = Ice_rink(50, 1000)
        >>> ice_rink.remove_people(25)
        """
        if not isinstance(minus_peopie, int):
            raise TypeError("Убираемые люди должны быть типа int")
        if minus_peopie < 0:
            raise ValueError("Убираемые люди должны быть не отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

