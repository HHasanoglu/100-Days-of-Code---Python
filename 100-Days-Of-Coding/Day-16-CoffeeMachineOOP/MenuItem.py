class MenuItem:
    def __init__(self, name: str, water: str, coffee: str, milk: str, cost: float):
        self.name = name
        self.cost=cost
        self.ingredients = {"water": water, "coffee": coffee, "milk": milk}

