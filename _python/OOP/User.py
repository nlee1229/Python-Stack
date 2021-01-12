from Bank_Account import BankAccount
class User: 
    def __init__(self, name, email, balance):
        print(f"CREATING USER {name}")
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance)
        
    
    def make_deposit(self, amount): #takes an arguments that is the amount of the deposit
        print(f"DEPOSITING ${amount} TO {self.name}")
        self.account.deposit
        
    
    def make_withdrawal(self, amount):
        print(f"{self.name}, withdrew $ {amount} in their account.")
        self.account.withdrawal
        # self.account_balance = self.account_balance - amount

    def display_user_balance(self):
        print(f"{self.name}, has $ {self.account_balance} left in their account.")
        self.account.display_account_info


john = User("John", "email@fake.com", 500)
guido = User("Guido", "guidoemail.com", 540)
sadie = User("Sadie", "sadiemail@gmail.com", 345)

john.make_deposit(50)
print(john.account_balance)
john.make_deposit(75)
john.make_deposit(95)
john.make_withdrawal(35)
john.display_user_balance()

guido.make_deposit(3)
guido.make_deposit(73)
guido.make_withdrawal(4)
guido.make_withdrawal(9)
guido.display_user_balance()

sadie.make_deposit(54)
sadie.make_withdrawal(40)
sadie.make_withdrawal(100)
sadie.make_withdrawal(20)
sadie.display_user_balance()





    


    
