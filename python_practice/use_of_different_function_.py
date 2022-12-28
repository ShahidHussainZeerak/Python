# how to sum a list.
l=[20,39,99,40,77,58]
print(sum(l))
# how to use for loop with giving a start,last and step key words value..
lst=[]
start=0
stop=50
step=2
for i in range(start,stop,step):
    lst.append(i)
print(lst)
# in function after return we can not use any things because it does not work once we return something.
x1=10
x2=30
def abc(x):
    if x%2==0:
        return x1+x
        x2= x2+x  # does not work because after return nothing will be executed.
    else:
        return x-1
        x2=x2-x # not working.
print(abc(10))
# * It  is used to pass a variable number of arguments to a function, it is mostly used to pass a non-key argument and variable-length argument list.
def sum_l(*a):
    
    return sum(*a)
print(sum([5,6,7,12,34,5]))

#
def multiply(x,y,z):
    return multiply(x,y,z)
print(multiply(5,5,6))



