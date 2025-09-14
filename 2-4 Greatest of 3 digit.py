"""(a,b,c)=eval(input("enter a,b,c"))

if a>b and a>c:
    print(a,'is greater')
elif b>c:
    print(b,'is greater')
else:
    print(c,"is greater")
#nested if else greastest of 3 no.
"""
(a,b,c)=eval(input('enter a,b,c'))
if a>c:
    if a>c:
        print(f"{a}is greatest")
    else:
        print("{}is Greatest")
else:
    if b>c:
        print(b,"is Greatest")
    else:
        print("%d is greatest"%c)
        
             


    
