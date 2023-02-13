
# Use a factory pattern to create a burger 


class Burger:
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

# create a class that will insantiate the burger 

class BurgerFactory:

    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createSuperCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty", "tomato", "onions"]
        return Burger(ingredients)
    
    def createVeggieCheeseBurger(self):
        ingredients = ["bun", "cheese", "veggie-patty", "tomato", "onions"]
        return Burger(ingredients)

burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createSuperCheeseBurger().print()
burgerFactory.createVeggieCheeseBurger().print()
