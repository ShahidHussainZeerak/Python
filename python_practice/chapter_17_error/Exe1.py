# Exercise 1.
# a=int(input('enter value of a : '))
# b=int(input('enter value of b : '))
def divide(a,b):
    try:
        return a/b

    except ZeroDivisionError as err: # this is for zero division
        print(err)
    except TypeError as err: # this is for string...when we enter string instead of int.
        print(err)
   
print(divide(10,0))
print(divide(10,'2'))