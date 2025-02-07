class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}$. New balance: {self.balance}$")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Available balance: {self.balance}$")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: {amount}$. New balance: {self.balance}$")
        else:
            print("Withdrawal amount must be positive.")


account = BankAccount(input("Enter your name: "), int(input("Your account balance is: ")))
account.deposit(int(input("How much money you want to deposit: ")))

account.withdraw(int(input("How much money you want to withdraw: ")))
print(f"Final balance: {account.balance}$")