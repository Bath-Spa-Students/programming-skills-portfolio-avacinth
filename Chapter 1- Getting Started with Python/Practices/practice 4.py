# Compute the area of a triangle 

# Three sides of the triangle is a, b and c:  
a = float(input(10))  
b = float(input(12))  
c = float(input(9))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   