"""
JT Nugent
"""


class Kiosk:
    def getTotal(self,item_price) -> None:
        total_price = sum(self.price_list)

    def addItem(self) -> None:
        self.item_list = item_list
        self.price_list = price_list
        item_list = []
        price_list = []
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
        
    def newTransaction(self)-> None:
        transaction_start = str.lower(input("Would you like to start a new transaction? (yes/no) "))
        if transaction_start == "yes":
            self.addItem()


    def takePayment(self)-> None:
        payment = str(input(f"Your total is {sum(self.price_list)}.\nHow much will you pay?"))
        if payment < sum(self.price_list):
            print("You have not paid your bill. Try again")
        elif payment >= sum(self.price_list):
            change = payment - sum(self.price_list)
            print(f"Your change is {payment - sum(self.price_list)}")
            self.print_reciept(change)

    def finalizePurchase(self)-> None:
        total_items = len(self.item_list)
        total_price = sum(self.price_list)
        self.takePayment()

    def print_reciept(self,change)-> None:
        for i in range(len(self.item_list)):
            print(f"{self.item_list[i]}  {self.price_list[i]}")
            
        print(change)
    def reset_transaction(self)-> None:
        pass



def main():
    
    


main()