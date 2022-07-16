from payment import Payment

class Cash(Payment):
    
    def __init__(self, id, ammount):
        super().__init__(id, ammount)
    