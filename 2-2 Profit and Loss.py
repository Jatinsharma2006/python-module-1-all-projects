cp=int(input("Enter Cost Price"))
sp=int(input("Enter Selling Price"))
(cp,sp)=eval(input("enter cp,sp"))
a=sp-cp

if(cp<sp):
    print ("You Made Profit",a)
if(cp>sp):
    print(f"You made loss{-1*a}")
else:
    print("no profit no loss")
                   


       
