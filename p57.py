from abc import ABC, abstractmethod
import os
os.system('cls')
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Barks"
    
class Cat(Animal):
    def sound(self):
        return "Meows"
    
dog = Dog()
print(dog.sound())