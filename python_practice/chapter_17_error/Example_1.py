# NotImplmentedErrors....This error is raised only when we use inheritance.
# Abstruct method.
from typing import ClassVar


class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self): # if the sound methofd not present in the dog and cat class so this error  will be raise. 
        raise NotImplementedError('you ahve to define this method in subclass')
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "blow blow"
class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return " meo meo"
d=Dog("papo",'germanshiperd')
c=Cat("mano","asli")
print(d.breed)
print(d.sound())
print("**************")
print(c.name)
print(c.sound())