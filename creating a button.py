from tkinter import *
#main area
window = Tk()
def myClick():
    mylabel = Label(window, text="Fauxmos", bg="black", fg="white")
    mylabel.pack()
myButton = Button(window, text="Graph", padx=50, pady=25, command=myClick, bg="black", fg="white")

myButton.pack()
window.mainloop()

