import numpy as np
p1=np.poly1d([2,4,6])
p2=np.poly1d([1,3,5])
p3=p1+p2
print("POLYNOMIAL ADDITION:\n",p3)
p3=np.polyadd(p1,p2)
print("POLYNOMIAL ADDITION:\n",p3)


p4=p1*p2
print("POLYNOMIAL ADDITION:\n",p4)
p4=np.polymul(p1,p2)
print("POLYNOMIAL MULTIPLICATION:\n",p4)
