# car.py

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")

# Test the class
if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2020)
    car.display_info()  # Output: Car: Toyota Corolla, Year: 2020
