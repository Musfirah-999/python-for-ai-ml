class Account:
    def __init__(self,account_holder, balance,):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []
    
    
    def deposit(self,amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.balance
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
        print(f"Deposited: ${amount}")
        return self.balance
    
    
    def withdraw(self, amount):
       
       if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self.balance
       elif amount > self.balance:
            print("Insufficient balance.")
            return self.balance
       self.balance -= amount
       self.transactions.append(f"Withdrawn: ${amount}")
       print(f"Withdrawn: ${amount}")
       return self.balance
   
    def check_balance(self):
        return f"Account Number: {self.account_holder}, Balance: {self.balance}"
    def transection_history(self):
        if self.transactions == []:
            print("No transactions yet.")
            return
        print(f"--Transaction History for {self.account_holder}'s Account---")
        for transaction in self.transactions:
            print(f"\t{transaction}")
            
class BankSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, initial_balance):
        if name in self.accounts:
            print(f"Account {name} already exists")
        else:
            self.accounts[name] = Account(initial_balance, name)
        
    def  get_account(self, name) -> Account:
        return self.accounts.get(name, None)

bank = BankSystem()
bank.create_account("David", 25)
               
    