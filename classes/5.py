class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        if money>0:
            self.balance += money
            print("Your balance: ", self.balance)
        else:
            pass
    def withdraw(self, draw):
        self.balance -= draw
        print("Your balance: ", self.balance)
account = Account("John", 10500)
print("Summ of transition:")
d = int(input())
account.deposit(d)
print("Pay the draw:")
w = int(input())
account.withdraw(w)