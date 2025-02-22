class Auto :
    """Базовый класс для всех транспортных средств."""

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует базовый класс транспортного средства.
        brand: Марка транспортного средства.
        model: Модель транспортного средства.
        year: Год выпуска.
        """
        self._brand = brand
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self) -> str:
        """Возвращает детальное представление транспортного средства."""
        return f"Auto(brand='{self._brand}', model='{self._model}', year={self._year})"

    def start_engine(self) -> None:
        """Запускает двигатель транспортного средства."""
        print(f"{self._brand} {self._model} двигатель запущен.")


class Car(Auto):
    """Класс для легковых автомобилей, наследует от Vehicle."""

    def __init__(self, brand: str, model: str, year: int, mass: float) -> None:
        """
        Инициализирует класс легкового автомобиля.
        brand: Марка легкового автомобиля.
        model: Модель легкового автомобиля.
        year: Год выпуска.
        mass: Масса автомобиля в тоннах.
        """
        super().__init__(brand, model, year)
        self._mass = mass
        if mass < 0:
            raise ValueError("Масса не может быть меньше 0.")

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} с массой {self._mass} тонн"

    def __repr__(self) -> str:
        """Возвращает детальное представление легкового автомобиля."""
        return f"Car(brand='{self._brand}', model='{self._model}', year={self._year}, mass={self._mass})"

    def drive(self, speed: int = 0) -> None:
        """ Метод, имитирующий движение автомобиля.

        Если скорость не указана, выводит сообщение о том, что автомобиль движется без указания скорости.
        speed: Скорость движения автомобиля в км/ч. По умолчанию 0.
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной.")

        if speed == 0:
            print(f"{self._brand} {self._model} стоит.")
        else:
            print(f"{self._brand} {self._model} движется со скоростью {speed} км/ч.")


# Пример использования классов
if __name__ == "__main__":
    car = Car("Рено", "Дастер", 2018, 1.4)
    print(car) #Рено Дастер (2018) с массой 1.4 тонн
    print(repr(car)) #Car(brand='Рено', model='Дастер', year=2018, mass=1.4)
    car.start_engine() #Рено Дастер двигатель запущен.
    car.drive() #Рено Дастер стоит.
    car.drive(85) #Рено Дастер движется со скоростью 85 км/ч.
