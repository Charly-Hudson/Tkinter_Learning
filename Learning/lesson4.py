# Input Boxes
# https://youtu.be/7A_csP9drJw?si=5xYLJFURtvUGYvID

# Rows start from 0
# Col start from 0

from tkinter import *

root = Tk()

# Creating a Label widget first part
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Guess what?")
myLabel6 = Label(root, text="Add your name:")

# Function Click 1
def myClick1 ():
    myLabel3 = Label(root, text="Cha0s Rains Supreme!")
    myLabel3.grid(row=3, column=0)

# Display 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel6.grid(row=0, column=1)

# in Button() you can add a state like state=DISABLED to disable the button e.g. \/
# myButton = Button(root, text="What?", state=DISABLED)
# Padding, think CSS padx=50 (pixels) pady=50 (pixels) 
# wont work unless you add command=
#change text colour = fg="color" 
# Change Background colour = bg="colour" 
# Hex colour codes can be used, Satisfactory colours have been used here
myButton = Button(root, text="What?", padx=50, command=myClick1, fg="#e49245", bg="#4c5b5f")
myButton.grid(row=2, column=0)

# Entry widget
# Changing peramitors of the box:
# Width and colour (width=50, bg="#4c5b5f", fg="#e49245")
# Height dosent work?
# Borders can be added with (borderwidth=5)
e = Entry(root, width=20, bg="#4c5b5f", fg="#e49245", borderwidth=5)
e.grid(row=1, column=1)
#Get function for getting what you entered
e.get()

# Function click 2
def myClick2():
    myLabel5 = Label(root, text=e.get())
    myLabel5.grid(row=3, column=1)

myButton = Button(root, text="Go!", command=myClick2)
myButton.grid(row=2, column=1)

root.mainloop()