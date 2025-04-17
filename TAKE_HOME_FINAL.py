"""
Garden Simulator
Water, trim, or feed plant
Plants options: Fern, Succulent, Tree
Stats: Water level, Evolution Level(caused by failure to trim), Hunger level(Overfeeding causes anomoly)
Time passes after two actions
Summary:
Water, trim, and feed your choice of plant to reach different
evolution states based off your choices.
"""



class Plant:
    def __init__(self, plant_choice, water_level, hunger, action, day):
        self.plant_choice = plant_choice
        self.water_level = water_level
        self.hunger = hunger
        self.action = action
        self.day = day

    def menu(self):
        print("1 - water\n2 - fee\n3 - trim\n4 - wait")
        action = str.input("Choose.\n")

    def __repr__(self):
        #acts as stats
        return self.water, self.evo, self.hunger, self.action, self.day
    
    def __add__(self):
        #Adds number to keep track of days.
        self.day +=1

    def __evolution__(self):
        pass

class Fern(Plant):
    def __init__(self, hunger, evo, water):
        self.hunger = hunger
        self.evo = evo
        self.water = water

    def stat_check(self):
        if self.hunger <= 0:
            print("Fern withered away")
        elif  self.evo <=0:
            print("To skinny...")
        elif self.water <= 0:
            print("Fern dried out")

class Succulent(Plant):
    def __init__(self, hunger, evo, water):
        self.hunger = hunger
        self.evo = evo
        self.water = water

    def stat_check(self):
        if self.hunger <= 0:
            print("Succulent withered away")
        elif  self.evo <=0:
            print("To skinny...")
        elif self.water <= 0:
            print("Succulent dried out")
            
class Tree(Plant):
    def __init__(self, hunger, evo, water):
        self.hunger = hunger
        self.evo = evo
        self.water = water

    def stat_check(self):
        if self.hunger <= 0:
            print("Tree withered away")
        elif  self.evo <=0:
            print("To skinny...")
        elif self.water <= 0:
            print("Tree dried out")

def main():
    pass

main()