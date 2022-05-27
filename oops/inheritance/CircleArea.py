
import math
from ShapeArea import ShapeArea

class CircleArea(ShapeArea):
    def __init__(self, type, radius):
        super().__init__(type) # calling super class constructor with the help of super keyword
        self.radius = radius
        
    def get_area(self):
        return math.pi * pow(self.radius, 2)
    


# create an object of Circle Shape
circle = CircleArea('circle', 5)

print("Area of the circle is : "+ str(round(circle.get_area(), 2)))

print('Getting color of the circle : ' + circle.get_color()) # calling super class method using inheritance.

# now we can find the aread of hemishere , .... we're inheriting

# Event multiple inheritance is possible

# class Hemishphere(ShapeArea, CircleArea): will give error 
# class Hemishphere(CircleArea, ShapeArea): this is fine [order matters]
# https://stackoverflow.com/a/42567588/9898251 [Stackoverflow discussion]

class Hemishphere(CircleArea):
    pass # CicleArea already inherits ShapeArea and Hemisphere inherits both ...

 # Polymorphism [method overriding]

class A:
    def explore(self):
        print("explore() method from class A")

class B(A):
    def explore(self):
        super().explore()  # calling the parent class explore() method
        print("explore() method from class B")


b_obj = B()
b_obj.explore()

# Just like java extends Object by default and allows us to override methods like toString()
class Demo(object):
   def __init__(self, demo_value):
       self.demo_value = demo_value

   def __str__(self):
       return "Demo Value is : " + self.demo_value   

demo = Demo('Python Inheritance')
print(demo) # invokes __str__() method
