class Bank:

    def __init__(self):
        self.account = []
    

class Account:
    def __init__(self,customer, balance):
        self.customer = customer
        self.balance = balance
    

class Customer:
    def __init__(self, cusNr,name,age):
        self.cusNr=cusNr
        self.name=name
        self.age=age


cus1 = Customer(1,"Bob",42)

acc1 = Account(cus1,10000)

b = Bank()
b.account.append(acc1)

print(b.account[0].customer.name+"\n"+str(b.account[0].balance))