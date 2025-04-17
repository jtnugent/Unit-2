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
    def __init__(self, plant_choice, water, hunger, action, evo, day = 0):
        end = False
        self.end = end
        self.plant_choice = plant_choice
        self.water = water
        self.hunger = hunger
        self.action = action
        self.day = day
        self.evo = evo

    def menu(self):
        print(f"Actions Left: {self.action}    Day: {self.day}")
        print(f"Water: {self.water}%    Evo: {self.evo}%    Hunger: {self.hunger}%")
        print("1 - water (+50 water)\n2 - feed (+50 hunger)\n3 - trim (-50 evo)\n4 - wait")
        action = int(input("Choose.\n"))
        if action == 1:
            self.water = self.water+50
        elif action == 2:
            self.hunger = self.hunger+50
        elif action == 3:
            self.evo = self.evo - 50
        elif action == 4:
            pass
        self.action = self.action - 1
        if self.action <= 0:
            self.day_reset()
        
    def day_reset(self):
        self.set_day(1)
        if self.plant_choice == "tree":
            Tree.reset(self)
        elif self.plant_choice == "fern":
            Fern.reset(self)
        elif self.plant_choice == "succulent":
            Succulent.reset(self)
        self.action = 2

    def __repr__(self):
        #Checks if lost
        return f"{self.end}"
    
    def get_day(self):
        return self.day
    
    def set_day(self,x):
        self.day = self.day + x

    def stat_check(self):
        #If any stats are too large or too small it sends the info to the subclasses to get the correct message and image. 
        if self.hunger <=0 or self.hunger > 100 or self.water <= 0 or self.water > 100 or self.evo <=0 or self.evo >= 100:
            if self.plant_choice == "tree":
                Tree(self.hunger, self.evo, self.water).stat_check()
            if self.plant_choice == "succulent":
                Succulent(self.hunger, self.evo, self.water).stat_check()
            if self.plant_choice == "fern":
                Fern(self.hunger, self.evo, self.water).stat_check()
            self.end = True

    def __eq__(self, other):
        return self == other
    
    def __add__(self, other):
        return self + other


class Fern(Plant):
    def __init__(self, hunger, evo, water):
        self.hunger = hunger
        self.evo = evo
        self.water = water

    def stat_check(self):
        if self.hunger <= 0:
            print("Fern withered away")
            self.end = True
        elif  self.evo <=0:
            print("To skinny...")
            self.end = True
        elif self.water <= 0:
            print("Fern dried out")
            self.end = True
        if self.hunger > 100:
            print("BIG BOY")
            self.end = True
        elif self.evo >= 100:
            print("Fern Transformed")
            self.end = True
        elif self.water > 100:
            print("overwatered")
            self.end = True

    def reset(self):
        self.hunger = self.hunger-10
        self.water = self.water-40
        self.evo = self.evo+20

class Succulent(Plant):
    def __init__(self, hunger, evo, water):
        self.hunger = hunger
        self.evo = evo
        self.water = water

    def stat_check(self):
        if self.hunger <= 0:
            print("Succulent withered away")
            self.end = True
        elif  self.evo <=0:
            print("To skinny...")
            self.end = True
        elif self.water <= 0:
            print("Succulent dried out")
            self.end = True
        if self.hunger > 100:
            print("BIG BOY")
            self.end = True
        elif self.evo >= 100:
            print("Succulent Transformed")
            self.end = True
        elif self.water > 100:
            print("overwatered")
            self.end = True

    def reset(self):
        self.hunger = self.hunger-10
        self.water = self.water-10
        self.evo = self.evo+30
            
class Tree(Plant):
    def __init__(self, hunger, evo, water):
        self.hunger = hunger
        self.evo = evo
        self.water = water

    def stat_check(self):
        if self.hunger <= 0:
            print("Tree withered away")
            self.end = True
        elif  self.evo <=0:
            print("To skinny...")
            self.end = True
        elif self.water <= 0:
            print("Tree dried out")
            self.end = True
        if self.hunger > 100:
            print("oh...")
            self.end = True
        elif self.evo >= 100:
            print("Tree Transformed")
            self.end = True
        elif self.water > 100:
            print("overwatered")
            self.end = True

    def reset(self):
        self.hunger = self.hunger-20
        self.water = self.water-30
        self.evo = self.evo+40

def main():

    print(""" 
                                  
                            
                             
                              
                            
                              
                           
                              
                            
                      
        |---------------|                                     
        |               |                            
        |               |          |        |          |-------------------|                                 
        _________________          |________|          |___________________|      
""")
    plant_choice = str.lower(input("Would you like to choose a Fern, Tree, or Succulent?\n"))
    plant = Plant(plant_choice, 50, 50, 2, 50)
    end = False
    while end == False:
        plant.menu()
        plant.stat_check()

        if repr(plant).__eq__("True"):
            end = True
    
main()