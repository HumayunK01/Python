# Question No 1:
class Emp:
    Name=""
    Dept=""
    Salary=0
    def read_e(self):
        self.Name = input("Enter Name: ")
        self.Dept = input("Enter Department: ")
        self.Salary = int(input("Enter Salary: "))
    def disp(self):
        print("Name:", self.Name)
        print("Department:", self.Dept)
        print("Salary:", self.Salary)

# Question No 2:
class student:
    def get_s(self, rn, name):
        self.RN = rn
        self.Name = name
    def disp_s(self):
        print("Roll No: ", self.RN)
        print("Name: ", self.Name)

class Result(student):
    def __init__(self, p1, p2):
          self.PTT1 = p1
          self.PTT2 = p2
    def disp_r(self):
        print("Marks for PTT1:", self.PTT1)
        print("Marks for PTT2:", self.PTT2)
R1 = Result(18,19)
R1.get_s(93,'Humayun')
R1.disp_s() 
R1.disp_r()

# Question No 3:
class Person:
    name = ""
    city = ""
    def get_person(self):
        self.Name = input("Enter Programmer Name: ")
        self.City = input("Enter City: ")
    def disp_person(self):
        print("Programmer Name: ", self.Name)
        print("Programmer City: ", self.City)

class Emp:
    sal = ""
    desig = ""
    def get_emp(self):
        self.Sal = int(input("Enter Salary: "))
        self.Desig = input("Enter Designation: ")
    def disp_emp(self):
        print("Salary: ", self.Sal)
        print("Designation: ", self.Desig)

class Programmer(Person, Emp): # Multiple Inheritance
    skill = ""
    def get_prog(self):
        self.Skill = input("Enter Your Skill:")
    def disp_prog(self):
        print("Skill: ", self.Skill)

P = Programmer()
P.get_person()
P.get_emp()
P.get_prog()

P.disp_person()
P.disp_emp()
P.disp_prog()