class Vehicle:
    def __init__(self):
        pass

    def move(self):
        print("Vehicle can move.")

class Car(Vehicle):
    def __init__(self):
        pass

    def move(self):
        print("Car can move.")


car = Car()
print(car.move())