class BankAccount:
    def __init__(self, account_id, balance, account_type,customer_id):
        self.account_id=account_id
        self.balance=float(balance)
        self.account_type=account_type
        self.customer_id=customer_id
        
    def cheak_balance(self):
        print("\nCurrent Balance:", self.balance)
        
    def show_account_type(self):
        print("Account Type:", self.account_type)
    
    def deposit(self, amount):
        if amount <= 0:
            print("invalid amount.")
            return
        self.balance += amount
        print("Deposit successful.")
        print("New balance:", self.balance)
    
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", self.balance)
    
    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance
    

    



