# find the devisor of a number in python.
def devisor(num):
    l=[]
    for i in range(1,num):
        if num%i==0:
            l.append(i)
    return l
num=int(input("enter your number :"))
print(devisor(num))

