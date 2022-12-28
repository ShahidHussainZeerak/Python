# use of try , except ,else and finallay...
# use infinte while loop...the loop will execute till corect output
while True:
    try:
        age=int(input("enter your age here : "))
        
    except ValueError:
        print("you entered incorrect value : ")
    except:
        print("invalid out put")
    else:
        if  age<18:
             print("you are not eligible for this game : ")
    finally:
        print('you are  eligible for this game : ')

