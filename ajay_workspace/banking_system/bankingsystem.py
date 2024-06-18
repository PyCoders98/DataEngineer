# ### Steps to Implement the Simple Banking System


# 1. **Define the `Account` Class**:
#     - Create the `Account` class with attributes:
#         - `account_number`
#         - `holder_name`
#         - `balance`
#     - Implement methods:
#         - `deposit(amount)`: Adds funds to the account balance.
#         - `withdraw(amount)`: Subtracts funds from the account balance.
#         - `get_balance()`: Returns the current balance.
#         - `__str__()`: Returns a string representation of the account details.
class Account:
    # account_number
    # holder_name
    # balance
    def deposit(self, account_no, amount):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for num, i in enumerate(file_data):
            data = i.split(",")
            print(data)
            if account_no in data:
                data[-1] = amount
                file_data[num] = ",".join(data) + "\n"
        with open("bankingsystem.txt", "w") as file:
            file.writelines(file_data)

    def withdraw(self, account_no, amount):
        balance = 0
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for num, i in file_data:
            data = i.split(",")
            if account_no in data:
                current_balance = data[-1]
                new_balance = int(amount)
                data[-1] = str(current_balance - new_balance)
                balance = int(amount)
            file_data[num] = ",".join(data) + "\n"
        with open("bankingsystem.txt", "w") as file:
            file.writelines(file_data)
        # return balance

    def get_balance(self, account_no):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for i in file_data:
            if account_no in i:
                return i.split(",")

    def __str__(self):
        pass


class UtilityClass:
    def generate_ac_no(self):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        if file_data != []:
            no = file_data[-1].split(",")
            # new_ac_no=no[0]+1
            return int(no[0]) + 1
        else:
            return 100000000000


# 2. **Define the `Bank` Class**:
#     - Create the `Bank` class with attributes:
#         - `name`
#         - `accounts` (a list to store `Account` objects)
#     - Implement methods:
#         - `add_account(account)`: Adds a new account to the bank.
#         - `find_account(account_number)`: Finds an account by its account number.
#         - `deposit_to_account(account_number, amount)`: Deposits money into a specified account.
#         - `withdraw_from_account(account_number, amount)`: Withdraws money from a specified account.
#         - `transfer(from_account_number, to_account_number, amount)`: Transfers money between two accounts.
#         - `close_account(account_number)`: Closes a specified account.
#         - `__str__()`: Returns a string representation of the bank's details.
class Bank(Account):
    name = "Smart Bank"
    accounts = []

    # accountopen karne ke liye holdername or bank name ki jrurat hogi
    def add_account(self, holder_name, account_no):
        # holder_name = str("Enter account holder name : ")
        with open("bankingsystem.txt", "a") as file:
            balance = 0
            file.write(f"{holder_name},{account_no},{balance}\n")
        self.accounts.append([holder_name, account_no])

    def find_account(self, account_no):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for i in file_data:
            if account_no in i:
                return i.split(",")

    def deposit_to_account(self, account_no, amount):
        super().deposit(account_no, amount)

    def withdraw_from_account(self, account_no, amount):
        super.withdraw(account_no, amount)

    def transfer(self, from_account_number, to_account_number, amount):
        super.withdraw(from_account_number, amount)
        print(f"Account no {to_account_number} debited with amount {amount} !")
        super.deposit(to_account_number, amount)
        print(f"Account no {to_account_number} credited with amount {amount} !")

    def close_account(self, account_no):
        pass

    def __str__(self):
        pass


# 3. **Create a Main Script**:
#     - Initialize a `Bank` object.
#     - Create multiple `Account` objects.
#     - Add the `Account` objects to the `Bank` object.
#     - Perform various operations such as depositing, withdrawing, transferring money, checking balances, and closing accounts.
#     - Print the results of the operations to verify correctness.

obj = Bank()
utility_obj = UtilityClass()


class Perform_Operation:
    def __init__(self):
        while True:
            print("Enter 1 for create new account : ")
            print("Enter 2 to find your account :  ")
            print("Enter 3 for deposit money in your account : ")
            print("Enter 4 to transfer money from your account : ")
            print("Enter 7 for exit : ")
            no = int(input("Follow the above instructions to peform operations : "))
            if no == 1:
                acc_no = utility_obj.generate_ac_no()
                holder_name = input("Enter account holder name : ")
                obj.add_account(acc_no, holder_name)
            elif no == 2:
                acc_no = input("Enter account number : ")
                print(obj.find_account(acc_no))
            elif no == 3:
                acc_no = input("Enter account number : ")
                amount = input("Enter ammount you want to deposite : ")
                obj.deposit_to_account(acc_no, amount)
            elif no == 4:
                acc_no1 = input(
                    "Enter account number from you want to transfer money : "
                )
                acc_no2 = input(
                    "Enter account number in which you want to tranfer money : "
                )
                amount = input("Enter ammount you want to transfer : ")
                obj.transfer(acc_no1,acc_no2,amount)
            else:
                break


perform_obj = Perform_Operation()
