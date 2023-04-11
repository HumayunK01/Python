# Write a Python program to create a set, add member(s) in a set and remove one item from set.
S1 = {10, 20, 30, 40, 50}
print("Original Set is:", S1)
S1.add(60)
print("After adding a single a element:", S1)
S1.update([70, 80, 90])
print("After adding multiple a elements:", S1)
S1.discard(90)
print("After discaring a element:", S1)
S1.remove(80)
print("After removing a element:", S1)
S1.pop()
print("After adding popping aelement:", S1, "\n")

# Write a Python program to perform following operations on set: intersection of sets, union of sets, set difference, symmetric difference, clear a set.
S2 = {10, 70, 80, 90}
S3 = S1.union(S2)
print("After Union:", S3)
S4 = S1.intersection(S2)
print("After intersection", S4)
S5 = S1.difference(S2)
print("After difference", S5)
S6 = S1.symmetric_difference(S2)
print("After symmetric difference", S6, "\n")
S6.clear()

# Write a Python program to find maximum and the minimum value in a set.
print("Maximum of S1 is:", max(S1))
print("Minimum of S1 is:", min(S1), "\n")

# Write a Python program to find the length of a set.
print("Length of S1 is:", len(S1))
    