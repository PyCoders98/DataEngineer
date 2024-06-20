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


utility_obj = UtilityClass()


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


class Bank(Account):
    name = "Smart Bank"
    accounts = []

    def __init__(self):
        pass

    def add_account(self,account_no, holder_name ):
        with open("bankingsystem.txt", "a") as file:
            balance = 0
            file.write(f"{account_no},{holder_name},{balance}\n")
        print("~" * 40)
        print("Account created successfully.")
        print("~" * 40)
        print(f"This is your account no. {account_no}")

    def assign(self):
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for i in file_data:
            acc_no, holder_name, balance = i.split(",")
            obj = Account(acc_no, holder_name, balance)
            self.accounts.append(obj)

    def find_account(self, account_no):
        self.assign()
        for i in self.accounts:
            acc_no = i.account_no
            holder_name = i.holder_name
            balance = i.balance
            if account_no == acc_no:
                self.account_no = acc_no
                self.holder_name = holder_name
                self.balance = balance
                obj = Account(acc_no, holder_name, balance)
                return obj
        else:
            return False

    def deposit_to_account(self, account_no, amount):
        super().deposit(amount)

    def withdraw_from_account(self, account_no, amount):
        super().withdraw(amount)

    def transfer(self, from_account_number, to_account_number, amount):
        Account.withdraw(from_account_number, amount)
        print(f"Account no {to_account_number} debited with amount {amount} !")
        Account.deposit(to_account_number, amount)
        print(f"Account no {to_account_number} credited with amount {amount} !")

    def close_account(self, account_no):
        new_file = []
        with open("bankingsystem.txt", "r") as file:
            file_data = file.readlines()
        for i in file_data:
            data = i.split(",")
            if account_no == data[0]:
                continue
            new_file.append(",".join(data))
        with open("bankingsystem.txt", "w") as file:
            file.writelines(new_file)
            count = -1
        print("Account closed successfully!")

    def __str__(self):
        return super().__str__()


bank_obj = Bank()
bank_obj.assign()


