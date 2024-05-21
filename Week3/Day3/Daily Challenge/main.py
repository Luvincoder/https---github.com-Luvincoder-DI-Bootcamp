from math import pi

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
print(circle1.diameter)  
print(circle2.area) 

circle3 = Circle(radius=3)
circle4 = Circle(radius=7)
print(circle3 + circle4)  

print(circle3 < circle4)  
print(circle3 == circle4)  

circles_list = [circle1, circle2, circle3, circle4]
sorted_circles = sorted(circles_list)
print(sorted_circles)  

