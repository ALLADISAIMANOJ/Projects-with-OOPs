from abc import ABC

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Account(ABC):
    def __init__(self, account_id, user, balance=0):
        self.account_id = account_id
        self.user = user
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Withdrawal denied. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def display(self):
        print(f"Checking Account {self.account_id} for {self.user.name} has balance: ${self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_id, user, balance=0):
        super().__init__(account_id, user, balance)
        self.interest_rate = 0.02  # 2% interest rate
        self.min_balance = 100

    
class CheckingAccount(Account):
    def __init__(self, account_id, user, balance=0):
        super().__init__(account_id, user, balance)
        self.min_balance = 0

    

class BusinessAccount(Account):
    def __init__(self, account_id, user, balance=0):
        super().__init__(account_id, user, balance)
        self.interest_rate = 0.01  # 1% interest rate
        self.min_balance = 500

    

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_id, user, initial_deposit=0):
        if account_type == "savings":
            account = SavingsAccount(account_id, user, initial_deposit)
        elif account_type == "checking":
            account = CheckingAccount(account_id, user, initial_deposit)
        elif account_type == "business":
            account = BusinessAccount(account_id, user, initial_deposit)
        else:
            print("Invalid account type")
            return

        self.accounts[account_id] = account
        print(f"Created {account_type} account with ID {account_id} for {user.name}")

    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            print("Account not found")

    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].withdraw(amount)
        else:
            print("Account not found")

    def transfer(self, from_account_id, to_account_id, amount):
        if from_account_id in self.accounts and to_account_id in self.accounts:
            if self.accounts[from_account_id].balance - amount < self.accounts[from_account_id].min_balance:
                print("Transfer denied. Insufficient funds or minimum balance requirement not met.")
            else:
                self.accounts[from_account_id].withdraw(amount)
                self.accounts[to_account_id].deposit(amount)
                print(f"Transferred ${amount} from account {from_account_id} to account {to_account_id}")
        else:
            print("One or both accounts not found")

    def display_account(self, account_id):
        if account_id in self.accounts:
            self.accounts[account_id].display()
        else:
            print("Account not found")

# Example Usage
if __name__ == "__main__":
    bank = Bank()
    
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    
    bank.create_account("savings", "A001", user1, 500)
    bank.create_account("checking", "A002", user2, 300)
    bank.create_account("business", "A003", user1, 1000)
    
    bank.deposit("A001", 200)
    bank.withdraw("A002", 100)
    bank.transfer("A001", "A002", 300)
    bank.display_account("A001")
    bank.display_account("A002")
    bank.display_account("A003")
