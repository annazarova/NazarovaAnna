class Vehicle:
    def __init__(self, brand, model, year, color):
        self._brand = brand
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def speed(self):
        return self._speed

    def accelerate(self, amount):
        self._speed += amount
        return f"Скорость увеличена на {amount} км/ч"

    def brake(self, amount):
        self._speed = max(0, self._speed - amount)
        return f"Скорость уменьшена на {amount} км/ч"

    def __str__(self):
        return f"{self._color} {self._brand} {self._model} {self._year} года"

    def __repr__(self):
        return f"Vehicle(brand={self._brand}, model={self._model}, year={self._year}, color={self._color})"


class Car(Vehicle):
    def __init__(self, brand, model, year, color, doors_count, fuel_type):
        super().__init__(brand, model, year, color)
        self._doors_count = doors_count
        self._fuel_type = fuel_type
        self._fuel_level = 100

    @property
    def doors_count(self):
        return self._doors_count

    @property
    def fuel_type(self):
        return self._fuel_type

    @property
    def fuel_level(self):
        return self._fuel_level

    def refuel(self, amount):
        self._fuel_level = min(100, self._fuel_level + amount)
        return f"Заправлено {amount} литров"

    def accelerate(self, amount):
        if self._fuel_level <= 0:
            return "Нет топлива"
        self._fuel_level = max(0, self._fuel_level - amount * 0.1)
        return super().accelerate(amount)

    def __str__(self):
        return f"Автомобиль: {super().__str__()}, {self._doors_count} двери, топливо: {self._fuel_type}"


class Truck(Vehicle):
    def __init__(self, brand, model, year, color, load_capacity, axles_count):
        super().__init__(brand, model, year, color)
        self._load_capacity = load_capacity
        self._axles_count = axles_count
        self._current_load = 0

    @property
    def load_capacity(self):
        return self._load_capacity

    @property
    def axles_count(self):
        return self._axles_count

    @property
    def current_load(self):
        return self._current_load

    def load(self, weight):
        if self._current_load + weight > self._load_capacity:
            return "Превышение грузоподъемности"
        self._current_load += weight
        return f"Загружено {weight} тонн"

    def unload(self, weight):
        if weight > self._current_load:
            weight = self._current_load
        self._current_load -= weight
        return f"Разгружено {weight} тонн"

    def accelerate(self, amount):
        if self._current_load > self._load_capacity * 0.8:
            amount = amount * 0.5
        return super().accelerate(amount)

    def __str__(self):
        return f"Грузовик: {super().__str__()}, грузоподъемность: {self._load_capacity}т, загрузка: {self._current_load}т"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, "черный", 4, "бензин")
    truck = Truck("Volvo", "FH16", 2021, "белый", 20, 3)

    print(car)
    print(truck)

    print(car.accelerate(50))
    print(car.refuel(20))

    print(truck.load(15))
    print(truck.accelerate(30))
    print(truck.unload(5))
    