'''
Name: JT Nugent
'''
class Restaurant:
    number_served = 0

    def __init__(self, restaurant_name : str, cuisine_type : str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
            print(f"Restaurant name: {self.restaurant_name}\nRestaurant cuisine: {self.cuisine_type}")

    def open_restaurant(self) -> None:
            print(f"{self.restaurant_name} is open")

    def set_number_served(self, number) -> None:
        self.number_served = number

    def increment_number_served(self,increment_number) -> None:
        self.number_served = self.number_served + increment_number
        print(self.number_served)
        return self.number_served



class User:
    login_attempts = 0

    def increment_login_attempts(self)-> None:
        self.login_attempts = self.login_attempts +1
        print(self.login_attempts)
    
    def reset_login_attempts(self)-> None:
        self.login_attempts = 0
        print(self.login_attempts)

    def __init__(self, first_name : str, last_name : str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self) -> None:
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}")

    def greet_user(self) -> None:
        print(f"Welcome {self.first_name}!")    

def main():
    
    restaurant_one = Restaurant("Fat Joes","Barbeque")
    restaurant_one.set_number_served(5)
    restaurant_one.increment_number_served(5)
    login = User("James","Nugent")
    login.increment_login_attempts()
    login.reset_login_attempts()


if __name__ == '__main__':
    main()