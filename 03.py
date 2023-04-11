# Write a program to convert US dollars to Indian Rupees:
us = 81.71
indian = 500
output = indian * us
print(indian, "Rupees in Dollars is", int(output), "\n")

# Write a program to convert bits to Megabytes, Gigabytes, and Terabytes:
B = 8589934592
KB = B/1024
MB = B/(1024 * 1024)
GB = B/(1024 * 1024 * 1024)
TB = B/(1024 * 1024 * 1024 * 1024)
print(B, "Bits in MB is: ", MB)
print(B, "Bits in GB is: ", GB)
print(B, "Bits in TB is: ", TB, "\n")

# Write a program to find the square root of a number:
no = 125
result = no ** 0.5
print(no, "square root is", int(result), "\n")

# Write a program to find the area of rectangle:
h = 40
w = 20
area = h * w
print("Area of rectangle with height of", h, "cm and width of", w, "cm is:", area, "cm \n")

# Write a program to calculate area and perimeter of the square:
Side = 20
SArea = Side * Side
Perimeter = 4 * Side
print("The area of a square is", SArea, "cm and perimeter of the square is", Perimeter, "cm \n")

# Write a program to calculate surface volume and area of the cylinder:
pi = 3.14
height = 30
radius = 20
volume = pi * height * radius
CArea = ((2 * pi * radius) * height) + ((pi * radius ** 2) * 2)
print("Surface volume of cylinder is", volume, "cm and Area of the cylinder is", CArea, "cm \n")

# Write a program to swap the values of the variable:
a = 20
b = 50
print("Before swapping the values, a:", a, "and b:", b)
a,b = b,a
print("After swapping the values, a:", a, "and b:", b)