from pprint import pprint
from account import Account
from car import Car
from cash import Cash
from uberConfor import UberConfort
from uberx import UberX


if __name__ == "__main__":

    car = Car("PBO5555", Account("Diego Yanez", "17215555555"))   
    print(vars(car))
    print(vars(car.driver))
    
    uberX = UberX("PCC-12345", Account("Manuelita", "555555555"), "Chevrolet", "Spark")
    print(vars(uberX))
    print(vars(uberX.driver))
    
    uberConfort = UberConfort("PJK-4561", Account("Jose", "123456789"), "Dodge", "Cuero", "6")
    print(vars(uberConfort))
    print(vars(uberConfort.driver))
    
    pagoDinero = Cash("1", "14-7-2022", "20", "Cash")
    print(vars(pagoDinero))
    print(pagoDinero.date)
    
    
    


# if __name__ == "__main__":
    
#     # car = Car()
#     # car.id          = 1
#     # car.brand       = "Toyota"
#     # car.driver      = "Sebas"
#     # car.passager    = 4
#     # print(vars(car))
    
    
#     # car2 = Car()
#     # car2.id          = 2
#     # car2.brand       = "Renault"
#     # car2.driver      = "Luis"
#     # car2.passager    = 5
#     # print(vars(car2))
    

#     # account = Account()
#     # account.id          = 1
#     # account.name        = "Carlos"
#     # account.document    = 17549846
#     # account.mail        = "mail@gma"
#     # print(vars(account))
    
    
#     # payment = Payment()
#     # payment.id          = 1
#     # payment.ammount     =  1000
#     # print(vars(payment))
    
    
#     # driver = Driver()
#     # driver.id            = 1
#     # driver.name          = "Juan"
#     # driver.document      = "GMN-005195560-PAR"
#     # driver.email         = "juan_4@gmail.com"
#     # driver.possword      = 1225593
#     # print(vars(driver))
    
#     # user = User()
#     # user.id             = 1
#     # user.name           = "Pedro"
#     # user.document       =  "172832059"
#     # user.email          = "pedro6@gmail.com"
#     # user.possword       = 5289423
#     # print(vars(user))
    
 