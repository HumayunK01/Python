import math
import random

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
string = "pyTHon progRAMMing"

def c_l_u(s):
    c_lower = 0
    c_upper = 0

    for c in string:
        if c.islower():
            c_lower = c_lower+1
        elif c.isupper():
            c_upper = c_upper+1
    print("Lower Case count is", c_lower)
    print("Lower Case count is", c_upper)

c_l_u(string)

# Write a Python program to generate a random float where the value is between 5 and 50 using Python math module.
random_float = random.uniform(5, 50)
rounded_float = round(random_float, 2)
print("Random float between 5 and 50:", rounded_float)
