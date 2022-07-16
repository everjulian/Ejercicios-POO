from payment import Payment

class Card(Payment) :
    number      = int
    cvv         = int
    date        = int
    
    def __init__(self, id, ammount, number, cvv, date):
        super().__init__(id, ammount)
        self.number     = number
        self.cvv        = cvv
        self.date       = date
    
   
    