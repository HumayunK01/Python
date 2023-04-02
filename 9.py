# Write a Python script to sort (ascending and descending) a dictionary by value.
d1 = {1: "Computer", 3: "Robotics", 2: "Mechanical"}
def dic_value(e):
    return e[1]

print("Sorting according to value - Descending Order")
S01 = dict(sorted(d1.items(), reverse=True, key=dic_value))
print(S01)
print("Sorting according to value - Ascending Order")
S01 = dict(sorted(d1.items(), reverse=False, key=dic_value))
print(S01, "\n")

# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary:
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict = {}
dict.update(dict1)
dict.update(dict2)
dict.update(dict3)
print(dict, "\n")

# Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'c': 100}
d = {}
for k in d1.keys():
    if k in d2.keys():
        d2[k] = d1[k] + d2[k]
    else:
        d2[k] = d1[k]
print(d2, "\n")

# Write a Python program to print all unique values in a dictionary.
sampleData = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
    "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print("Original List: ", sampleData)
u_value = set(val for dic in sampleData for val in dic.values())
print("Unique Values: ", u_value, "\n")

# Write a Python program to find the highest 3 values in a dictionary.
S = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f':50}
l = list(S.values())
print(l)
l.sort(reverse = True)
for i in range(0, 3):
    print(l[i])