"pip install matplotlib"
#%matplotlib inline - to genrate plot inside Jupyter Notebook


#Drawing Sine wave --using Matplotlib


import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,4*3.14,100)

y=np.sin(x)

plt.plot(x,y)

plt.show()
