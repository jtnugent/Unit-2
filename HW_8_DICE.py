import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1,self.sides))

class Ticket:
    def __init__(self, lucky_ticket, counter = 0):
        self.counter = counter
        self.lucky_ticket = lucky_ticket

    def create_ticket(self):
        possible_list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
        self.guess_list = []
        for i in range(1):
            self.guess_list.append(random.choice(possible_list))
        print(self.guess_list)
        print()
        self.counter += 1
        return self.counter

    def check_ticket(self):
        global winstate
        print("start")
        print(self.guess_list)
        print(self.lucky_ticket)
        print("end")
        if self.guess_list == self.lucky_ticket:
            return True

    def win(self):
        return self.counter


def main():
    global winstate
    winstate = False
    possible_list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
    lucky_list = []
    for i in range(1):
        lucky_list.append(possible_list[random.randint(1,len(possible_list)-1)])
    print(f"Any ticket matching {lucky_list} WINS!")
    Win = True
    ticket_checker = Ticket(lucky_list)
    for i in range(1000):
        ticket_checker.create_ticket()
        ticket_checker.check_ticket()
        if ticket_checker.check_ticket():
            Win = False
            counter = ticket_checker.win()
    print(f"Win took {counter} attempts.")

main()
