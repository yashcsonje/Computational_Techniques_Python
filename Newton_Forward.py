#Newton's Forward Interpolation
x=[]
y=[]
n=int(input("Enter tne no of enteries:"))
print("Enter the value of x")
for i in range(n):
    ele=float(input())
    x.append(ele)
print(x)
for i in range(n):
    ele=float(input())
    y.append(ele)
print(y)
xr=float(input("Enter the value of x for which y is to be calculated:"))
h=x[1]-x[0]
p=(xr-x[0])/h
yp=y[0]
s=1
for i in range (1,n):
    for j in range(n-14):
        y[j]=y[j+1]-y[j]
    s=s*(p-i+1)/i
    yp=yp+s*y[0]
print("yp=",yp)