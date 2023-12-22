from MenuItem import MenuItem
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", water=50, coffee=18, milk=0, cost=1.5),
            MenuItem("latte", water=200, coffee=24, milk=150, cost=2.5),
            MenuItem("espresso", water=250, coffee=24, milk=100, cost=3.0),
        ]
        
    def GetItems(self):
        text=""
        for item in self.menu:
            text+=f"{item.name}/"
        return text;

    def FindDrink(self,OrderName:str):
        for item in self.menu:
            if item.name==OrderName:    
                return item
        print("Item Not Found")