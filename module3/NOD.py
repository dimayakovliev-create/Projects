num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0:
    sum = num + (num - 1)
    num = num - 1
print(sum)


a = 3
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)


for i in range(0, 10, 2):
    print(i, end=" ")


val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")


my_list = [1, 2, 3]
a, *rest = my_list
print(a, rest)
