import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4*314,200)
y=np.sin(x)
plt.plot(x,y)
plt.show()


x=np.arange(0,50,0.1)
y=np.sin(x)
z=np.cos(x)
w=np.tan(x)
plt.plot(x,y,color="r")
#plt.plot(x,z,color="y")
#plt.plot(x,w,color="g")
plt.show()
