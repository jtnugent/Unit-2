class Lawnmower:
    def __init__(self, gasoline : 0, running : False, blade_height : 0.5) -> None:
        self.gasoline = gasoline
        self.running = running
        self.blade_height = blade_height
    
    def start_lawnmower(self):
        self.running = True

    def adjust_blade(self):
        blade_adjust = float(input("How would you like to adjust the blade? (negative goes down)"))
        self.blade_height = self.blade_height + blade_adjust

    def gasoline_refill(self):
        gas = str.lower(input("Would you like to refill your gas? "))
        if gas == "yes":
            self.gasoline = 100

    def lawnmower_stats(self):
        print(f"Lawnmower started: {self.running}")
        print(f"Lawnmower Blade Hieght: {self.blade_height}")
        print(f"Gasoline Level: {self.gasoline}")



def main():
    lawnmower_one = Lawnmower(60,False,0.5)
    lawnmower_one.gasoline_refill()
    lawnmower_one.start_lawnmower()
    lawnmower_one.adjust_blade()
    lawnmower_one.lawnmower_stats()


if __name__  == "__main__":
    main()