from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class EnginePower(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(EnginePower, Vehicle):
    def __init__(self, model, make):
        self.model = model
        self.make = make
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            print(f"Engine of {self.make} {self.model} started")
        else:
            print(f"Engine is already runnig in {self.make} {self.model}")

    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            print(f"Engine of {self.make} {self.model} stopped")
        else:
            print(f"Engine is already off in {self.make} {self.model}")
            
    def move(self):
        if self.engine_started:
            print(f"{self.make} {self.model} is moving.")
        else:
            print(f"Start the engine first to move the {self.make} {self.model}")
        
    def stop(self):
         print(f"{self.make} {self.model} has stopped.")  
         
car = Car("Model S", "Tesla")
car.start_engine()
car.stop_engine()
car.move()
car.stop()