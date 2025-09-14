                          #fibonacci series trigonacci
                 # in c style
n=int(input("enter no of terms"))
a=0
b=1
c=1
i=1            #iitaial
while i<=n:    #condition
    print(a)
    d=a+b+c
    a=b
    b=c
    c=d
    i=i+1      #counter




              #hexanacci
n=int(input("enter no. of terms"))
a=0
b=1
c=1
d=2
e=4
f=8
i=1            #intaial
while i<=n:    #condition
    print(a,end="\t")
    g=a+b+c+d+e+f
    a=b
    b=c
    c=d
    d=e
    e=f
    f=g
    i=i+1      #counter

    
# fabibonacci series   in python style
n=int(input("Enter a number of terms"))
(a,b,c,i)=(0,1,1,1)#concepts of tuple

for i in range(1,n+1):      #start, end+1
    print(a,end="\t")
    d=a+b+c
    a=b
    b=c
    c=d









