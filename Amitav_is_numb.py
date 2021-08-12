import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1e-8,1000, num=50000)
y = np.sqrt(x)

fig, ax = plt.subplots()

ax.loglog(x,y)

fig.show()
input("Press enter to quit")