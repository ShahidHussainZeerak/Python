# use calss varible to find circumference of a circle
# from _typeshed import Self


class Circle:
     pi=3.14  # class
     def __init__(self,radius):
        self.radius=radius
     def cal_circumference(self):
        return 2*Circle.pi*self.radius #circumference of circle =2*pi*radius
c1=Circle(10)
print(c1.cal_circumference())

# example 2
class Laptop:
   discount=20
   def __init__(Self,brand,model,price):
      Self.brand=brand
      Self.model=model
      Self.price=price
   def apply_discount(Self):
      off_price=(Self.discount/100)*Self.price
      return Self.price-off_price
l1=Laptop('hp','ab34df',45000)
l2=Laptop('Apple','macbook pro',350000)
l2.discount=40
print(l2.__dict__)
print(l2.apply_discount())


