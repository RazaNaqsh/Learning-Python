class Car:
    def __init__(self,make,model,year,odometer_reading=0):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = odometer_reading
        
    def get_description(self):
        return (f'{self.year} {self.make} {self.model}')
    
    def read_odometer(self):
        print(f'This cas has {self.odometer_reading} miles on it')
    
car1 = Car('Toyota','Corolla',2024,40)
print(car1.get_description())
car1.read_odometer()