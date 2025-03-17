class Customer:
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        
def greet(customer):
    if customer.gender == "Male":
         print("Hello",customer.name,"Sir")
    else:
         print("Hello",customer.name,"Ma'am")
    
    cust2 = Customer("Muskan","Female")     
    return cust2
            
cus = Customer("Asad","Male")
new_cust = greet(cus)
print(new_cust.name)
