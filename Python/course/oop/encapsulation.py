class Account:
    def __init__(self,account_holder, balance,):
        self.account_holder = account_holder
        self.__balance = balance
        self.transactions = []
    
    
    def deposit(self,amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.__balance
        self.__balance = self.__balance + amount
        self.transactions.append(f"Deposited: ${amount}")
        print(f"Deposited: ${amount}")
        return self.__balance
    
    
    def withdraw(self, amount):
       
       if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self.__balance
       elif amount > self.__balance:
            print("Insufficient balance.")
            return self.__balance
       self.__balance -= amount
       self.transactions.append(f"Withdrawn: ${amount}")
       print(f"Withdrawn: ${amount}")
       return self.__balance
   
    def check_balance(self):
        print( f"Account Number: {self.account_holder}, Balance: ${self.__balance}")
    def transection_history(self):
        if self.transactions == []:
            print("No transactions yet.")
            return
        print(f"--Transaction History for {self.account_holder}'s Account---")
        for transaction in self.transactions:
            print(f"\t{transaction}")
    def get_balance(self):
        return self.__balance
            
class BankSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, initial_balance):
        if name in self.accounts:
            print(f"Account {name} already exists")
        else:
            self.accounts[name] = Account(name, initial_balance)
        
    def  get_account(self, name) -> Account:
        return self.accounts.get(name, None)

bank = BankSystem()
bank.create_account("David", 25)
david_account = bank.get_account("David")
if david_account:
    david_account.deposit(25)
    david_account.deposit(10)
    david_account.withdraw(15)
    david_account.check_balance()
    david_account.transection_history()
    # david_account.__balance = 100 
    david_account.transection_history()
    david_account.check_balance()
    print(david_account.get_balance())
    
    