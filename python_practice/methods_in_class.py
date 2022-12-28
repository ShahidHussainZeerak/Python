# Methods in a class.
class Person:
    def __init__(self,first_name,last_name,age):
        #instance varaibles
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self): # full _name method self making.
        return(f"{self.first_name} {self.last_name}")
    def is_above(self): # age method to check age .
        return self.age>18
p1=Person("Shahid",'Hussain',21)
p2=Person("Abid",'Hussain',20)
p3=Person("Hashim",'Hussain',11)
print(p1.full_name())
print(p1.is_above())
print(p3.is_above())

# Example 2
# methods of list.
l=[1,2,3,4]
l.append(5)
print(l)
l.pop()
print(l)
l.clear()
print(l)