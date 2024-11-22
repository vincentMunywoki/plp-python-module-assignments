class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing 🚢"

# Creating instances of each class
car = Car()
plane = Plane()
boat = Boat()

# Polymorphism in action: calling move() on each object
print(car.move())  
print(plane.move())  
print(boat.move())  
