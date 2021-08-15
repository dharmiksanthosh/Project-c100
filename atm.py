import stdiomask

class Atm(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
        
    def balenceinquiry(self):
        print("Your balance is ₹1000")

    def cashwidthdrawel(self, amount):
        new_amount = 1000-amount
        print("You withdrawed: " + str(amount) + " Your remaining balance is " + str(new_amount))
    
def main():
    name = input("Hello, what is your name?\n")
    print("Hello, " + name)
    cardnumber = input("Enter Your card number: ")
    pin = stdiomask.getpass()
    new_user = Atm(cardnumber, pin)

    print('Choose Your activity')
    print('1. Balance Inquiry')
    print('2. Cash Withdrawel')
    activity = int(input('Enter your activity choice: '))

    if activity == 1:
        new_user.balenceinquiry()
    elif activity == 2:
        amount = int(input('Enter the amount: '))
        new_user.cashwidthdrawel(amount)
    else:
        print('Enter a valid number choice')

if __name__ == "__main__":
    main()