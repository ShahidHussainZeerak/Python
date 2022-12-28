def perfect_num(num):
    count=0
    for i in range (1,num):
        if (num%i==0):
            count +=i
    return count==num
#num=int("enter your number : ")
print(perfect_num(28))