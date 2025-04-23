"""
JT Nugent
"""


class Kiosk:
    def __init__(self, transaction_ID : int)-> None:
        self.transaction_ID = transaction_ID

    def newTransaction(self)-> None:
        transaction_start = str.lower(input("Would you like to start a new transaction? (yes/no) "))
        if transaction_start == "yes":
            return transaction_start    

    def getTotal(self,item_price) -> None:
        total_price = sum(self.price_list)
        return total_price

    def addItem(self) -> None:
        item_list = []
        price_list = []
        self.item_list = item_list
        self.price_list = price_list
        while True:
            item = str(input("What are you buying?"))
            item_list.append(item)
            price = int(input("How much does it cost?"))
            price_list.append(price)
            done = str.lower(input("Are you done shopping?(yes/no)"))
            if done == "yes":
                return item_list, price_list
            else:
                print(f"{item_list}\n{price_list}")

    def takePayment(self)-> None:
        payment = int(input(f"Your total is {self.getTotal(self.price_list)}.\nHow much will you pay?"))
        if payment < sum(self.price_list):
            print("You have not paid your bill. Try again")
        elif payment >= sum(self.price_list):
            change = payment - sum(self.price_list)
            print(f"Your change is {payment - sum(self.price_list)}$")
            self.print_reciept(change)

    def finalizePurchase(self)-> None:
        total_items = len(self.item_list)
        total_price = sum(self.price_list)
        return total_items, total_price

    def print_reciept(self,change)-> None:
        print("Item     Cost")
        for i in range(len(self.item_list)):
            print(f"{self.item_list[i]}    {self.price_list[i]}")
            
        print()
        print(f"Change : {change}$")
        print(f"Transaction_ID: {self.transaction_ID}")
    def reset_transaction(self)-> None:
        self.item_list = []
        self.price_list = []



def main():
    import random
    transaction_ID = random.randint(1000000000,9999999999)
    transaction_one = Kiosk(transaction_ID)
    transaction = transaction_one.newTransaction()
    if transaction == "yes":
        item_list, price_list = transaction_one.addItem()
        total_items, total_price = transaction_one.finalizePurchase()
        transaction_one.takePayment()



main()