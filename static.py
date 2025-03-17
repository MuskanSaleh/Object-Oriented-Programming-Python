#simple
class Atm:
    #static/class
    #shared among all instances of the class.
    # It keeps track of the number of Atm objects created.
    __counter = 1
    
    #constructor
    def __init__(self):
        self.pin = ""  #instance variable each object gets its own copy of these variables.
        self.balance = 0 #instance variable
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        print(id(self))
    
    @staticmethod #doesnt need self object
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allowed")  

#Each object has its own instance variables (pin, balance, sno) 
# but shares the class variable (counter).
  
c1 = Atm()
c2 = Atm()
c3 = Atm()

print(c1.sno)
print(c2.sno)
print(c3.sno)

print(Atm.get_counter())
Atm.set_counter(5)

