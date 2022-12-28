# Define a function that accepts 2 values and return its sum, subtraction and multiplication.
def fun(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    return (sum,sub,mul)
x=int(input("enter your number X : "))
y=int(input("enter your number Y : "))
print(fun(x,y))

#2: Define a function that accepts roll number and returns whether the student is present or absent
def roll(a):
    l=[1,10,11,13,15,18]
    if a in l:
        print("value of a:",a)
    else:
        print(" a is  not present")
    return a
a=int(input(" enter value of A :"))
(roll(a))

#Exercise 3: Define a function in python that accepts 3 values and returns the maximum of three numbers
def maximum(a,b,c):
    if a>b and a>c:
        print (a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
    return (a,b,c)
a=int(input("enter your number a :"))
b=int(input("enter your number b :"))
c=int(input("enter your number c :"))
maximum(a,b,c)

#Exercise 4: Define a function that accepts a number and returns whether the number is even or odd
def even_odd(a):
    if a%2==0:
        print("a is even:",a)
    else:
        print("a is odd:" ,a)
    return a
a=int(input("enter your number a :"))
(even_odd(a))

#Exercise 5: Define a function which counts vowels and consonant in a word.
def vowl_conso(word):
   vov=0
   con=0
   for i in range (len(word)):
       if word[i] in['a','e','i','o','u']:
           vov= vov+1
       else:
           con=con+1

   print("vowel is :",vov)
   print("consonant is :",con)
x=input("Enter your word :")
print(vowl_conso(x))

 #Exercise 6: Define a function that returns Factorial of a number
def fact(num):
    fct=1
    while (num!=0):
        fct*= num
        num=num-1
    print("factorial is :",fct)
num=int(input("enter your number :"))
fact(num)

#Exercise 7: Define a function that accepts lowercase words and returns uppercase words.
def word(text):
    print( text.upper())
text=input("enter your string:")
word(text)

#Exercise 8: Define a function that accepts radius and returns the area of a circle.
def area_of_circle(r):
    ar=3.14*r*r
    return ar
r=int(input("enter radius :"))
print(area_of_circle(r))

