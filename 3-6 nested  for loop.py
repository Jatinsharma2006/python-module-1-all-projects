
for i in range(1,5+1):
    print('i=',i,end="=>")
    for j in range(1,5+1):
        print(j,end=" ")
    print(end="\n")


#second
"""

n=int(input("enter number of lines"))
for i in range(1,n+1):
    print('i=',i,end="=>")
    for j in range(1,n+1):
        print(j,end=" ")
    print(end="\n")
"""
"""


#third
n=int(input("enter number of line"))
for i in range(1,n+1):
    print('i=',i,end="=>")
    for j in range(1,n+1):
        if j==1 or j==n or i==1 or i==n//2:
            print("#",end="")
        else:
            print(" ",end="")
    print(end="\n")
"""
