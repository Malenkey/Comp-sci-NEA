###################################################################################
#     ######      #        #    #   #      #  ##     ##       #####      ######   #
#     #          # #       #    #    #   #    #  # #  #      #     #     #        #
#     ###       ####       #    #      #      #   #   #      #     #     ######   #
#     #        #    #      #    #    #   #    #       #      #     #         #    #
#     #       #      #     ######  #       #  #       #       ####      ######    #
###################################################################################


################################importing libraries##########################


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, TextBox, Slider


##############################defining functions and routines##############################

def grid(this_text_needs_to_be_here):
    ax.grid()
    fig.canvas.draw()


def colorfunc(label):
    l.set_color(label)
    plt.draw()


def stylefunc(label):
    l.set_linestyle(label)
    plt.draw()


def submit(text):
    ydata = eval(text)
    l.set_ydata(ydata)
    ax.set_ylim(np.min(ydata), np.max(ydata))
    plt.draw()


#######################################defining variables###########################################################

x_startValue = 100

initial_text = "Enter input"

x = np.arange(-(float(x_startValue)), float(x_startValue), 0.01)
y = x

fig, ax = plt.subplots()
l, = ax.plot(x, y, lw=2, color='red')  ## (x axis increments, y axis increments , line width, line color)
fig.subplots_adjust(left=0.3, right=0.99)

horizontal = ax.plot()

Widget_colour = 'lightgoldenrodyellow'

####################################################creating interactive widgets###################################

ax_grid = plt.axes([0.05, 0.15, 0.08, 0.05])
grid_button = Button(ax_grid, 'Grid', color=Widget_colour, hovercolor='grey')

ax_color = fig.add_axes([0.02, 0.7, 0.08, 0.25], facecolor=Widget_colour)
color_button = RadioButtons(ax_color, ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'))

ax_line_option = fig.add_axes([0.1, 0.8, 0.07, 0.15], facecolor=Widget_colour)
line_option = RadioButtons(ax_line_option, ('-', '--', '-.', ':'))

ax_box = plt.axes([0.1, 0.001, 0.6, 0.06])
text_box = TextBox(ax_box, 'Evaluate', initial=initial_text)

################################## when interacted with ###################################################

text_box.on_submit(submit)

grid_button.on_clicked(grid)

color_button.on_clicked(colorfunc)

line_option.on_clicked(stylefunc)

plt.show()
