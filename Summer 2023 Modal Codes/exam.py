# ----------------------------------------------------------------
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# ----------------------------------------------------------------
class employee:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_emp(self):
        print("ID:", self.id)
        print("Name:", self.name)

e = employee(2005690093, "Humayun")
e.show_emp()

# ----------------------------------------------------------------
import calculation as cal

print(cal.add(5, 3))
print(cal.sub(5, 3))

# ----------------------------------------------------------------
dict1 = {1: "Vijay", 2: "Santosh", 3: "Yogita"}
print(dict1)

dict1[2] = "Shreyas"
print(dict1)

dict1.pop(1)
print(dict1)

# ----------------------------------------------------------------
