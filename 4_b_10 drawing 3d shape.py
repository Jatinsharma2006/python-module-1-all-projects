#Drawing 3D Chart
 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)

X,Y=np.meshgrid(x,y)

Z=np.sin(np.sqrt(X**2+Y**2))

fig=plt.figure()

ax=fig.add_subplot(111,projection='3d')

ax.contour3D(X,Y,Z,50,cmap="plasma")
ax.contour3D(X,Y,Z,zdir="z",offset=np.min(Z),cmap="plasma")

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.set_title('3D Contour Plot with Contour lines')
plt.show()


