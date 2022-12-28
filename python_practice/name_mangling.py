# Encapsulation,Abstraction method, Naming convention, Name Mangling.
class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price=price 
    def make_a_call(self,phone_Number):
        return(f"calling {phone_Number}...")
    def full_name(self):
        return(f"{self.name} {self.model}")
p1=Phone("Apple","13 ",390000)
print(p1._price)
p1.Phone_price=-20000
print(p1.Phone_price)
print(p1.__dict__)  # data descriptor ...to check how many attributes of in instance.

    