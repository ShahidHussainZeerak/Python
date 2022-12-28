class Person:
    count_instance=0
    def __init__(self,f_name,l_name,age):
        Person.count_instance +=1
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(",")
        return cls (first,last,age)
    def full_name(self):
        return((f"{self.f_name} {self.l_name}"))

p1=Person("Shahid",'Hussain',21)
p2=Person("Abid",'Hussain',20)
p3=Person.from_string('shahid,Hussain,21')
print(p3.full_name())