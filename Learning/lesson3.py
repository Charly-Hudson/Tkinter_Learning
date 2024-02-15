# Buttons
# https://youtu.be/yuuDJ3-EdNQ?si=bNfKSR3dO_qVB7x3

# Rows start from 0
# Col start from 0

from tkinter import *

root = Tk()

# Creating a Label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Guess what?")

# Function Click
def myClick ():
    myLabel3 = Label(root, text="Cha0s Rains Supreme!")
    myLabel3.grid(row=3, column=3)

# Display 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# in Button() you can add a state like state=DISABLED to disable the button e.g. \/
# myButton = Button(root, text="What?", state=DISABLED)
# Padding, think CSS padx=50 (pixels) pady=50 (pixels) 
# wont work unless you add command=
#change text colour = fg="color" 
# Change Background colour = bg="colour" 
# Hex colour codes can be used, Satisfactory colours have been used here
myButton = Button(root, text="What?", padx=50, command=myClick, fg="#e49245", bg="#4c5b5f")
myButton.grid(row=2, column=2)

root.mainloop()