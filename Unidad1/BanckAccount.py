#Create a BanckAccount class with functions

class banckAccount():
    def __init__(self):
        pass

    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print("Account Holder: " , self.name)
        print("Account balance: " , self.balance)

    def recall(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

cuenta1 = banckAccount()
cuenta2 = banckAccount()

cuenta1.set_details("Ismael de la Rosa Guerrero", 200000)
cuenta1.display()
cuenta1.recall(1000)
cuenta1.deposit(2000)
cuenta1.display()