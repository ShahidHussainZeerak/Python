#take string from user and count each character in string.
s=input("Enter a string : ")
for i in s:
    c=''
    print(f"{i} = {s.count(i)}")
    c+=i
