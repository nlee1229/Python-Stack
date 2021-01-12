class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.account_balance = balance
    
    def make_deposit(self, amount): #takes an arguments that is the amount of the deposit
        print(f"{self.name}, deposited $ {amount} in their account.")
        self.account_balance += amount
        
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        # self.account_balance = self.account_balance - amount

    def display_user_balance(self):
        print(f"{self.name}, has $ {self.account_balance} in their account.")


john = User("John", "email@fake.com", 500)
guido = User("Guido", "guidoemail.com", 540)

john.make_deposit(50)
print(john.account_balance)
john.make_deposit(75)
print(john.account_balance)
john.make_deposit(95)
print(john.account_balance)
john.make_withdrawal(35)
print(john.account_balance)
john.display_user_balance()

guido.make_deposit(3)
print(guido.account_balance)
guido.display_user_balance()


    
