class ATM():

    def __init__(self):
        self.ATMNumber=""
        self.pinNumber=""
        self.Amount=""

    def enterATMNumber(self):
        self.ATMNumber=int(input("Enter Your ATM Number"))
    def enterPinNumber(self):
        self.pinNumber=int(input("Enter Your Pin Number"))
    def enterAmount(self):
        self.Amount=int(input("Enter Amount For Withdrawl"))
    def withdrawl(self,Amount):
        self.Amount=self.Amount-Amount
        print("Done")
    def balanceEnquiry(self):
        print(self.Amount)
def main():
    Customer1=ATM()
    Customer1.enterATMNumber()
    Customer1.enterPinNumber()
    Customer1.balanceEnquiry()
    Customer1.enterAmount()
    Customer1.withdrawl(2000)
main()


      