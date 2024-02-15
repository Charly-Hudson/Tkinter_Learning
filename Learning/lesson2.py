# Grid learning
# https://youtu.be/BSfbjrqIw20?si=t25ZAnEIsy7x3etr

# Rows start form 0
# Col start form 0

from tkinter import *

root = Tk()

# Creating a Label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Guess what?")
myLabel3 = Label(root, text="Cha0s Rains Supreme!")

# Displaying it onto the screen
# This can be put at the end of the label like below, and it will display the same
# myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)

root.mainloop()