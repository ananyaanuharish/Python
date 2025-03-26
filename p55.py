# Inheritance in python
class Vehicle:
    def __init__(self, brand):
        self.brand=brand

    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model=model

    def show_details(self):
        print(f"Car Model: {self.model}")

car_obj = Car("Honda","Civic")
car_obj.show_brand()
car_obj.show_details()