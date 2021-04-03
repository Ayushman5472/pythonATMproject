class ATM (object):
    def __init__(self, cardNumber, pinNumber, cash):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.cash = cash
    
    def cashWithdraw(self, cardNumber, pinNumber, cash):
        if cardNumber==self.cardNumber and pinNumber == self.pinNumber:
            self.cash = self.cash- cash
            print('available balance =' + str(self.cash))
        else:
            print("Please give the right information")
    
    def balance(self, cardNumber, pinNumber):
        if cardNumber==self.cardNumber and pinNumber == self.pinNumber:
            print('available balance =' + str(self.cash))
        else:
            print("Please give the right information")

Card1 = ATM(1234,123,1000)
Card1.balance(1234,123)
Card1.cashWithdraw(1234,123,200)