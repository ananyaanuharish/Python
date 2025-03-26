# class constructor and user defined method
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

obj1 = Car("Lamborghini","Carmy")
obj1.display_info()