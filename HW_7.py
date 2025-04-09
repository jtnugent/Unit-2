'''
Name: JT Nugent
'''
class Restaurant:
    def __init__(self, restaurant_name : str, cuisine_type : str) -> None:

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
            print(f"Restaurant is named {self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self) -> None:
            print("Restaurant is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name : str, cuisine_type = 'ice cream'):
        self.flavors = []
    def show_flavors(self):
        print("We currently have the flavors")
        for i in range(len(self.flavors)):
            print(f"{self.flavors[i]} ", end="")



class User:
    def __init__(self, first_name : str, last_name : str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self) -> None:
        print(f"Name is {self.first_name} {self.last_name}")

    def greet_user(self) -> None:
        print(f"Hello {self.first_name} {self.last_name}!")  
    
class Admin(User):
    def __init__(self):
        self.priviledges = Priviledges()

class Priviledges():
    def __init__(self, priviledges = []):
        self.priviledges = priviledges

    def show_priviledges(self):
        print()
        for i in range(len(self.priviledges)):
            print(f"{self.priviledges[i]} ", end="")


def main():
    ice_cream = IceCreamStand("Ice Cream!")
    ice_cream.flavors = ["vanilla","chocolate"]
    ice_cream.show_flavors()

    admin_one = Admin()
    admin_one_priviledges = ["can edit"]
    admin_one.priviledges.priviledges = admin_one_priviledges
    admin_one.priviledges.show_priviledges()





if __name__ == '__main__':
    main()