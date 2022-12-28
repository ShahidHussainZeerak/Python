# create a laptop class with attributes like brand name ,model  name ,price etc...
# crerate two instance/object of your.
class Laptop:
    def __init__(self,brand_name,model_name,price):
        #instance Variable
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
# Exercise 2...define a method for discount.
    def percentage(self,num):
        off_price=(num/100)*self.price
        return self.price-off_price
l1=Laptop("HP","DESKTOP-NV8JEB7",45000)
print(l1.brand_name,", ",l1.model_name,",",l1.price)
l2=Laptop('apple','macbook pro',330000)
print(l1.percentage(10))
print(l2.percentage(20)) 