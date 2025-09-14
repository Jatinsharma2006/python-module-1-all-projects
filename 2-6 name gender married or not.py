n=str(input("enter Name"))
g=str(input("enter Gender"))
m=str(input("enter Married(yes or no)"))
if(g=='male','Male','MALE'):
    
   if m=="yes":
       print(f"hello Mr.{n}")   
   else(m=="no"):
       print(f"hello {n}")
       
elif (g=='female','Female','FEMALE'):
    
    if m=="yes":
       print(f"hello Mrs.{n}")  
    else(m=="no"):
       print(f"hello Ms.{n}")
else:
    ("please enter valid gender")
       


#Enhancement in name,gender,married example
(name,gender,married)=input(
    "Enter Name,Gender[M/F],Married[Y/N]").split(",")
#decision making

if gender in ("m","M",'male','Male'):
    if married in ('Y','y','yes','Yes','YES'):
        print(f"Hello Mr.{name}")
    else:
        print(f"Hello Master. {name}")
        
elif gender  in ("f","F",'female','Female'):
    if married in ('Y','y','yes','Yes','YES'):
        print(f"namaskar Mrs.{name}")
    else:
        print(f"namaste Ms. {name}")
 
else:
    print("please enter vaid gender")
