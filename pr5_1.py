# print("1. What would be the output from the following Python code segment?")
# x = 10
# while x > 5:
#     print(x)
#     x = 1

# print("\n2. Change the following Python code from using a while loop to for loop:")
# for i in range(1, 10):
#     print(i)

# n = 1
# while n <= 100:
#     if n%2 == 0:
#         print(n)
#     n = n + 1

# #5
# n = int(input("Enter a number: "))
# f = 1
# while n > 0:
#     f = f * n
#     n = n - 1
# print(f)

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print('*', end='')
    print("\r")