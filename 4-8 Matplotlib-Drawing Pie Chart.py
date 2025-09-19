#Drawing pie chart

import matplotlib.pyplot as plt

labels=['IT','Marketing','DataScience','Finance']

values=[500,156,300,510]

explode=(0.05,0.05,0.05,0.05)

plt.pie(values,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True)

plt.show()






















