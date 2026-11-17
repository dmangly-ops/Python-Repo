class BankAccount:

    # Initialise the bank account
    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.__balance = balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    # Method to check the balance
    def get_balance(self):
        return self.__balance


# Create a bank account object
customer1 = BankAccount("Audrey", 1000)

# Deposit £200
customer1.deposit(200)

# Withdraw £300
customer1.withdraw(300)

# Display the current balance
print("Current balance:", customer1.get_balance())