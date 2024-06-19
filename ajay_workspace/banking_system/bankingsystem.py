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
    account_no = ""
    holder_name = ""
    balance = ""
    print(account_no, holder_name)

    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        print("name : ", self.holder_name)
        print("account : ", self.account_no)
        print("Amount : ", amount)
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for num, i in enumerate(file_data):
            data = i.split(",")
            if self.account_no in data:
                current_balance = int(data[-1])
                data[-1] = str(current_balance + int(amount))
                file_data[num] = ",".join(data) + "\n"
        with open("bankingsystem.txt", "w") as file:
            file.writelines(file_data)
        print("~" * 40)
        print(f"Account No : {self.account_no} Credited With amount : {amount}")
        print("~" * 40)

    def withdraw(self, amount):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for num, i in enumerate(file_data):
            data = i.split(",")
            if self.account_no in data:
                current_balance = int(data[-1])
                new_balance = int(amount)
                data[-1] = str((current_balance - new_balance))
                balance = int(amount)
                file_data[num] = ",".join(data) + "\n"
        with open("bankingsystem.txt", "w") as file:
            file.writelines(file_data)
        print("~" * 40)
        print(f"Account No : {self.account_no} debited With amount : {amount}")
        print("~" * 40)

    def get_balance(self, account_no):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for i in file_data:
            if account_no in i:
                return i.split(",")

    def __str__(self):
        return f"{self.account_no}{self.holder_name}{self.balance}"


class UtilityClass:
    def generate_ac_no(self):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        if file_data != []:
            no = file_data[-1].split(",")
            return int(no[0]) + 1
        else:
            return 100000000000

    def verify_account_no(self, account_no):
        flag = False
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for i in file_data:
            data = i.split(",")
            if account_no == data[0]:
                return True
        else:
            False

    def verify_balance(self, account_no, amount):
        flag = False
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for i in file_data:
            data = i.split(",")
            if account_no == data[0]:
                if int(amount) <= int(data[-1][:-1]):
                    return True
        else:
            False


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

    def __init__(self):
        pass

    def add_account(self, holder_name, account_no):
        with open("bankingsystem.txt", "a") as file:
            balance = 0
            file.write(f"{holder_name},{account_no},{balance}\n")
        print("~"*40)
        print("Account created successfully.")
        print("~"*40)

    def assign(self):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for num, i in enumerate(file_data):
            acc_no, holder_name, balance = i.split(",")
            obj = Account(acc_no, holder_name, balance)
            self.accounts.append(obj)

    def find_account(self, account_no):
        for i in self.accounts:
            acc_no = i.account_no
            holder_name = i.holder_name
            balance = i.balance
            if account_no == acc_no:
                obj = Account(acc_no, holder_name, balance)
                return obj
        else:
            return False

    def deposit_to_account(self, account_no, amount):
        super.account_no = account_no
        self.find_account(account_no)
        super().deposit(amount)

    def withdraw_from_account(self, account_no, amount):
        super().withdraw(amount)

    def transfer(self, from_account_number, to_account_number, amount):
        Account.withdraw(from_account_number, amount)
        print(f"Account no {to_account_number} debited with amount {amount} !")
        Account.deposit(to_account_number, amount)
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


bank_obj = Bank()
bank_obj.assign()
utility_obj = UtilityClass()


class Perform_Operation:
    def perform(self):
        while True:
            print("\n\n\n")
            print("Enter 1 for create new account : ")
            print("Enter 2 to find your account :  ")
            print("Enter 3 for deposit money in your account : ")
            print("Enter 4 for withdraw money from your account : ")
            print("Enter 5 to transfer money from your account : ")
            print("Enter 7 for exit : ")
            no = int(input("Follow the above instructions to peform operations : "))

            # for add Account
            if no == 1:
                acc_no = utility_obj.generate_ac_no()
                holder_name = input("Enter account holder name : ")
                bank_obj.add_account(acc_no, holder_name)

            # for find account and perform deposit,withdraw,get balance
            elif no == 2:
                account_no = input("Enter Account Number : ")
                if data := bank_obj.find_account(account_no):
                    print("~" * 40)
                    print(
                        f"Name : {data.holder_name}\nAccount No : {data.account_no}\nBalance : {data.balance}"
                    )
                    print("~" * 40)
                    count = 3
                    while count:
                        print("Enter 1 to deposit money.")
                        print("Enter 2 to withdraw money.")
                        print("Enter 3 to get balance.")
                        print("Enter 4 to main menu.")
                        no = int(
                            input(
                                "Follow the above instructions to peform operations : "
                            )
                        )
                        if no == 1:
                            count_deposit = 3
                            while count_deposit:
                                amount = int(
                                    input("Enter amount you want to deposit : ")
                                )
                                if amount > 0:
                                    data.deposit(str(amount))
                                    break
                                else:
                                    print("~" * 40)
                                    print(
                                        "Amount You Are Trying To Deposit Is Less Than 1"
                                    )
                                    print("~" * 40)
                                    count_deposit -= 1
                                    print(
                                        f"You have only {count_deposit} chances are left to enter correct ammount ."
                                    )
                        elif no == 2:

                            count_withdraw = 3
                            while count_withdraw:
                                amount = int(
                                    input("Enter amount you want to withdraw : ")
                                )
                                if amount < 1:
                                    print("~" * 40)
                                    print(
                                        "Amount You Are Trying To withdraw Is Less Than 1!"
                                    )
                                    print("~" * 40)
                                    count_withdraw -= 1
                                    print(
                                        f"You have only {count_withdraw} chances are left to enter correct ammount ."
                                    )
                                elif amount > int(data.balance):
                                    print("~" * 40)
                                    print("Insufficient balance!")
                                    print("~" * 40)
                                    count -= 1
                                    print(
                                        f"You have only {count_withdraw} chances are left to enter correct ammount ."
                                    )
                                else:
                                    data.withdraw(str(amount))
                                    break
                        elif no == 3:
                            print("~" * 40)
                            print(
                                f"Account balance of {data.account_no} is {data.balance}"
                            )
                            print("~" * 40)

                        elif no == 4:
                            break

                else:
                    count = 2
                    for i in range(count):
                        print("~" * 40)
                        print("Account Does Not Exist!")
                        print("~" * 40)
            # for deposit money this belongs to bank class
            elif no == 3:
                count_deposit = 3
                while count_deposit:
                    account_no = input(
                        "Enter account no in which you want to deposit : "
                    )
                    if data := bank_obj.find_account(account_no):
                        count_deposit_inner = 3
                        print(data.account_no, data.holder_name)
                        while count_deposit_inner:
                            amount = int(input("Enter amount you want to deposit : "))
                            if amount < 1:
                                print("~" * 40)
                                print("The amount you want to deposit is less than 1")
                                print("~" * 40)
                                count_deposit -= 1
                                print("~" * 40)
                                print(
                                    f"You have only {count_deposit} chances are left."
                                )
                                print("~" * 40)
                            else:
                                bank_obj.deposit_to_account(account_no, str(amount))
                                break
                    else:
                        count_deposit -= 1
                        print("~" * 40)
                        print(f"You have only {count_deposit} chances are left.")
                        print("~" * 40)


perform_obj = Perform_Operation()
perform_obj.perform()
