class Car:
    def __init__(self, make, model, year, odometer_reading=0):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = odometer_reading  # private attribute

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This cas has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Filling the gas tank")

    # Getter for odometer_reading
    def get_odometer_reading(self):
        return self.__odometer_reading

    # Setter for odometer_reading
    def set_odometer_reading(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You cant roll back an odometer")


class ElectricCar(Car):
    def __init__(self, make, model, year, odometer_reading=0, battery_size=75):
        super().__init__(make, model, year, odometer_reading)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_description(self):
        return f"{self.year} {self.make} {self.model} (Electric)"

    def fill_gas_tank(self):
        print("Electric car dont have gas tanks")


car1 = Car("Toyota", "Corolla", 2024, 40)

# car1.update_odometer(50)
# car1.read_odometer()
# car1.increment_odometer(20)
print(car1.get_description())
car1.fill_gas_tank()
car1.set_odometer_reading(90)
print(car1.get_odometer_reading())
# car1.read_odometer()

ev1 = ElectricCar("Tesla", "Model-5", 2024, 80, 100)

print(ev1.get_description())
ev1.describe_battery()
ev1.fill_gas_tank()
