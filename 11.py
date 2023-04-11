# Write a Python function that takes a number as a parameter and check the number is prime or not:
def prim_find(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag == False:
        print("Its Not A Prime Number")
    elif flag == True:
        print("Its A Prime Number")
prim_find(14)

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument:
num = int(input("Enter a number: "))    

factorial = 1
if num < 0:
    print(" Factorial does not exist for negative numbers")    
elif num == 0:
    print("The factorial of 0 is 1")    
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of",num,"is",factorial)

# Write a Python function to return uppercase letters from the list:
L = ['A','B','c','d','E','F','g','h','I']

def upper(List):
    u = []
    for i in List:
        if i.isupper():
            u.append(i)
    return u

u_letters = upper(L)
print(u_letters)