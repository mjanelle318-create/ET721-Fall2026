"""
Janelle Moncrieffe
lab 5: review of clas, objects, methods, and attributes
Sep 16, 2026
"""
print("\n-----example 1-----")

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.pi = 3.14159

    # method
    def circumference(self):
        return 2 * self.pi * self.radius


# create instance object of the class
c1 = Circle(2, "red")

print(c1.color)
print(c1.circumference())


print("\n-----example 2-----")
class Rectangle():
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

        # method to calculate the area
        def area(self):
            return self.w * self.h

        # method to calculate the perimeter
        def perimeter(self):
            return 2* self.w + 2*self.h

        # mthod to draw rectangle itself
        """
        def drawRectangle(self):
            plt.gca().add_patch(plt.Rectangle((0,0), self.w, self.h, fc=self.c))
            plt.axis('scaled')
            plt.show()
"""
# create instance object of the class
r1 = Rectangle(2,3, "olive")
print(f"the perimeter of rectangle with height = {r1.h} and width {r1.w} is {r1.perimeter()}")

"""
car dealership's inventory management system
you are working on a python program to stimulate a car dealership's inventory management system. The system aims to model cars and their attributes
Task 1: create a class to represent each vehicle. Each car should have attributes for maximum speed and mileage
Task 2: update the class with the default color for all vehicles, "white"
Task: create a class method to assign seating capacity to a vehicle
Task 4: create a class method to display all the properties of an object class --> "the __ (color) car has __ seats, with ___ miles and maximum speed of ___" 
Task 5: create two instance objects of the car, One car will have a max speed of 200kph and mileage of 50000 kmpl with five seatign capacity. The other car max speed = 180 kph, mileage = 750000 kmpl, four seating
"""

