class Person:
    def __init__(self,first_name,last_name,age):
        #instance varaibles
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
# create object. 
p1=Person("Shahid",'Hussain',21)
p2=Person("Abid",'Hussain',20)
p3=Person("Hashim",'Hussain',11)
print(p1.first_name,p1.last_name,p1.age)
#print(p1.last_name)
print(p2.first_name,p2.last_name,p2.age)
#print(p2.last_name)
print(p3.first_name,p3.last_name,p3.age)
#print(p3.last_name)