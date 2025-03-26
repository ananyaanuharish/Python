# Polymorphism in python
class dog:
    def sound(self):
        return "bark"
    
class cat:
    def sound(self):
        return "meow"
    
def animal_sound(animal):
    print(animal.sound())

Dog = dog()
Cat = cat()

animal_sound(Dog)
animal_sound(Cat)