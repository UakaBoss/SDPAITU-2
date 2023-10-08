

# Base Coffee class
class Coffee:
    def cost(self):
        return 5.0

# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.dec_coffee = coffee

    def cost(self):
        return self.dec_coffee.cost()

# Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.dec_coffee.cost() + 1.2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.dec_coffee.cost() + 0.5

class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return self.dec_coffee.cost() + 1.5



# Main code
if __name__ == "__main__":

    my_coffee = Coffee()
    print("Hello, your coffee costs 5$, do you want add some topics?")
    print("Type *milk*, *sugar*, *chocolate* or *end* to leave")

    # Menu
    while(True):
        user = input()
        match(user):
            case "milk":
                my_coffee = MilkDecorator(my_coffee)
                print("You added milk, it costs 1.2$")
            case "sugar":
                my_coffee = SugarDecorator(my_coffee)
                print("You added sugar, it costs 0.5$")
            case "chocolate":
                my_coffee = ChocolateDecorator(my_coffee)
                print("You added chocolate, it costs 1.5$")
            case "end":
                total_cost = my_coffee.cost()
                print("Total cost for your coffee is: $", total_cost)
                break