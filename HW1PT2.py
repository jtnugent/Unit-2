'''
Name: JT Nugent


'''
class Restaurant:
    number_served = 0

    def __init__(self, restaurant_name : str, cuisine_type : str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
            print(f"Restaurant is named {self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self) -> None:
            print("Restaurant is open!")

    def set_number_served(self) -> None:
        self.number_served = int(input("How many served today total? "))

    def increment_number_served(self,increment_number) -> None:
        self.number_served = self.number_served + increment_number
        print(self.number_served)
        return self.number_served



class User:
    login_attempts = 0

    def increment_login_attempts()-> None:
        pass

    def __init__(self, first_name : str, last_name : str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self) -> None:
        print(f"Name is {self.first_name} {self.last_name}")

    def greet_user(self) -> None:
        print(f"Hello {self.first_name} {self.last_name}!")    

def main():
    
    restaurant_one = Restaurant("Fat Joes","Barbeque")
    restaurant_one.set_number_served()
    restaurant_one.increment_number_served(5)

if __name__ == '__main__':
    main()