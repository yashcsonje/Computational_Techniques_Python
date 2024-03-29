#Intermediate value theorem. Ex.2
import math
def function(x):
    return math.cos(x)-1.3*x

a=float(input("\n Enter 1st the number:" ))
b=float(input("\n Enter 2nd the number:" ))

fa=function(a)
fb=function(b)

print("The value of fa: ",fa)
print("The value of fb: ",fb)

if fa==0 or fb==0:
    print("\n It is the limit for the root for the give equation.")
    
else:
    if(fa*fb) < 0.0:
        print("\n Exist a root in the give interval in function ")
        
    else:
        print("\n doesn't exist a root in the given interval in function")

'''
Output:
 Enter 1st the number:-12

 Enter 2nd the number:12
The value of fa:  16.443853958732493
The value of fb:  -14.75614604126751

 Exist a root in the give interval in function
'''