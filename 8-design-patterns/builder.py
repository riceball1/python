# Builder pattern provides more control than the factory pattern
# allows more control of the individual parts


class Burger:
    def __init__(self) -> None:
        self.buns = None
        self.patty = None
        self.cheese = None
    
    # allows for print(<instance>) to work
    def __str__(self) -> str:
        return str([self.buns, self.patty, self.cheese])
    
    
    def setBuns(self, bunStyle):
        self.buns = bunStyle
    
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

class BurgerBuilder:
    def __init__(self) -> None:
        self.burger = Burger()

    # individual methods for each ingreidents
    # returns a reference to the builder, which allows method chaining

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self
    
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self

    # have a build method to return the final product
    def build(self):
        return self.burger

burger = BurgerBuilder().addBuns("sesame").addPatty("fish patty").addCheese("swiss cheese").build()

# builder pattern commonly used for protocol buffers

print(burger) # ["sesame", "fish patty", "swiss cheese"]

