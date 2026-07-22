class BMW:
    def __init__(self, model):
        self.model = model
    def fuel_type(self):
        return "Diesel or Electric"
    def max_speed(self):
        return "250 km/h"
class Ferrari:
    def __init__(self, model):
        self.model = model

    def fuel_type(self):
        return "High-octane Petrol"
    def max_speed(self):
        return "340 km/h"
# 1. Demonstration using an iterable Loop
print("--- Polymorphism via Iteration ---")
car_instances = [BMW("M4"), Ferrari("SF90")]
for car in car_instances:
    print(f"{car.__class__.__name__} {car.model}:")
    print(f"  Fuel: {car.fuel_type()}")
    print(f"  Top Speed: {car.max_speed()}")
print("\n--- Polymorphism via a Function ---")
def display_car_performance(car_object):
    # The function accepts any object that contains these methods
    print(f"This vehicle reaches {car_object.max_speed()} using {car_object.fuel_type()}.")
bmw_car = BMW("i8")
ferrari_car = Ferrari("F8")
display_car_performance(bmw_car)
display_car_performance(ferrari_car)