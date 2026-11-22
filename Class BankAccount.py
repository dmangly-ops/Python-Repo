class BankAccount:

    # Initialise the bank account
    def __init__(self, customer_name, balance=0.0):
        self.customer_name = customer_name
        self.__balance = max(0.0, balance)  
        # Prevent starting wiht a negative balance

    @property
    #converted get_balance() into a python property
    #allows to access customer 1 or 2 balance cleanly
    def balance(self):
        """Access the balance securely like an attribute."""
        return self.__balance
    
    # Method to deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Successfully deposited £{amount}.")
       
    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Successfully withrew £{amount}.")

    # Method to check the balance
    def get_balance(self):
        return self.__balance


# Create a bank account object
customer1 = BankAccount("Audrey", 1000)
customer2 = BankAccount("Lionel", 2000)

#Display the initial balance before any transactions
print(f"Inital balance (before transactions) for {customer1.customer_name}: £{customer1.balance}")
print(f"Inital balance (before transactions) for {customer2.customer_name}: £{customer2.balance}")

#Perform transactions
# Deposit
customer1.deposit(200)
customer2.deposit(500)

# Withdraw
customer1.withdraw(300)
customer2.withdraw(3000)

# Display the current balance
print(f"Current balance for {customer1.customer_name}: £{customer1.balance}")
print(f"Current balance for {customer2.customer_name}: £{customer2.balance}")
