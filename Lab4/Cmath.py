#ex1
import math
D = int(input())
print(math.radians(D))

#ex2
import math
H = float(input("Height:"))
B1 = float(input("B1:"))
B2 = float(input("B2:"))
print(1/2*H*(B1+B2))

#ex3
import math

a = int(input("Number of sides: "))
b = int(input("Length of side: "))

x = b / (2 * math.tan(math.pi / a))
p = a * b
S =   (x * p)/2

print("Area of the regular polygon:", S)

#ex4
import math
L = int(input("Length of base:"))
H = int(input("Height:"))
print(L * H)