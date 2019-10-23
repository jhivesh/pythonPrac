"""""#object orientated"""
class Employee:
    pass    #no attributes
    def __init__(self, first, last, pay):     #constructor : that initialise all objects
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "-" + last


empl_1 = Employee("john", "wick", 10000)
empl_2 = Employee("mia", "khalifa", 10000000)

print(empl_2.email)
print(empl_1.email)

"""""#   We dont need to do this as init method does it for us
instance variable
empl_1.first = "john"
empl_1.last = "wick"
empl_1.email = "jwick@gmail.com"
empl_1.pay = 10000
"""""



