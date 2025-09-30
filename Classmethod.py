class Account:
    def __init__(self, bal , acc , dharak):
        self.bal = bal
        self.acc = acc
        self.dharak = dharak
        
    def debit(self, amt):
        self.bal = self.bal - amt
        print("Hey",self.dharak,"your account is debited by: ",amt)
        print("Remaining Balance: ",self.tot(),"\n")
        
    def credit(self, amt):
        self.bal = self.bal + amt
        print("Hey",self.dharak,"your account is credited with: ",amt)
        print("Remaining Balance: ",self.tot(),"\n")
        
    def tot(self):
        return self.bal
        
acc1 = Account(1000,676767,"Asim")
print("Account Balance: ",acc1.bal)
print("Account Number: ",acc1.acc)
print("Account Holder: ",acc1.dharak,"\n\n")
acc1.debit(100)
acc1.credit(1000)
print("\n\n")
acc2 = Account(100000,99999999999,"Hina Khan")
print("Account Balance: ",acc2.bal)
print("Account Number: ",acc2.acc)
print("Account Holder: ",acc2.dharak,"\n\n")
acc2.debit(100)
acc2.credit(1000)