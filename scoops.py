class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        ingredients = self.ingredients
        toppings = self.toppings
        scooped = [[i,t] for i in ingredients for t in toppings]
        return scooped

        pass

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate", "rainbow"], ["chocolate sauce", "strawberry sauce", "nuts"])
    print(machine.scoops()) #should print all combinations of ice cream and toppings 