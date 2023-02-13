import numpy as np
import matplotlib.pyplot as plt


ticks = np.arange(0, 10, 1)
theta = np.arange(0, 10, 0.01)
one = (np.sin(theta)**2)+(np.cos(theta)**2)
r = one


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rmax(10)
ax.set_rticks(ticks)  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)





plt.show()
