class Atm:

    def __init__(self, number, pin):
        self.number = number
        self.pin = pin

    def bankBalance(self):
        print(" You got nun😇 ")

    def cashWithdrawl(self, amount):
        remainingBalance = 0-amount
        print(" You have withdrawn " +str(amount)+". Your remaining balance is"+str(remainingBalance))

        if (remainingBalance <0):
            print(" Insufficient funds!! ")

def main():

    Number = input(" Enter Your card number: ")
    Pin = input( " Enter your pin: ")


    new_user = Atm(Number, Pin)

    new_user.bankBalance()

    amount = int(input(" Enter the amount to be withdrawn: ")) 
    new_user.cashWithdrawl(amount)

if __name__ == "__main__":
    main()