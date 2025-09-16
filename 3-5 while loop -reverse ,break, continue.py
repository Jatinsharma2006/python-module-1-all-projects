#while
i=4
while i<=40:
    print(i)
    i=i+4
#reverse while    
i=40
while i>=4:
    print(i)
    i=i-4
#break a while loop    
i=400
while i>=4:
    print(i)
    i=i-4
    if i<30:
        break
#continue a while loop
i=1
while i<=10:
    i=i+1
    if i%2==0:
        continue
    print(i)
