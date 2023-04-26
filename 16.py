# 1. Write a Python program to Check for ZeroDivisionError Exception.
numerator = 10
denominator = 0

try:
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero! \n")

# 2. Write a Python program to create user defined exception that will check whether the password is correct or not?
class PasswordIncorrectError(Exception):
    pass

def check_password(password):
    correct_password = "my_password123"
    if password != correct_password:
        raise PasswordIncorrectError("Password is incorrect")
    else:
        print("Password is correct")

# Testing the check_password function
password = input("Enter your password: ")
try:
    check_password(password)
except PasswordIncorrectError as error:
    print(error)
