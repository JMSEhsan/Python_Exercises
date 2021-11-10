# Ref. Get Programming Learn to code with Python by Ana Bell
# UI: Creating a Window

import tkinter
window = tkinter.Tk()
window.geometry("800x200")
window.title("My first GUI")
window.configure(background = "grey")

red = tkinter.Button(window, text = "Red", bg = "red")
red.pack()

yellow = tkinter.Button(window, text = "Yellow", bg = "yellow")
yellow.pack()

green = tkinter.Button(window, text = "Green", bg = "green")
green.pack()

textbox = tkinter.Entry(window)
textbox.pack()

colorlabel = tkinter.Label(window, height = "1", width = "1")
colorlabel.pack()

window.mainloop()