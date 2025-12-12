class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")
    
    
class Electric:
    def __init__(self, battery_size,battery_model):
        self.battery_size = battery_size
        self.Battery_model = battery_model
    
    def display__info(self):
        print(f"Battery Size: {self.battery_size} kWh")
    
class ELectricCar(Vehicle, Electric):
    def __init__(self, make, model, battery_size, battery_model):
        # super().__init__(make, model) #vehicle
        Vehicle.__init__(self, make,model)
        Electric.__init__(self, battery_size,battery_model)
    
    def display_info(self):
        # print(f"ELectricCar=> Vehicle: {self.make} {self.model}")
        # print(f"ELectricCar=> Battery Size: {self.battery_size} kWh")
        # super().display_info()  #left most parent
        
        Vehicle.display_info(self)
        Electric.display__info(self)


ecar = ELectricCar("Tesla", "3", 75, "Lithium")
print(f"Ecar model => {ecar.Battery_model}")
ecar.display_info()