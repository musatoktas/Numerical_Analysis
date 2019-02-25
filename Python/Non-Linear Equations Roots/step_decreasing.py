x = float(input("Enter X value:"))
h = float(input("Enter H value:"))
a  = float(input("Enter a value:"))
eps = float(input("Enter Epsilon value:"))

def my_func(k):
  import math
  j = math.sin(k)
  l = 2*pow(k,3)
  m = l-j-5
  return m
 

while (h>eps):
    y = my_func(x)
    z = my_func(x+h)
    if (y*z>0):
        x = x + h
    else:
        h = h / a

    
print('root is: %f'%x)
