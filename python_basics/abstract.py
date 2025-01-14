from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        return "burk"

# an instance of dog calss
dog1 = dog()
print(dog1.sound())


