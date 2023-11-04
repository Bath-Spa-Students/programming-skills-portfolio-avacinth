# Computing the area of a circle 

# Integer variable
a = 4
b = 5
c = 6

# Calculate the semi-perimeter
s=(a+b+c)/2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c))**0.5

print('The area of the triangle is', area)
