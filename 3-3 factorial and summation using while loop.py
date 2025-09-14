#factorial of any number using while loop
"""
n=int(input("enter a number"))
f=1
i=1
while i<=n:
    f=f*i
    i=i+1
#when this loop end   
print(f"factorial of {n}=\n{f}")
"""     

"""
#factorial of any number but it will show every steps
n=int(input("enter a number"))
f=1
i=1
while i<=n:
    f=f*i
    i=i+1
#will print everytime a  loop has run   
    print(f"factorial of {n}=\n{f}")      
"""

#factorial using reverse loop
n=int(input("enter a number"))
f=1
i=n
while i>=1:
    f=f*i
    i=i-1
    #when this loop end   
print("factorial=",f,step=' ')
print("factorial=",f)



#summation of numbers


n=int(input("enter a number"))
s=0
i=1
while i<=n:
    s=s+i
    i=i+1
#when this loop end   
    print(f"summation of {n}=\n{s}")


