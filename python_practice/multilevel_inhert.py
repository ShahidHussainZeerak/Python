# Multilevel inheritance.
from inheritance import smartphone


class Phone:
    def __init__(self,brand,model,_price):
        self.brand=brand
        self.model=model
        self._price=max(_price,0)

    def full_name(self):
        return f"{self.brand} {self.model}"
    def call(self,number):
        return f" calling is {number}..."
class Smartphone(Phone): # child calss of phone.
    def __init__(self, brand, model, _price ,ram,rom):
        super().__init__(brand, model, _price)
        self.ram=ram
        self.rom=rom
class Supersmartphone(Smartphone):   # child class of smartphone.
    def __init__(self, brand, model, _price, ram, rom,f_camera,b_camera):
        super().__init__(brand, model, _price, ram, rom)
        self.f_camera=f_camera
        self.b_camera=b_camera
p1=Supersmartphone("Apple","x max",80000,"4gb","128 gb","15mp","10mp")
print(p1.full_name())
#print(help(Supersmartphone))
print(isinstance(p1,Supersmartphone))
print(issubclass(Supersmartphone,Phone))
print(help(Supersmartphone))