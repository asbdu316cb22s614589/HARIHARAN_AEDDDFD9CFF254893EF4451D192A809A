class BankAccount:
    balance=0
    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
    def deposit(self,amount):
        self.balnce-=amount
        return self.balance
    def balanceCheck(self):
        print("\n New balance is..Rs.{}".format(self.balance))
    def bal_return(self):
        return(self.balance)
BT=BankAccount()
while True:
    print("1.Deposit\n")
    print("2.Withdraw\n")
    print("3.Balance\n")
    print("4.Exit\n")
    ch=int(input("Enter yout choice.."))
    if ch==1:
        while True:
            amt=int(input("Enter amount to Deposit..."))
        if amt>0:
            BT.deposit(amt)
            break
        else:
            print("Enter Valid Amount")
            continue
    if ch==2:
        while True:
            amt=int(input("Enter amount to withdraw..."))
            if BT.bal_return()>amt:
                BT.withdraw(amt)
                break
            else:
                BT.balanceCheck()
                print("\n Low Balance,Please Enter Less Amount..")
                continue
            if ch==3:
                BT.balanceCheck()
            if ch==4:
                break
