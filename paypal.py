
from payment import Payment

class Paypal(Payment) :
    email  =str
    
    def __init__(self, id, ammount, email):
        super().__init__(id, ammount)
        self.email      = email
    
   
