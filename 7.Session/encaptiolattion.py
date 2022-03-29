class P:
    def __init__(self,name,amount):
        self.name = name        #Public variable
        self.amount = amount    #Public variable

    @property
    def get_amount(self):#Getter
        return self.__amount

    @amount.setter
    def set_amount(self,amount):#Setter
        self.__amount = amount

p = P("Bob",123)

p.__dict__
print(p.amount)


print()