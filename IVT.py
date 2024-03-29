#Intermediate value theorem
'''
If a function f(x) is continuous in th interval a,b and f(a) & f(b) are of opposite
signs then equation f(x)=0 has atleast one root between x=a & x=b.
'''

def function(x): 
    return 2*x**5 + 3*x**3 + 7*x - 13 
 
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
        print("\n Exist a root in the give interval in function") 
         
    else: 
        print("\n Doesn't exist a root in the given interval in function")
        
'''
Output:
Enter 1st the number:-12

 Enter 2nd the number:12
The value of fa:  -502945.0
The value of fb:  502919.0

 Exist a root in the give interval in function
'''
