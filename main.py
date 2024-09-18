from user import Customer, Admin
from Bank import Bank

def login_user(acc):
    while True:
        print("1. Available Balance")
        print("2. Transaction History")
        print("3. Take a Loan")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer Amount")
        print("7. Exit")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            print(f"** Your account balance is: {acc.get_balance()}tk **")
        elif ch == 2:
            acc.transactionHistory()
        elif ch == 3:
            amount = int(input("Enter your loan amount : "))
            acc.take_a_loan(Islami_bank, amount)

        elif ch == 4:
            amount = int(input("Enter your deposit amount : "))
            acc.deposit_amount(Islami_bank, amount)

        elif ch == 5:
            amount = int(input("Enter your withdraw amount : "))
            acc.withdraw_amount(Islami_bank, amount)

        elif ch == 6:
            account_no = int(input("Enter reciver Account Number : "))
            amount = int(input("Enter your transfer amount : "))
            acc.transfer_amount(amount, Islami_bank, account_no)

        elif ch == 7:
            return
        else:
            print("** Invalid input **")

def create_user():
    while True:
        print("1. Login")
        print("2. Registration")
        print("3. Main Page")
        ch = int(input("Enter Your choice: "))

        if ch == 1:
            name = input("Enter your Name : ")
            account_no = int(input("Enter your Account No : "))
            for acc in Islami_bank.accounts:
                if acc.account_no == account_no and acc.name.lower() == name.lower():
                    print("** Login Successfully **")
                    print(f"Welcome {acc.name}")
                    login_user(acc)
                    break
            else:
                print("** User Not Found **")

        elif ch == 2:
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")
            address = input("Enter Your Address: ")
            print("Account type:")
            print("1. Savings")
            print("2. Current")
            type = int(input("Choose: "))
            account_type = ""

            if type == 1:
                account_type = "Savings"
            elif type == 2:
                account_type = "Current"
            user = Customer(name, email, address, account_type)

            Islami_bank.create_account(user)
            print(f"Registration Successfully!! \n(Your Account number is : {user.account_no})")

        elif ch == 3:
            return
        else:
            print("Invelid input!")

def admin_login():
    while True:
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        ch = int(input("Enter Your choice: "))

        if ch == 1:
            name = input("Enter your Name: ")
            email = input("Enter your Email: ")
            for ad in Islami_bank.admins:
                if ad.name == name and ad.email == email:
                    print("** Login Successfully **")
                    while True:
                        print("1. Delete User Account")
                        print("2. Show All Users")
                        print("3. Total bank balance")
                        print("4. Total loan amount")
                        print("5. On or Off the loan feature")
                        print("6. Bankrupt ON or Off")
                        print("7. Exit")
                        ch = int(input("Enter Your choice: "))

                        if ch == 1:
                            ac_no = int(input("Enter the Account Number: "))
                            ad.delete_account(Islami_bank, ac_no)
                        elif ch == 2:
                            ad.see_account_list(Islami_bank)
                        elif ch == 3:
                            ad.total_available_balance(Islami_bank)
                        elif ch == 4:
                            ad.check_total_loan(Islami_bank)
                        elif ch == 5:
                            print("1. On")
                            print("2. Off")
                            select = int(input())
                            ad.loan_feature(Islami_bank, select)
                        elif ch == 6:
                            print("1. On")
                            print("2. Off")
                            select = int(input())
                            ad.bankrupt(Islami_bank, select)
                        elif ch == 7:
                            return
                        else:
                            print("** Invalid Input **")
            else:
                print("** Admin Not Found **")


        elif ch == 2:
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")
            address = input("Enter Your Address: ")
            admin = Admin(name, email, address)
            Islami_bank.admin_create(admin)

        elif ch == 3:
            return
        else:
            print("** Invalid Input **")

Islami_bank = Bank("islami_Bank", "Moulvibazar")

while True:
    print("****Welcome!****")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    ch = int(input("Enter Your choice: "))

    if ch == 1:
        create_user()
    elif ch == 2:
        admin_login()
    elif ch == 3:
        break
    else:
        print("Invelid input!")
    
