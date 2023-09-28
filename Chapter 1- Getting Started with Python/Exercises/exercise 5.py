#Exercise 5: Compute area of Circle 

#Python Program to fine the area of triangle
a=4
b=5
c=6
# a= float(input('Enter first side:: '))
# b= float(input('Enter second side:: '))
# c= float(input('Enter third side:: '))

#calculate the semi-perimeter
s=(a+b+c)/2

#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The are of the triangle is %0.2f'%area)