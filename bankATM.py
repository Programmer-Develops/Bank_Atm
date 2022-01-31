class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin=pin
    def Check_balance(self):
        print("your balance is 50000")
    
    def with_drawl(self,amount):
        new_amount=50000-amount
        print("you have withdrawm"+str(amount)+".your leftOver balance is"+str(new_amount))

def main():
    CardNumber =int(input("enter your card number :"))
    PinNumber =int(input("Enter your pin number :"))
    
    print("choose an activity")
    print("1. Check balance 2.Withdraw")

    user = Atm(CardNumber, PinNumber)
    activity = int(input("Choose an activity 1 or 2 :"))

    if activity == 1 :
        user.Check_balance()
    elif activity == 2:
        amount= int(input("enter your amount"))
        user.with_drawl(amount)
    else:
        print('enter a valid id')

if __name__ == "__main__":
    main()