#Write a program on Newton Rephson Method
import math
def func(x):
    return x**2+4*math.sin(x)

def func1(x):
    return 2*x+4*math.cos(x)

x0=float(input("Enter the approximation:"))
n=int(input("Enter the no of iteration:"))

i=1
while i < n+1:
    fx=func(x0)
    fdx=func1(x0)
    x1=x0-(fx/fdx)
    print("The root of the equation is",i, "is", x1)
    # x0=x1
    i=i+1