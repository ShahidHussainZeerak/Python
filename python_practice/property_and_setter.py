class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price= max(price,0) #this is technique used if we give price in negative then the max will zero price auotomatically. 
    @property
    def complete_specification(self):
        return f"{self.name} {self.model} and price is {self._price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        return slice._price == max(new_price,0)
    def make_a_call(self,phone_Number):
        return(f"calling {phone_Number}...")
    def full_name(self):
        return(f"{self.name} {self.model}")
    
p1=Phone("Apple","13 ",390000)
print(p1._price)
p1._price=-20000
print(p1.complete_specification)