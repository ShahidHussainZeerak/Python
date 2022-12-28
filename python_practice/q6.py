def prime_num(num):
    for i in range(2,num):
        if (num%i==0):
            return False
    else:
        return True
num=int(input("enter your number : "))
print(prime_num(num))
