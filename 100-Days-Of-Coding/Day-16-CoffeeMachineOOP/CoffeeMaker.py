from MenuItem import MenuItem

class CoffeeMaker:
    def __init__(self) :
        self.resources = {"water": 300, "milk": 200, "coffee": 100}
    
    def is_resources_sufficient(self, menuItem:MenuItem):
        """ Returns true when order can be done  """
        for i in menuItem.ingredients:
            if menuItem.ingredients[i]> self.resources[i]:
                print(f"Sorry there is not enough {menuItem.ingredients[i]}.")
                return False
        return True
    
    def make_coffee(self,menuItem:MenuItem):
        for item in menuItem.ingredients:
           self.resources[item]-= menuItem.ingredients[item]
        print(f"Here is your {menuItem.name}")
    
    def GetReport(self):
        for key, value  in self.resources.items():
            print(f"{key}:{value}")