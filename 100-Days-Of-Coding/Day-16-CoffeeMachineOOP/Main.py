from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine
from Menu import Menu



menu=Menu()
coffeeMaker=CoffeeMaker()
moneyMachine=MoneyMachine()

isOn=True
while isOn:
    choice=input(f"What would you like{menu.GetItems()}?:").lower()
    if choice == "off":
        isOn=False
    elif choice=="report":
        coffeeMaker.GetReport()
        moneyMachine.GetReport()
    else:
        drink=menu.FindDrink(choice)
        if coffeeMaker.is_resources_sufficient(drink) and moneyMachine.MakePayment(drink.cost):
                coffeeMaker.make_coffee(drink)
            
            
        
        
        