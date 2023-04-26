# Question No 1:
import numpy as np
# Creating two matrices of size 2x2
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Addition of two matrices
addition = matrix1 + matrix2

# Subtraction of two matrices
subtraction = matrix1 - matrix2

# Multiplication of two matrices
multiplication = np.dot(matrix1, matrix2)

# Division of two matrices
division = np.divide(matrix1, matrix2)

# Printing the results
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Addition:\n", addition)
print("Subtraction:\n", subtraction)
print("Multiplication:\n", multiplication)
print("Division:\n", division)

# Question No 2:
# Input strings
string1 = "Hello, "
string2 = "world!"

# Concatenating two strings
result = string1 + string2

# Printing the result
print(result)

# Question No 3:
import random

# Generating six random integers between 10 and 30 (inclusive)
random_integers = [random.randint(10, 30) for _ in range(6)]

# Printing the random integers
print(random_integers)
