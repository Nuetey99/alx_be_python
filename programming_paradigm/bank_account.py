class BankAccount:
    def __init__ (self, account_balance):
        self.current_balance = account_balance
        
    
    def deposit(self, amount):
        self.current_balance = amount + self.current_balance
        return self.current_balance
    
    def withdraw(self,amount):
        if self.current_balance >= amount:
            self.current_balance = amount - self.current_balance
        else:
            raise Exception("Insufficient funds")

    def display_balance(self):
        return print(f"${self.account_balance:.2f} is your current balance")
    