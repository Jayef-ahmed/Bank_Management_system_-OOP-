from abc import ABC
import random
from Bank import Bank

class User(ABC):
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
        

    
class Customer(User):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address)
        self.account_type = account_type
        self.account_no = random.randint(1000,9999)
        self.__balance = 0
        self.transaction_history = []
        self.loan_limit = 0

    def get_balance(self):
        return self.__balance

    def deposit_amount(self, bank, amount):
        if amount > 0:
            self.__balance += amount
            bank.total_balance += amount
            hst = {"Deposit" : amount}
            self.transaction_history.append(hst)
            print(f"** {amount}tk Deposit successfully!! **")
        else:
            print("** Amount is less Than 1!! **")

    def withdraw_amount(self,bank, amount):
        if bank.is_bankrupt == False:
            if amount > self.__balance:
                print("** Withdrawal amount exceeded! **")
            elif amount < 0:
                print("** Amount is Negative **")
            else:
                self.__balance -= amount
                bank.total_balance -= amount
                hst = {"Withdraw" : amount}
                self.transaction_history.append(hst)
                print(f"** {amount}tk Withdrawal successfully!! **")
        else:
            print("** The bank is bankrupt! **")

    def available_balance(self):
        print(f"Available Balance is: {self.__balance}TK")

    def transactionHistory(self):
        print("*** Transaction History ***")
        for i in self.transaction_history:
            for keys,values in i.items():
                print(f"{keys} --> {values}")

    def take_a_loan(self, bank, amount):
        if self.loan_limit < 2:
            if amount > 0:
                if bank.total_balance >= amount:
                    if bank.loan_status == True:
                        self.__balance += amount
                        bank.total_balance -= amount
                        bank.total_loan += amount
                        self.loan_limit += 1
                        hst = {"loan" : amount}
                        self.transaction_history.append(hst)
                        print(f"** Your Loan {amount}TK Successfully added your account **")
                    else:
                        print("** You can't take Loan from bank **")
                else:
                    print("** Your request Amount is out of bank total balance **")
            else:
                print("** Your amount is less than 1 **")
        else:
            print("** Your Loan Limit Exceeded! **")

    def transfer_amount(self, amount, bank, account_no):
        find_acc = bank.find_account(account_no)
        if find_acc:
            if amount < 1:
                print("your request amount is less than 1")
            elif amount > self.__balance:
                print("** You bank balance is low **")
            elif bank.is_bankrupt == True:   
                print("** The bank is bankrupt!! **")
            else:
                find_acc.__balance += amount
                self.__balance -= amount
                hst = {"Transfer" : amount}
                self.transaction_history.append(hst)
                print(f"** {amount}tk successfully transfer to {find_acc.name} **")
                print(f"* Your account balance is : {self.__balance} *")
        else:
            print("** Account does not exist **")

class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def delete_account(self, bank, account_no):
        bank.del_account(account_no)
        
    def see_account_list(self, bank):
        bank.see_accounts()

    def total_available_balance(self, bank):
        print(f"Available Balance is : {bank.total_balance}")

    def check_total_loan(self, bank):
        print(f"Total loan is : {bank.total_loan}")

    def loan_feature(self, bank, select):
        if select == 1:
            bank.loan_status = True
            print("loan feature is ON Successfully!")
        elif select == 2 :
            bank.loan_status = False
            print("Loan feature is OFF Successfully!")
        else:
            print("Invalid!!")

    def bankrupt(self, bank, select):
        if select == 1:
            bank.is_bankrupt = True
            print("Bankrupt ON Successfully!")
        elif select == 2 :
            bank.is_bankrupt = False
            print("Bankrupt is OFF Successfully!")
    