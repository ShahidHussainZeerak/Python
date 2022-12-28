# inheritance..
class Phone:
    def __init__(self,brand,model,_price):
        self.brand=brand
        self.model=model
        self._price=max(_price,0)

    def full_name(self):
        return f"{self.brand} {self.model}"
    def call(self,number):
        return f" calling is {number}..."
class smartphone(Phone):
    def __init__(self, brand, model, _price ,ram,rom):
        super().__init__(brand, model, _price)
        self.ram=ram
        self.rom=rom
class Supersmartphone(Phone): 
    def __init__(self, brand, model, _price,camera):
        super().__init__(brand, model, _price)
        self.camera=camera

p1=smartphone("Apple","x max",80000,"4gb","128 gb")
p2=Supersmartphone("Apple","12 max",180000,"10mp")
# print(p1.full_name())
# print(p1.full_name()+ f" and price is {p1._price}")
print(p2.full_name)


