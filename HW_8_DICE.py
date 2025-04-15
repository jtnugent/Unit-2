import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1,self.sides))

class Ticket:
    def __init__(self, lucky_ticket, guess_list, counter = 0):
        self.guess_list = guess_list
        self.lucky_ticket = lucky_ticket
        self.counter = counter

    def create_ticket(self):
        possible_list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
        for i in range(2):
            self.guess_list.append(random.choice(possible_list))
        print(self.guess_list)
        print()
        self.counter += 1
        return self.guess_list

    def check_ticket(self):
        if self.guess_list == self.lucky_ticket:
            return False

    def win(self):
        pass


def main():
    possible_list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
    lucky_list = []
    for i in range(2):
        lucky_list.append(possible_list[random.randint(1,len(possible_list)-1)])
    print(f"Any ticket matching {lucky_list} WINS!")
    Win = True
    ticket_checker = Ticket(lucky_list,[])
    while Win:
        ticket_checker.create_ticket()
        ticket_checker.check_ticket()
        if ticket_checker.check_ticket():
            Win = False
            counter = ticket_checker.win()
    print(f"Win took {counter} attempts.")

main()
