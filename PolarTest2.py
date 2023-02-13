import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, TextBox, Slider

ticks = np.arange(0, 10, 1)
theta = np.arange(0, 10, 0.01)
one = (np.sin(theta)**2)+(np.cos(theta)**2)
r = one



########################plotting##############################

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rmax(10)
ax.set_rticks(ticks)  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
fig.subplots_adjust(left=0.3, right=0.99)

ax_theta = plt.axes([0.1, 0.8, 0.08, 0.05])
ax_radius = [0.1, 0.7, 0.08, 0.05]

# theta_box
plt.show()
