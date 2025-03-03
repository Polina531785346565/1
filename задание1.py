
class Flash:
    def __init__(self, memory: float, free: float):
        """
             Создание и подготовка к работе объекта "Флешка"
             :param memory: Объем памяти флешки
             :param free: Объем свободной памяти
             Примеры:
             >>> flash = Flash(16, 9.8)  # инициализация экземпляра класса
             """
        if not isinstance(memory, (int, float)):
            raise TypeError("Объем памяти должен быть типа int или float")
        if memory <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.memory = memory

        if not isinstance(free, (int, float)):
            raise TypeError("Объем свободной памяти должен быть int или float")
        if free < 0:
            raise ValueError("Объем свободной памяти не может быть отрицательным числом")
        self.free = free

    def use_memory(self, amount: float):
        """
        Использовать определенное количество памяти на флешке

        :param amount: Объем памяти, который нужно использовать
        ValueError: Если amount больше доступной свободной памяти
        Примеры:
        >>> flash = Flash(16, 9.8)
        >>> flash.use_memory(5)
        >>> flash.free()
        4.8
        """
        if amount > self.free:
            raise ValueError("Недостаточно свободной памяти для выполнения этой операции")
        self.free -= amount

    def get_free_memory(self) -> float:
        """
        Получить объем свободной памяти

        :return: Объем свободной памяти
        Примеры:
        >>> flash = Flash(16, 9.8)
        >>> flash.get_free_memory()
        9.8
        """
        return self.free


if __name__ == "__main__":
    import doctest
    doctest.testmod()




class Furnitue:
    def __init__(self, material: str, weight: float, height: float):
        """
            Создание и подготовка к работе объекта "Мебель"
            :param material : Материал
            :param weight: Вес мебели
            :param height: Размер мебели
            Примеры:
            >>> furnitue = Furnitue(дерево, 9.8, 8)  # инициализация экземпляра класса
            """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес должен быть больше нуля.")
        if not isinstance(height, (int, float)):
            raise TypeError("Размер должен быть типа int или float")
        if height <= 0:
            raise ValueError("Размер должен быть больше нуля.")
        self.material = material
        self.weight = weight
        self.height = height

    def installation(self, size: float):
        """
        Поставить мебель в определенное место

        :param size: Габариты места
        ValueError: Если height больше доступного свободного места
        Примеры:
        >>> furnitue = Furnitue(дерево, 9.8, 8)
        >>> furnitue.installation(10)
        >>> furnitue.free()
        2
        """
        if 0 > self.free:
            raise ValueError("Недостаточно свободного места для выполнения этой операции")
        self.free = self.size-self.height

    def get_weight(self) -> float:
        """
        Получить вес мебели

        :return: Вес мебели
        Примеры:
        >>> furnitue = Furnitue(дерево, 9.8, 8)
        >>> furnitue.get_weight()
        9.8
        """
        return self.weight


if __name__ == "__main__":
    import doctest
    doctest.testmod()