class Perform_Operation:
    def perform(self):
        while True:
            print("\n")
            print("Enter 1 for create new account . ")
            print("Enter 2 to find your account .  ")
            print("Enter 3 for deposit money in your account . ")
            print("Enter 4 for withdraw money from your account . ")
            print("Enter 5 to transfer money from your account into another account . ")
            print("Enter 6 to close account . ")

            print("Enter 7 for exit . ")
            no = int(input("Follow the above instructions to peform operations : "))

            # for add Account
            if no == 1:

                acc_no = utility_obj.generate_ac_no()
                count = 3
                while count:
                    holder_name = input("Enter account holder name : ")
                    if holder_name == "":
                        print("~" * 40)
                        print("You can't leave name blank : ")
                        count -= 1
                        print("~" * 40)
                        print(f"you have only {count} chances are left")
                        print("~" * 40)
                    else:
                        bank_obj.add_account(acc_no, holder_name)
                        break

            # for find account and perform deposit,withdraw,get balance
            elif no == 2:
                account_no = input("Enter Account Number : ")
                bank_obj.accounts.clear()
                bank_obj.assign()
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
                                    if count_deposit > 0:
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
                                    if count_withdraw > 0:
                                        print(
                                            f"You have only {count_withdraw} chances are left to enter correct ammount ."
                                        )
                                elif amount > int(data.balance):
                                    print("~" * 40)
                                    print("Insufficient balance!")
                                    print("~" * 40)
                                    count_withdraw -= 1
                                else:
                                    data.withdraw(str(amount))
                                    break
                        elif no == 3:
                            # bank_obj.update_accounts(account_no)
                            account_details = bank_obj.get_balance(account_no)
                            print("~" * 40)
                            print(
                                f"Account balance of {account_details[0]} is {account_details[-1][:-1]}"
                            )
                            print("~" * 40)

                        elif no == 4:
                            break

                else:
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
                    bank_obj.accounts.clear()
                    bank_obj.assign()
                    if data := bank_obj.find_account(account_no):
                        print("~" * 40)
                        print(
                            f"Name : {data.holder_name}\nAccount No : {data.account_no}\nBalance : {data.balance}"
                        )
                        print("~" * 40)
                        count_deposit_inner = 3
                        while count_deposit_inner:
                            amount = int(input("Enter amount you want to deposit : "))
                            if amount < 1:
                                print("~" * 40)
                                print("The amount you want to deposit is less than 1")
                                print("~" * 40)
                                count_deposit_inner -= 1
                                if count_deposit_inner == 0:
                                    count_deposit_inner = 0
                                    count_deposit = 0

                                else:
                                    print("~" * 40)
                                    print(
                                        f"You have only {count_deposit_inner} chances are left to enter correct amount."
                                    )
                                    print("~" * 40)
                            elif amount > 1:
                                bank_obj.deposit_to_account(account_no, str(amount))
                                print("")
                                decision = input(
                                    "Do you want to deposit more money - y/n : "
                                )
                                if decision.lower() == "n":
                                    count_deposit_inner = 0
                                    count_deposit = 0
                            if count_deposit_inner == 0:
                                count_deposit_inner = 0
                                count_deposit = 0

                    else:
                        count_deposit -= 1

                    if count_deposit > 0:
                        print("~" * 40)
                        print(
                            f"You have only {count_deposit} chances are left to enter correct acount number."
                        )
                        print("~" * 40)
                    elif count_deposit < 1:
                        print("\n")
                        input("Press enter to go back in main menu : ")

            elif no == 4:
                count_withdraw = 3
                account_no = input(
                    "Enter account no from which you want to Withdraw money : "
                )
                while count_withdraw:
                    bank_obj.accounts.clear()
                    bank_obj.assign()
                    if data := bank_obj.find_account(account_no):
                        print("~" * 40)
                        print(
                            f"Name : {data.holder_name}\nAccount No : {data.account_no}\nBalance : {data.balance}"
                        )
                        amount = int(input("Enter amount you want to withdraw : "))
                        if amount < 1:
                            print("~" * 40)
                            print("Amount You Are Trying To withdraw Is Less Than 1!")
                            print("~" * 40)
                            count_withdraw -= 1
                            print(
                                f"You have only {count_withdraw} chances are left to enter correct ammount ."
                            )
                        elif amount > int(data.balance):
                            print("~" * 40)
                            print("Insufficient balance!")
                            print("~" * 40)
                            count_withdraw -= 1
                            print(
                                f"You have only {count_withdraw} chances are left to enter correct ammount ."
                            )

                        else:
                            data.withdraw(str(amount))

                        no = input("Do you want to withraw more money - y/n : ")
                        if no.lower() == "n":
                            break
            # for transfering money from your account to another account

            elif no == 5:
                bank_obj.assign()
                flag = True
                account_no_from = input(
                    "Enter account no from which you want to transfer money : "
                )
                if utility_obj.verify_account_no(account_no_from):
                    data = bank_obj.find_account(account_no_from)
                    print("~" * 40)
                    print(f"Name : {data.holder_name}\nBalance : {data.balance}")
                    print("~" * 40)
                while flag:
                    if int(data.balance) > 0:
                        account_no_to = input(
                            "Enter account no in which you want to transfer money : "
                        )
                        if utility_obj.verify_account_no(account_no_to):
                            count = 3
                            data2 = bank_obj.find_account(account_no_to)
                            print(
                                f"Name : {data2.holder_name}\nBalance : {data2.balance}"
                            )
                            while count:
                                amount = input(
                                    "Enter amount you want to transfer : "
                                )
                                if utility_obj.verify_balance(
                                    account_no_from, amount
                                ):
                                    bank_obj.find_account(account_no_from)
                                    bank_obj.withdraw_from_account(
                                        account_no_from, str(amount)
                                    )
                                    bank_obj.find_account(account_no_to)
                                    bank_obj.deposit_to_account(
                                        account_no_to, str(amount)
                                    )
                                    print("Transferrerd successfully : ")
                                    count = 0
                                    flag =False
                                else:
                                    print("~" * 40)
                                    print("Insufficient balance : ")
                                    print(
                                        f"Your current balance is {data.balance}Which is lower than the amount {amount} you want to transfer."
                                    )
                                    print("~" * 40)
                                    count -= 1
                        else:
                            print("~" * 40)
                            print("Account Does not exist .")
                            print("~" * 40)
                    else:
                        print(
                            "Your current balance is 0 you are not eligible to transfer money . "
                        )
                        print("~" * 40)
                        decision = input(
                            "Do you want to continue with another account - y/n : "
                        )
                        if decision.lower() == "n":
                            flag = False
                    print("~" * 40)
            # for closing account
            elif no == 6:
                while True:
                    account_no = input("Enter account no you want to close : ")
                    if utility_obj.verify_account_no(account_no):
                        print("~" * 40)
                        data = bank_obj.find_account(account_no)
                        print(
                            f"Account no : {data.account_no}\nName : {data.holder_name}"
                        )
                        print("~" * 40)
                        decision = input(
                            "Are you sure you want to close account? y/n : "
                        )
                        print("~" * 40)
                        if decision.lower() == "y":
                            bank_obj.close_account(account_no)
                            bank_obj.accounts.clear()
                            bank_obj.assign()
                            break
                        else:
                            break
                    else:
                        print("Account does not exists.")

                    print("~" * 40)
                    decision = input("Do you want to delete another account ? y/n : ")
                    print("~" * 40)
                    if decision.lower() == "n":
                        break

            elif no == 7:
                break
            else:
                print("You can only choose from the available options.")


perform_obj = Perform_Operation()
perform_obj.perform()
