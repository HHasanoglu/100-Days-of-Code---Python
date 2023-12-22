from locale import currency
from tkinter import CURRENT, SEL


class MoneyMachine:
    
    CURRENCY="$"
    COIN_VALUES={"quarter":0.25,
            "dimes":0.1,
            "nickles":0.05,
            "pennies":0.01}
    
    def __init__(self) :
        self.profit=0
    
    
    def processCoins(self):
        """ Returns the total amount of money inserted """
        total=0
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            total+= int(input(f"How many {coin}?: "))*self.COIN_VALUES[coin] 
        return total
    
    def MakePayment(self,drinkCost:float):
        """ Returns true if the payment is successful, false if payment is insufficient"""
        total= self.processCoins()
        if total>=drinkCost:
            self.profit+=drinkCost
            change=round(total-drinkCost,2)
            print(f'Here is your {change} in change')
            return True
        else:
            print('Sorry thats not enough money, Money refunded')
            return False

    def GetReport(self):
        """Print the Current Profit"""
        print(f"money:{self.CURRENCY}{self.profit}")