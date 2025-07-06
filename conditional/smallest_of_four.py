a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a < b:
    min1 = a
else:
    min1 = b
if c < d:
    min2 = c
else:
    min2 = d
if min1 < min2:
    print(min1, "is the smallest")
else:
    print(min2, "is the smallest")
