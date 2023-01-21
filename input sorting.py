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

def inputText(textThing):
    secondInput == textThing


def submit(text):
    ydata = eval(text)
    l.set_ydata(ydata)
    ax.set_ylim(np.min(ydata), np.max(ydata))
    plt.draw()

def update(val):
    global x
    x = np.arange(-(float(val)), float(val), 0.01)
    plt.show()




#######################################defining variables#################################################################

x_startValue = 100

initial_text = " input"

x = np.arange(-(float(x_startValue)), float(x_startValue), 0.01)
y = x

fig, ax = plt.subplots()
l, = ax.plot(x, y, lw=2, color='red') ## (x axis increments, y axis increments , line width, line color)
fig.subplots_adjust(left=0.3, right=0.99)

horizontal = ax.plot()

Widget_colour = 'lightgoldenrodyellow'

####################################################creating interactive widgets############################################

ax_grid = plt.axes([0.05, 0.15, 0.08, 0.05])
grid_button = Button(ax_grid, 'Grid', color= Widget_colour, hovercolor='grey')


ax_color = fig.add_axes([0.05, 0.6, 0.15, 0.15], facecolor=Widget_colour)
color_button = RadioButtons(ax_color, ('red', 'blue', 'green', 'purple'))


ax_line_option = fig.add_axes([0.05, 0.2, 0.15, 0.15], facecolor=Widget_colour)
line_option = RadioButtons(ax_line_option, ('-', '--', '-.', ':'))


ax_box = plt.axes([0.1, 0.9, 0.08, 0.06])
text_box = TextBox(ax_box, 'Evaluate', initial=initial_text)






################################## when interacted with ###################################################

text_box.on_submit(submit)

grid_button.on_clicked(grid)

color_button.on_clicked(colorfunc)

line_option.on_clicked(stylefunc)









plt.show()
