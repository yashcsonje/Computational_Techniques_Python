print("Legranges interpolation")
x=[]
y=[]
n=int(input("Enter the number of data points="))
print("Enter value of x")
for i in range(0,n):
    ele=float(input())
    x.append(ele)
print(x)
print('enter values of y')
for i in range (0,n):
    ele=float(input())
    y.append(ele)
print(y) 
xr=float(input("Enter the value of x for for which y is to be found out xr="))
# fy=0
for j in range (0,n):
    num=1
    den=1
    for i in range (0,n):
        if (i!=j):
            num=num*(xr-x[i])
            den=den*(x[j]-x[i])
print(num)
print(den)
fy=float(num/den)*y[j]
print("The value of fy at xr=",xr,"is yr=",fy)