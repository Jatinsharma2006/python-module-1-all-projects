                             #for  loop 


# series 2,4,6,8,10
for i in range(2,10+1,2):
    print(i,end="\t")


#for reversed
for i in range(20,2-1,-2):
    print(i,end="\t")


#multiplication table
n=int(input("\nEnter a number"))    
for i in range(n,30-1,2):
    print(f"{n}*{i}={n*i}")
