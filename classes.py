# A class is like a blueprint for creating obkects. An object has properties and methods(functions) associated with it. Almost everything in python is an object

# Create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Customer class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'



# init user object
jamison = User('Jamison Kadlec', 'Jamisonmkadlec@gmail.com', 28)
rylea = User('Rylea Kadlec' 'ryleajkadlec@gmail.com', 29)

# edit property
jamison.age = 29

rylea.has_birthday()

# call method
print(rylea.greeting())

# init customer
john = Customer('John Doe', 'john@gmail.com', 40)

john.set_balance(500)

print(john.greeting())

