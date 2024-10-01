# Calculate a circumference of circle
import math
#Formula is 2*pi*r

# We will import math module , which will be helpful for this exercise.
pi = math.pi

print("Welcome to program made for calculating circumference of a circle")

r = float(input("Enter the radius value of a circle: "))

circumference_value_of_circle = 2*pi*r

#total= math.ceil(circumference_value_of_circle)
total = round(circumference_value_of_circle,2)
print(f"The circumference value of your circle is {total} cm.")