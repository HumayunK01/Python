#2
n = 1
while n <= 100:
    if n%2 == 0:
        print(n)
    n = n + 1

#5
n = int(input("Enter a number: "))
f = 1
while n > 0:
    f = f * n
    n = n - 1
print(f)
