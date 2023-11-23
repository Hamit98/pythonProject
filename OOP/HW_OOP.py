class Car:

    count = 0

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Car.count += 1

    def start(self):
        print(f"{self.make} {self.model} has started.")

    def stop(self):
        print(f"{self.make} {self.model} has stopped.")

    def honk(self):
        print(f"{self.make} {self.model} is honking.")

    @classmethod
    def get_total_count(cls):
        return cls.count


class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.make} {self.model} is charging.")


car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Ford", "Mustang", 2023, "Red")

electric_car1 = ElectricCar("Tesla", "Model S", 2023, "Silver", 100)
electric_car2 = ElectricCar("Nissan", "Leaf", 2022, "White", 80)


car1.start()
electric_car1.charge()

total_car_count = Car.get_total_count()
print(f"Общее количество созданных объектов класса Car: {total_car_count}")