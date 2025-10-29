class Account:
    def __init__(self, account_number):
        self.balance = 0
        self.account_number = account_number
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print("Amount deposited:", amount)
    
    def debit(self,amount):
        self.amount = amount
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Amount debited:", amount)
    
    def print_balance(self):
        print("Current balance:", self.balance)

acc1 = Account(1001)
print("Account Number:",acc1.account_number)
acc1.deposit(5000)
acc1.print_balance()
acc1.debit(7000)
acc1.print_balance()