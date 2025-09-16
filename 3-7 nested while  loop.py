#nested loop using while loop
i=1
while i<=5:
    print("i=",i,end=":")
    j=1
    while j<=5:
        #print(j,end=" ")
        #print(chr(64+j),end="_")
        print(i*j,end=" ")
        #print(chr(j),end=" ")
        j=j+1
    i=i+1
    print(end="\n")
