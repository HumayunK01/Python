# Write a python program to print all the even numbers between 1 too 100 using while loop:
print("All the even numbers between 1 too 100 are:")
num = 1
max = 100
while num <= max:
    if(num % 2 == 0):
        print(num, end=' ',)
    num += 1

# Write a python program to find the sum of first 10 natural numbers using for loop:
print("\n")
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers is", sum, "\n")

# Write a python program to print Fibonacci series:
n_terms = 10
n_1 = 0  
n_2 = 1  
count = 0  
print ("The fibonacci series of", n_terms ," numbers is:")  
while count < n_terms:  
    print(n_1, end=' ')  
    nth = n_1 + n_2  
    n_1 = n_2  
    n_2 = nth  
    count += 1

# Write a python program to calculate factorial of a number:
print("\n")
num = 6
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of", num, "is", factorial)

# Write a python program to reverse the given number:
num = 12345
print("\nNumbers are", num)
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Numbers are", reversed_num, "\n")

# Write a python program that takes in a number and finds the sum of digits in the number:
num = 12345
sum = 0
while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10
print("The sum of digits is", sum, "\n")

# Write a python program that takes a number and checks whether it is palindrome or not:
num = int(input("Enter a number: "))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(temp == rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")