#Write a program where a BankAccount class has methods to deposit, withdraw, and check the balance.
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        """
        Initialize the bank account with an account holder and an optional initial balance.
        """
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """
        Check the current account balance.
        """
        print(f"Current balance: {self.balance}")
        return self.balance


# Example usage
if __name__ == "__main__":
    # Create a bank account for "John Doe" with an initial balance of 100
    account = BankAccount("John Doe", 100)

    # Deposit money
    account.deposit(50)

    # Withdraw money
    account.withdraw(30)

    # Try withdrawing more than the balance
    account.withdraw(150)

    # Check the balance
    account.check_balance()
