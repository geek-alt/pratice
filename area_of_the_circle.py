import math

print("Welcome to area of circle calculator")

# Area of circle = Pi*r^2

radius = float(input("Enter the radius of a cirlce: "))

#area = math.pi * radius ** 2

area = math.pi * pow(radius, 2)

print(f"The area of your circle by given radius is {round(area, 2)}cm²!")