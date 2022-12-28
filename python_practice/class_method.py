class Person:
    count_instance=0
    def __init__(self,f_name,l_name,age):
        Person.count_instance +=1
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
# use of class method.
    @classmethod  # called decorator used before defining the class method.
    def count_instances(cls):
        return(f"you have created {cls.count_instance} instances of Person class")
# Example 2  Static Method..this has no relation with the class.
    @staticmethod
    def hello():
        print("hello, this is static method :")

p1=Person("Shahid",'Hussain',21)
p2=Person("Abid",'Hussain',20)
print(Person.count_instances())
# Example 2  Static Method
