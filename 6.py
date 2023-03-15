# Declaring Lists:
L1 = [1, 4, 6, 3, 6, 8, 2]
L2 = ['Apple', 'Mango', 'Kiwi', 'Orange']
L3 = ['Supra', 'Skyline', 'Mushtang', 'Mazda', 'Bugatti']

# Write a Python program to sum all the items in a list.
sm = 0
for i in L1:
    sm = sm + i
print("Sum all the items in a list is", sm)

# Write a Python program to multiplies all the items in a list.
ml = 1
for i in L1:
    ml = ml * i
print("Multiplication all the items in a list is", ml)

# Write a Python program to get the largest number from a list.
print("Largest number from a list is", max(L1))

# Write a Python program to get the smallest number from a list.
print("Smallest number from a list is", min(L1))

# Write a Python program to reverse a list.
print("Original List is:", L2)
L2.reverse()
print("Reversed List is:", L2)

# Write a Python program to find the length of each elements in the list:
Length_L3 = []
for i in L3:
    Length_L3.append(len(i))
print("Length of each element in", L3, "is", Length_L3)
