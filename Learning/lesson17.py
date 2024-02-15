# check boxes
#https://youtu.be/4IsLwwb_yDs?feature=shared

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('crap baskets')
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')
root.geometry("400x400")

# exit button frame
frame1 = LabelFrame(root)
frame1.pack(anchor=W)
exit_button = Button(frame1, text="Exit",command=root.quit)
exit_button.pack(anchor=W)

# main window frame
main = LabelFrame(root, borderwidth=5).pack()
top_label = Label(main, text="Check Boxes").pack(anchor=W)

# Can be changed for different variable types IntVar() etc.
var = StringVar()

def show():
    my_label = Label(main, text=var.get()).pack()

check = Checkbutton(main, text="Exit Program", variable=var, onvalue="On", offvalue="Off")
# This is needed otherwise it will alto select
check.deselect()
check.pack()

btn = Button(main, text="show", command=show).pack()

my_label = Label(main, text=var.get()).pack()



root.mainloop()