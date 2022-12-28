# check where the number is prime or not.
def prime_num(num):
    if num>1:
        for i in range (2,num):
            if (num%i==0)  :#or (num%num==1):
                return False
        
            else:
             return True
    else:
        print("it is not a prime number")
    
num=int(input("Enter your number : "))
print(prime_num(num))
    

