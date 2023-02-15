import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, TextBox, Slider

##########################Functions############################
def theta_limits():
    global theta
    theta = np.arange(min, max, 0.1)

def radius_limit(text):
    global l
    ax.cla()
    print(eval(text, {"theta": theta, "np": np}))
    #print(int(eval(text, {"theta": theta, "np": np}))*((np.sin(theta)**2)+(np.cos(theta)**2)))
    l, = ax.plot(theta, eval(text)*((np.sin(theta)**2)+(np.cos(theta)**2)), color='red')











######################defining variables

ticks = np.arange(0, 10, 1)
min = 0
max = 2*np.pi
theta_limits()
one = (np.sin(theta)**2)+(np.cos(theta)**2)




########################plotting##############################

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
l, = ax.plot(theta, one)
ax.set_rmax(5)
ax.set_rticks(ticks)  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
fig.subplots_adjust(left=0.3, right=0.99)




#####################plotting boxes###################
ax_theta1 = plt.axes([0.2+0.15, 0.8, 0.08, 0.05])
ax_theta2 = plt.axes([0.094+0.15, 0.8, 0.08, 0.05])
ax_radius = plt.axes([0.094+0.15, 0.7, 0.08, 0.05])

theta_box1 = TextBox(ax_theta1, '<Θ<', initial='2pi')
theta_box2 = TextBox(ax_theta2, '', initial='0')
radius_box = TextBox(ax_radius, 'Radius', initial='1')

#######################when interacted with####################

# theta_box1.on_submit(theta_limits( ,text))
# theta_box2.on_submit()
radius_box.on_submit(radius_limit)

plt.show()
