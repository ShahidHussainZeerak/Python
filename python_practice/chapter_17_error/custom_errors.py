# we can also raise a error ... which is called custom error.
class NameTooShortError:
    pass

def validate(name):
    if len(name)<8:
        print (NameTooShortError("name is too short"))
name=input('enter your name : ')
validate(name)
print(f'hello {name}')
