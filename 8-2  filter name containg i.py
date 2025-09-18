#old way
#imperative approch

#name that have i in name
a=["rancho","faran","priya","millimeter"]
b=[]
for name in a:
   if 'i' in name:
       b.append(name)
print("following NAME contains i",b)   
   

#name that dont  have i in name
a=["rancho","faran","priya","millimeter"]
b=[]
for name in a:
   if 'i' not in name:
       b.append(name)
print("following NAME Not  contains i",b)

#new way
a=["rancho","faran","priya","millimeter"]
b=[]
c=list(filter(lambda name: "i" in name,a))
print('Name containing "i"',c)
   
