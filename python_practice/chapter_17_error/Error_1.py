# Type of erros are (syntax,attribute,index,identation,value,type and name) errors.
# Raise of Error
def add(a,b): 
    if (type(a) is int) and (type(b)is int):
        return a+b
    raise TypeError('You are passing wrong data')  # if the passing value  are not integers then this error will be raise.
print(add("3","4"))
