# Check if a triangle is valid based on its sides

a = int(input("Enter side A of the triangle: "))
b = int(input("Enter side B of the triangle: "))
c = int(input("Enter side C of the triangle: "))

if a + b > c and b + c > a and c + a > b:
    print("Valid triangle")
else:
    print("Invalid triangle")
