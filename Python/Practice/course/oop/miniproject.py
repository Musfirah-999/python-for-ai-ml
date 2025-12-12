class Account:
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
    
    def input_details(self):
        amount = float(input("Enter amount to deposit/withdraw: "))
        return amount
    
    def deposit(self):
        amount = self.input_details()
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.balance
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
        print(f"Deposited: ${amount}")
        return self.balance
    
    
    def withdraw(self):
       amount = self.input_details()
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
        return f"Account Number: {self.account_number}, Balance: {self.balance}"
    def transection_history(self):
        if self.transactions == []:
            print("No transactions yet.")
            return
        print(f"--Transaction History for Account {self.account_number}---")
        for transaction in self.transactions:
            print(f"\t{transaction}")
        
        
        
class BankSystem:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts by account number
        
    def get_account(self,account_number) -> Account:
        return self.accounts.get(account_number, None)
    
    def create_account(self, account_number, initial_balance) :
        if account_number in self.accounts:
            print("Account already exists.")
            return None
        new_account = Account(account_number, initial_balance)
        self.accounts[account_number] = new_account
        print(f"Account {account_number} created with balance ${initial_balance}.")
        return new_account
        
    
    
bank_system = BankSystem()
bank_system.create_account("123456789", 1000.0)
my_account = bank_system.get_account("123456789")
if my_account:
    print(my_account.check_balance())
    my_account.deposit()
    print(my_account.check_balance())
    my_account.withdraw()
    print(my_account.check_balance())
    my_account.transection_history()
    

bank_system.create_account("12345", 100.0)
sarah_account = bank_system.get_account("12345")
if sarah_account:
    print(sarah_account.check_balance())
    sarah_account.deposit()
    print(sarah_account.check_balance())
    sarah_account.withdraw()
    print(sarah_account.check_balance())
    sarah_account.transection_history()



