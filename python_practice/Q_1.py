a=int(input("Enter first No : "))
b=int(input("Enter second No : "))
c=int(input("Enter second No : "))

if a>b and a>c:
    print(f" {a}  is greater then {b} and {c}")
    
elif b>a  and b>c:
    print("{c} is greater than {a} and {c}")
elif c>a and c>b:
    print(f"{c} is greter then {a }and {b}")
else:
    print('equal')

if a<b and a<c:
    print(f' {a} is smaller then  {b} and {c}')
elif  b<a and b<c:
    print(f' {b} is smaller then  {a} and {c}')
elif c<a and c <b:
    print(f' {c} is smaller then  {a} and {b}')
else:
    print('Equal  ')
