#sum of two digt
#old way :impertitive code
a=[100,20,50]
x=0
for i in a:
    x=x+i
print("Total is", x)


#new way:functional  programing
from functools import reduce
y=reduce(lambda x,y: x+y,a)
print("Total is", x)



#multiplication of two digt
#old way :impertitive code
a=[100,20,50]
x=1
for i in a:
    x=x*i
print("multiplcation  is", x)


#new way:functional  programing
from functools import reduce
y=reduce(lambda x,y: x*y,a)
print("multiplcation is", x)
