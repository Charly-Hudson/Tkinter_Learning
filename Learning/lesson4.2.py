# Buttons
# https://youtu.be/yuuDJ3-EdNQ?si=bNfKSR3dO_qVB7x3

# Rows start from 0
# Col start from 0

from tkinter import *

root = Tk()

# Creating a Label widget
myLabel1 = Label(root, text="Hello")
myLabel2 = Label(root, text="Guess what?")

# Function Click
def myClick ():
    cha0s = "Cha0s Rains Supreme! " + e.get()
    myLabel3 = Label(root, text=cha0s)
    myLabel3.grid(row=4, column=0)

# Display 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=2, column=0)

# Entry widget
# Changing peramitors of the box:
# Width and colour (width=50, bg="#4c5b5f", fg="#e49245")
# Height dosent work?
# Borders can be added with (borderwidth=5)
e = Entry(root, width=30, bg="#4c5b5f", fg="#e49245", borderwidth=5)
e.grid(row=1, column=0)
#Get function for getting what you entered
e.get()
# Default Text
e.insert(0, "Replace this with Your Name:")

# in Button() you can add a state like state=DISABLED to disable the button e.g. \/
# myButton = Button(root, text="What?", state=DISABLED)
# Padding, think CSS padx=50 (pixels) pady=50 (pixels) 
# wont work unless you add command=
#change text colour = fg="color" 
# Change Background colour = bg="colour" 
# Hex colour codes can be used, Satisfactory colours have been used here
myButton = Button(root, text="What?", padx=50, command=myClick, fg="#e49245", bg="#4c5b5f")
myButton.grid(row=3, column=0)

root.mainloop()