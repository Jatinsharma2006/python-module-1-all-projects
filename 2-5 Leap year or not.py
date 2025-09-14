"""year=(int(input("Enter Year")))
if(year%4==0):
    print(year,"is a Leap Year")
else:
    print("NOT A LEAP YEAR")"""
year=(int(input("Enter Year")))
if(year%100==0):
    if(year%400==0):
         print(year,"is Century a Leap Year")
    else:
        print(year,"NOT A Century LEAP YEAR")    
else:
    if(year%4==0):
        print(year,"is NORMAL a Leap Year")
    else:
        print(year,"NOT A LEAP YEAR")

       
    """ print(year,"is a Century")
    else:
        print(" Not a Century")""" 
