class BankAccount:
    def __init__(self, account_holder, balance,):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.balance
        self.balance = self.balance + amount
        self.transactions.append(f"Deposited: ${amount}")
        print(f"Deposited: ${amount}. New Balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self.balance
        elif amount > self.balance:
            print("Insufficient balance.")
            return self.__balance
        self.balance -= amount
        self.transactions.append(f"Withdrawn: ${amount}")
        print(f"Withdrawn: ${amount}")
        return self.balance

    def check_balance(self):
        print(
            f"Account Number: {self.account_holder}, Balance: ${self.balance}")

    def transection_history(self):
        if self.transactions == []:
            print("No transactions yet.")
            return
        print(f"--Transaction History for {self.account_holder}'s Account---")
        for transaction in self.transactions:
            print(f"\t{transaction}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"\nAccount Holder: {self.account_holder}, Balance: ${self.balance} "


class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: {self.balance}")

    def withdraw(self, amount):
        # raise NotImplementedError("withdraw is not implemented")
        if amount > 0 and (self.balance - amount) >= 100:
            self.balance -= amount
            print(f"Withdraw: ${amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or minimum balance required ($100)")
        
        
class CheckingAccount(BankAccount):   
    def __init__(self, account_holder, balance, overdraft_limt = 200):
        super().__init__(account_holder, balance)   
        self.overdraft_limit = overdraft_limt
    def withdraw(self, amount):
        if amount>0 and (self.balance - amount)>= -self.overdraft_limit:
            self.balance-=amount
            print(f"WIthdraw ${amount}. New balance ${self.balance}")
        else:
            print(f"OverfloW limit reached. Cannot withdraw ${amount}")
    
     
        
savings = SavingAccount("John", 300)
savings.deposit(200)
savings.withdraw(500)
print(savings)

checking = CheckingAccount("David", 200)
checking.deposit(100)
checking.withdraw(500)
checking.withdraw(1)
print(checking)