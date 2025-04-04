import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1,self.sides))


def main():
    possible_list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
    lucky_list = []
    for i in range(4):
        lucky_list.append(possible_list[random.randint(1,len(possible_list)-1)])
    print(f"Any ticket matching {lucky_list} WINS!")
    """six_sided = Die()
    ten_sided = Die(10)
    twenty_sided = Die(20)
    for i in range(10):
        six_sided.roll_die()
        ten_sided.roll_die()
        twenty_sided.roll_die()

"""
main()
