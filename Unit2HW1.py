'''
Name: JT Nugent


'''
class Restaurant:
    def __init__(self, restaurant_name : str, cuisine_type : str) -> None:

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
            print(f"Restaurant name: {self.restaurant_name}\nRestaurant cuisine: {self.cuisine_type}")

    def open_restaurant(self) -> None:
            print(f"{self.restaurant_name} is open")



class User:
    def __init__(self, first_name : str, last_name : str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self) -> None:
        print(f"First Name: {self.first_name} {self.last_name}")

    def greet_user(self) -> None:
        print(f"Welcome {self.first_name}!")    

def main():
    restaurant_one = Restaurant("Foodie","Fast")
    restaurant_two = Restaurant("BIGBOY","Barbeque")
    restaurant_three = Restaurant("Senor Taco","Mexican")

    restaurant_one.describe_restaurant()
    restaurant_one.open_restaurant()
    restaurant_two.describe_restaurant()
    restaurant_two.open_restaurant()
    restaurant_three.describe_restaurant()
    restaurant_three.open_restaurant()

    user_one = User("John","Jims")
    user_two = User("Big","Joe")
    user_three = User("Banana","Man")

    user_one.describe_user()
    user_one.greet_user()
    user_two.describe_user()
    user_two.greet_user()
    user_three.describe_user()
    user_three.greet_user()

if __name__ == '__main__':
    main()