# Method Overloading
def sum(a = None, b = None, c = None):
    if a == None and b == None and c == None:
        return 0
    elif b == None and c == None:
        return a
    elif c == None:
        return a + b
    else:
        return a + b + c
print(sum())
print(sum(10))
print(sum(10,20))
print(sum(10,20,30))


# Method Overriding:
class student:
    def get_s(self, rn, name):
        self.RN = rn
        self.Name = name
    def disp(self):
        print(self.RN)
        print(self.Name)

class Result(student):
    def __init__(self, p1, p2):
          self.PTT1 = p1
          self.PTT2 = p2
    def disp(self):
        print(self.PTT1)
        print(self.PTT2)
R1 = Result(18,19)
R1.get_s(93,'Humayun')
R1.disp() #Child class disp() will override parent class disp()
R1.disp()