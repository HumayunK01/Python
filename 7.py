# Create a tuple and find the minimum and maximum number from it.
T1 = (1, 3, 5, 7, 9, 11, 7, 5)
print("Tuple is:", T1)
print("Minimum:", min(T1))
print("Maximum:", max(T1))
print("\n")

# Write a Python program to find the repeated items of a tuple.
repeated = []
for i in T1:
    if T1.count(i) > 1 and i not in repeated:
        print("Repeated:", i)
        repeated.append(i)
print("\n")

# Print the number in words for Example: 1234 => One Two Three Four
Words = []
for i in T1:
    if (i == 0):
        print("Zero", end=', ')
    elif (i == 1):
        print("One", end=', ')
    elif (i == 2):
        print("Two", end=', ')
    elif (i == 3):
        print("Three", end=', ')
    elif (i == 4):
        print("Four", end=', ')
    elif (i == 5):
        print("Five", end=', ')
    elif (i == 6):
        print("Six", end=', ')
    elif (i == 7):
        print("Seven", end=', ')
    elif (i == 8):
        print("Eight", end=', ')
    elif (i == 9):
        print("Nine", end=', ')
