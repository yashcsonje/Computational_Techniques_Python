print("Program for jacobi's Method")
def f1(x,y,z): #equation for x
    return 1/20*(17-y0+2*z0)
def f2(x,y,z): #equation for y
    return 1/20*(-18-3*x0+z0)
def f3(x,y,z): #equation for z
    return 1/20*(25-2*x0+3*y0)
n=int(input("Enter the number of iterations:"))
x0=0
y0=0
z0=0
for i in range(0,n):
    x1=f1(x0,y0,z0)
    y1=f2(x0,y0,z0)
    z1=f3(x0,y0,z0)
    print("Iteration no:",i+1)
    print(x1,"\t\t",y1,"\t\t",z1)
    x0=x1
    y0=y1
    z0=z1
print("End") 