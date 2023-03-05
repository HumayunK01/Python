# Write a program to check whether a number is even or odd:
no = int(input("Enter Any Number: "))
if (no%2 != 0):
    print("Entered number is odd \n")
else:
    print("Entered number is even \n")

# Write a program to find out the absolute value of an input number:
num = int(input("Enter a number to find it absolute value: "))
if num <= 0:
    num = num *- 1
    print("The absolute value is:", str(num), "\n")
else:
    print("The absolute value is:", str(num), "\n")

# Write the program to check the largest number among the three numbers:
num1 = int(input("Enter First No: "))
num2 = int(input("Enter Second No: "))
num3 = int(input("Enter Third No: "))
if(num1 > num2) and (num1 > num3):
    print("The largest no is First No:", num1, "\n")
elif(num2 > num1) and (num2 > num3):
    print("The largest no is Second No:", num2, "\n")
else:
    print("The largest no is Third No:", num3, "\n")

# Write a program to check if the input year is a leap year or not:
year = int(input("Enter Any Year: "))
if (year % 4 == 0):
    print("It is a leap year \n")
else:
    print("Its not a leap year \n")

# Write a program to check if a Number is Positive, Negative or Zero:
number = int(input("Enter a number: "))
if(number > 0):
    print("It is a Positive Number \n")
elif(number == 0):
    print("It is a Zero \n")
else:
    print("It is a Negative Number \n")

# Write a program that takes the marks of 5 subjects and displays the grade:
sub1 = int(input("Enter marks of the First Subject: "))
sub2 = int(input("Enter marks of the Second Subject: "))
sub3 = int(input("Enter marks of the Third Subject: "))
sub4 = int(input("Enter marks of the Fourth Subject: "))
sub5 = int(input("Enter marks of the Fifth Subject: "))
avg = (sub1 + sub2 + sub3 + sub4 + sub4) / 5
if(avg >= 90):
    print("Grade: A")
elif(avg >= 80) and (avg < 90):
    print("Grade: B")
elif(avg >= 70) and (avg < 80):
    print("Grade: C")
elif(avg >= 60) and (avg < 70):
    print("Grade: D")
else:
    print("Grade: F")