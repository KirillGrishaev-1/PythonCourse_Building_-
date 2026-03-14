class Automobile:
    """Базовый класс для всех автомобилей."""

    def __init__(self, brand: str, mass: int, color: str) -> None:
        """Создаёт автомобиль с указанной маркой, массой и цветом."""
        self.brand = brand
        self.mass = mass
        self.color = color

    def move(self) -> str:
        """Возвращает общее описание движения автомобиля."""
        return f"{self.brand} automobile is moving"

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"Automobile {self.color} {self.brand} with mass {self.mass}"

    def __repr__(self) -> str:
        """Возвращает техническое представление объекта."""
        return f"Automobile('{self.brand}', {self.mass}, '{self.color}')"


class Car(Automobile):
    """Класс легкового автомобиля."""

    def __init__(self, brand: str, mass: int, color: str, passengers: int) -> None:
        """Создаёт легковой автомобиль с заданным количеством пассажиров."""
        super().__init__(brand, mass, color)
        self.passengers = passengers

    def move(self) -> str:
        """
        Перегруженный метод движения.

        Причина перегрузки:
        Для легкового автомобиля важно учитывать количество пассажиров,
        поэтому метод возвращает более конкретное описание движения.
        """
        return f"Car {self.brand} is moving with {self.passengers} passengers"

    def __repr__(self) -> str:
        """
        Перегруженный метод repr.

        Причина перегрузки:
        В классе Car появляется новый атрибут passengers,
        поэтому необходимо изменить строковое представление объекта.
        """
        return f"Car('{self.brand}', {self.mass}, '{self.color}', {self.passengers})"


class Truck(Automobile):
    """Класс грузового автомобиля."""

    def __init__(self, brand: str, mass: int, color: str, max_load: int) -> None:
        """Создаёт грузовой автомобиль с указанной грузоподъёмностью."""
        super().__init__(brand, mass, color)
        self.max_load = max_load

    def move(self) -> str:
        """
        Перегруженный метод движения.

        Причина перегрузки:
        Для грузового автомобиля важно учитывать грузоподъёмность,
        поэтому описание движения включает информацию о перевозимом грузе.
        """
        return f"Truck {self.brand} is moving with {self.max_load} kg"

    def __repr__(self) -> str:
        """
        Перегруженный метод repr.

        Причина перегрузки:
        В грузовом автомобиле появляется новый атрибут max_load,
        поэтому необходимо изменить представление объекта.
        """
        return f"Truck('{self.brand}', {self.mass}, '{self.color}', {self.max_load})"


if __name__ == "__main__":
    car1 = Car("KIA", 2750, "blue", 5)
    truck1 = Truck("Scania", 7500, "red", 40000)

    print(car1)
    print(truck1)

    print(car1.move())
    print(truck1.move())