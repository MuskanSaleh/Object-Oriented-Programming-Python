class Customer:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("I am",self.name,"and I am",self.age)
    
c1 = Customer("Muskan",21)
c2 = Customer("Asad",22)
c3 = Customer("Romana",20)

L = [c1,c2,c3]

for i in L:
    i.intro()