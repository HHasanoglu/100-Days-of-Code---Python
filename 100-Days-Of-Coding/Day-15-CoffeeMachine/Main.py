from pickle import TRUE


MENU={
    "espresso":{
                "ingredients":
                {
                    "water":50,
                    "coffee":18,
                },
                "cost":1.5
            },        
    "latte":{
                "ingredients":
                {
                    "water":200,
                    "milk":150,
                    "coffee":24,
                },
                "cost":2.5
            },
    "cappuccino":{
                    "ingredients":
                    {
                        "water":250,
                        "milk":100,
                        "coffee":24,
                    },
                    "cost":3.0   
                 }
    }


resources={
    "water":300,
    "milk":200,
    "coffee":100
}


profit=0
def is_resources_sufficient(ingredients:dict):
    """ Returns true when order can be done  """
    for ingredient in ingredients:
        if ingredients[ingredient]>resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def processCoins():
    """ Returns the total amount of money inserted """
    print("Please insert coins.")
    total= int(input(f"How many quarters?: "))*0.25
    total+= int(input(f"How many dimes?: "))*0.1
    total+= int(input(f"How many nickles?: "))*0.05
    total+= int(input(f"How many pennies?: "))*0.01
    return total
    

def isTransactionSuccessful(moneyRecived:float, drinkCost:float):
    """ Returns true if the payment is successful, false if payment is insufficient"""
    if moneyRecived>=drinkCost:
        global profit
        profit+=drinkCost
        change=round(moneyRecived-drinkCost,2)
        print(f'Here is your ${change} in change')
        return True
    else:
        print('Sorry thats not enough money, Money refunded')
        return False

def make_coffee(drink_name:str, order_ingredients:dict):
    for item in order_ingredients:
       resources[item]-= order_ingredients[item]
    print(f"Here is your {drink_name}")
    


isOn=True
while isOn:
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        isOn=False
    elif choice=="report":
        for key, value  in resources.items():
            print(f"{key}:{value}")
        print(f"money:${profit}")
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment=processCoins()
            if isTransactionSuccessful(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])
            
            
        
        
        