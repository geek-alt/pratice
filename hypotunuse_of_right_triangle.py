#Trigonometry
import math
# formula c = sqrt a² + b²

a = float(input("Enter the value of side a: "))
b = float(input("Enter the value of side b: "))


c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {round(c,4)}")