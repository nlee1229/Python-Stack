class BankAccount:
    def __init__(self, balance, int_rate): #self is basically like this
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
        return self #have this because we're gonna be doing chaining methods later
    def withdrawal(self, amount):
        self.balance -= amount
        return self
    def yield_interest(self): 
        if (self.balance < 0):
            print("Error: Balance insufficient")
            return self
        else:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self

# bobBA = BankAccount(100, 0.02, "checking")
# chadBA = BankAccount(200, 0.03, "debit")
# print(bobBA.balance, bobBA.account_name, bobBA.int_rate)
# bobBA.deposit(20).deposit(30).deposit(10).withdrawal(50).display_account_info().yield_interest()
# chadBA.deposit(10).deposit(30).withdrawal(5).withdrawal(5).withdrawal(5).withdrawal(5).display_account_info().yield_interest()





        


