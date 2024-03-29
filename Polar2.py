import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, TextBox, Slider


##########################Functions############################
def theta_limits(max):
    global theta
    theta = np.linspace(0, max, 360)



def radius_limit(text):
    global polar_l, radius
    print('hello', theta)
    ax.cla()
    radius = eval(text) * ((np.sin(theta) ** 2) + (np.cos(theta) ** 2))
    polar_l = ax.plot(theta, radius, color='red')
    fig.canvas.draw_idle()


def theta_max(val):
    global theta

    theta_limits(max_slider.val)
    polar_l.set_xdata(theta)

    fig.canvas.draw_idle()





######################defining variables##################

ticks = np.arange(0, 10, 1)
min = 0
max = 2*np.pi
theta_limits(max)
one = (np.sin(theta) ** 2) + (np.cos(theta) ** 2)

########################plotting##############################

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
polar_l, = ax.plot(theta, one, lw=1, color='red')
ax.set_rmax(5)
ax.set_rticks(ticks)  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
fig.subplots_adjust(left=0.3, right=0.99)

#####################plotting boxes###################
ax_thetaMax = fig.add_axes([0.25, 0.91, 0.65, 0.03])
ax_radius = plt.axes([0.094 + 0.15, 0.7, 0.08, 0.05])

max_slider = Slider(ax=ax_thetaMax, label='θ max', valmin=0, valmax=(2*np.pi), valinit=max)
radius_box = TextBox(ax_radius, 'Radius', initial='1')

#######################when interacted with####################

# theta_box1.on_submit(theta_limits( ,text))
# theta_box2.on_submit()
max_slider.on_changed(theta_max)
radius_box.on_submit(radius_limit)

plt.show()
