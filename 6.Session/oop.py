class Person:

    #Class variable
    type = "Mammel"


    #init is used to initialize the object
    def __init__(self,name):
        self.name = name #Instance variable


    def message(self):
        return print("Hello world")

p = Person("Bob")
p.message()
print(p.name)
print(p.type)