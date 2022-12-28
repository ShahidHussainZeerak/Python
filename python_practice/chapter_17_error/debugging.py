# debugging... pdb laibrary.
import pdb
pdb.set_trace()
name=input("enter your name : ")
age=input("enter your age : ")
print(f"hello {name} your age is {age}")

#age2=age+5   # this will create eeror b/c we can't add string and int... so to solve this problem we use pdb
age2=int(age)+5
print(f"hello {name} your age will be {age2} in next five years")