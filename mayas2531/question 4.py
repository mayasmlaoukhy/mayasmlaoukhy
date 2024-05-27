class BankAccount:
    def __init__(self, account_number, account_holder):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = 0.0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self._interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self._interest_rate

    def __str__(self):
        return "Account Details:\n" \
               f"Account Number: {self._account_number}\n" \
               f"Account Holder: {self._account_holder}\n" \
               f"Balance: ${self._balance:.2f}\n" \
               f"Interest Rate: {self._interest_rate * 100:.2f}%"

# Create an instance of BankAccount
b = BankAccount("2531", "Mayas")

# Perform a deposit of $1000
b.deposit(1000)
print(f"Current balance: ${b.get_balance():.2f}")

# Perform a withdrawal of $500
b.withdraw(500)
print(f"Current balance: ${b.get_balance():.2f}")

# Create an instance of SavingsAccount
s = SavingsAccount("67890", "Mayas Mlawkhy", 0.65)
s.deposit(3000)
print(f"Current balance: ${s.get_balance():.2f}")
# Apply interest and print the current balance and rate
s.apply_interest()
print(s)