import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, TextBox, Slider

def grid(this_text_needs_to_be_here):
    ax.grid(True)
    fig.canvas.draw()


def submit1(text):
    bananas = eval(text)
    l1.set_ydata(bananas)
    ax.set_ylim(np.min(bananas), np.max(bananas))
    plt.draw()


def submit2(text):
    bananas = eval(text)
    l2.set_ydata(bananas)
    ax.set_ylim(np.min(bananas), np.max(bananas))
    plt.draw()


def submit3(text):
    bananas = eval(text)
    l3.set_ydata(bananas)
    ax.set_ylim(np.min(bananas), np.max(bananas))
    plt.draw()


x_startValue = 100

initial_text = " input"

x1 = np.arange(-(float(x_startValue)), float(x_startValue), 1)
x2 = np.arange(-(float(x_startValue)), float(x_startValue), 1)
x3 = np.arange(-(float(x_startValue)), float(x_startValue), 1)

y1 = x1
y2 = x2 ** 2
y3 = x3 ** 3

fig, ax = plt.subplots()

l1 = ax.plot(x1, y1, lw=2, color='red')  ## (x axis increments, y axis increments , line width, line color)
l2 = ax.plot(x2, y2, lw=2, color='blue')
l3 = ax.plot(x3, y3, lw=2, color='purple')
fig.subplots_adjust(left=0.3, right=0.99)

horizontal = ax.plot()

Widget_colour = 'lightgoldenrodyellow'


ax_grid = plt.axes([0.05, 0.15, 0.08, 0.05])
grid_button = Button(ax_grid, 'Grid', color= Widget_colour, hovercolor='grey')

ax_box1 = plt.axes([0.1, 0.9, 0.08, 0.06])
ax_box2 = plt.axes([0.1, 0.9 - 0.07, 0.08, 0.06])
ax_box3 = plt.axes([0.1, 0.9 - 0.14, 0.08, 0.06])
text_box1 = TextBox(ax_box1, 'Evaluate', initial=initial_text)
text_box2 = TextBox(ax_box2, 'Evaluate', initial=initial_text)
text_box3 = TextBox(ax_box3, 'Evaluate', initial=initial_text)

text_box1.on_submit(submit1)
text_box2.on_submit(submit2)
text_box3.on_submit(submit3)
grid_button.on_clicked(grid)
plt.show()
