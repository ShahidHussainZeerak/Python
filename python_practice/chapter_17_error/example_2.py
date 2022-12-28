# Example....2.
class Mobile:
    def __init__(self,name):
        self.name=name
class Mobilestore:
    def __init__(self):
        self.mobiles=[]
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New mobile should be object of mobile class')
m=Mobile('oppo F11')
print(m.name)
mobostore=Mobilestore()
#mobostore.add_mobile("vivo")# this will raise error because vivo is not the object of a mobile class.
mobo_phones=mobostore.mobiles
print(mobo_phones[0].name) #print  name of mobile

    