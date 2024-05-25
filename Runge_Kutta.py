def f(x,y):
    return(x+y)
xo=float(input("enter the value of xo:"))
yo=float(input("enter the value of y0:")) #print
xr=float(input("enter the value of x at which y is to be found out:"))
h=float(input("enter the value of stepsize:"))
while(xo<xr):
    k1=h*f(xo,yo)
    k2=h*f(xo+h/2,yo+k1/2)
    k3=h*f(xo+h/2,yo+k2/2)
    k4=h*f(xo+h,yo+k3)
    k=1/6*(k1+2*k2+2*k3+k4)
    print("k=",k)
    y1=yo+k
    x1=xo+h
    print("y1=",y1)
    print("x1=",x1)
    xo=x1
    yo=y1
print("end")