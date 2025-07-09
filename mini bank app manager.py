class Bank_account:
    def __init__(self,name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    def display_acct_info(self):
        print(f'''account name: {self.name}
account number: {self.account_num}
balanace: {self.balance}''')
all_account = []
choice1 = "yes"
while choice1 == "yes":
    name1 = input("Enter customer name ").lower()
    account_num1 = input("Enter customers account number ")
    balance1 = int(input("Enter your starting balance "))
    acct1 = Bank_account(name1, account_num1, balance1)
    all_account.append(acct1)
    print("account added successfully✅")
    choice1 = input("Do you still want to add another customer? ").lower()
choice2 = "yes"
quest = input("Do you want to deposit money?(yes|no) ").lower()
if quest == "yes":
    while choice2 == "yes":
        found = False
        dep_name = input("Enter account name ").lower()
        dep_num = input("enter account number ")
        deposit_money = int(input("Enter amount you want to deposit "))
        for x in all_account:
            if dep_num == x.account_num and dep_name == x.name:
                found = True
                x.balance += deposit_money
                print(f"{deposit_money} added successfully")
        if not found:
            print(("account not found"))
        choice2 = input("Do you want to make another deposit?(yes|no) ")
if quest == "no":
        print("Thank you for banking with us")
quest1 = input("Do you want to make a withdrawal? ").lower()
if quest1 == "yes":
    choice3 = "yes"
    while choice3 == "yes":
        found1 = False
        with_name = input("Enter account name ").lower()
        with_acct_num = input("Enter account number")
        with_amount = int(input("Ennter amount "))
        for y in all_account:
            if y.name == with_name  and y.account_num == with_acct_num:
                found1 = True
                print("account found✅")
                if with_amount <=  y.balance:
                    y.balance -= with_amount
                    print("money withdrawn successfully")
                else:
                    print("insufficient fund")
        if not found1:
            print("account not found❌")
        choice3 = input("Do you want to make another withdrawals(yes|no)? ")
if quest1 == "no":
    print("It is no problem at all😂")
ques2 = input("Do you want to check balance? ").lower()
choice4 = "yes"
if ques2 == "yes":
    while choice4 == "yes":
        found2 = False
        bal_name = input("Enter account name ").lower()
        bal_acct_num = input("enter account number ")
        for b in all_account:
            if bal_name == b.name and bal_acct_num == b.account_num:
                found2 = True
                print("account found✅")
                print(f"your current balance is {b.balance}")
        if not found2:
            print("Account not found")        
        choice4 = input("Do you still want to check balance? ").lower()
if ques2 == "no":
    print("No problem")
print("Thank you for banking with us🤝")