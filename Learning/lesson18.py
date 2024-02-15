# Dropdown Boxes
#https://youtu.be/3E_fK5hCUnI?feature=shared

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('crap baskets')
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')
root.geometry("400x400")

# exit button frame
topbar = LabelFrame(root)
topbar.pack(anchor=W)
exit_button = Button(topbar, text="Exit",command=root.quit)
exit_button.grid(row=0, column=1)


# main window frame
main = LabelFrame(root, borderwidth=5).pack()
top_label = Label(main, text="Spicy Tomatos").pack(anchor=W)

# Dropdown

def show():
    labbl = Label(main, text=clicked.get()).pack()

# Adding a list to take it out of option menu I.E.
# drop = OptionMenu(main, clicked, "monday", "tuesday", "etc.")
options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]
clicked = StringVar()
clicked.set(options[0])

# Options for the dropdown are after (main, clicked, "options")
# see abouve for alternate methonds
drop = OptionMenu(main, clicked, *options)
drop.pack()

btn = Button(main, text="Show Selection", command=show).pack()

root.mainloop()