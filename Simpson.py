def f(x):
    return(1/(1+x**2))
lo=float(input("Enter the lower limit of Integration:"))
up=float(input("Enter the upper limit of Integration:"))
n=int(input("Enter the number of strips:"))
h=float((up-lo)/n)   #Calculating step size
print("Step size(h):",h)
sum=0
for i in range(1,n):
    k=lo+i*h            #k is the variable used for the value of x in actual problem
    print(k)
    if i%2==0:              #i is the variable used for the value y in the actual problem(y1,y2)
        sum=sum+f(k)*2      #Sum calculation of even terms of y
    else:
        sum=sum+f(k)*4      #Sum calculation of odd terms of y

sum=float(h/3*(sum+f(lo)+f(up)))
print("Ans:",sum)

'''
Output:
Enter the lower limit of Integration:0
Enter the upper limit of Integration:6
Enter the number of strips:6
Step size(h): 1.0
Ans: 1.3661734132322367
'''