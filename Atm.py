class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber 
        self.pin = pin

    def BankBalance(self):
        print("Your Bank-Balance is 50,000")     
   
    def withDraw(self,amount):
        newAmount = 50000 - amount
        print("Your have Withdrawn "+str(amount)+". Now, your Bank-Balance is " +str(newAmount))
   
def main():
    card_number = input("Enter Your Card Number : ")
    pin_number = input("Enter Your Pin : ")

    newUser = Atm(card_number,pin_number)
    print("Choose An Activity")
    print("1) Check Bank-Balance   2) WithDraw Cash")
    activity = int(input("Enter The Activity Number : "))
    if (activity == 1):
        newUser.BankBalance()
    elif (activity == 2):
        amount = int(input("Enter The Amount To WithDraw : "))
        newUser.withDraw(amount)
    else:
        print("The number you have entered is invalid, Enter a valid number") 
if __name__ == "__main__":
    main()           







