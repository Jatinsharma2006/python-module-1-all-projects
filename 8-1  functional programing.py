#print series from 1 to 10 in a list
"""
a=[]
for i in range(1,10+1):
    a.append(i)
print(a)    
"""
#create a sublist consist of only even numbers
a=[]
for i in range(1,11):
    a.append(i)
#old way
def even(x):
    return x%2==0

b=list(filter(even,a))
print(b)

#new way
c=list(filter(lambda x: x%2==0,a))
print(c)       
