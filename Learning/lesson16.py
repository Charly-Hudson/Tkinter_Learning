# Sliders
#https://youtu.be/knUHd8ZGyiM?feature=shared

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
main = LabelFrame(root).pack()
top_label = Label(main, text="Sliders").pack()

# Pack/Grid seperately 
vertical = Scale(main, from_=400, to=800)
vertical.pack()

horizontal = Scale(main, from_=300, to=600, orient=HORIZONTAL)
horizontal.pack()

def AAAAA():
    root.geometry(str(horizontal.get()) +"x"+ str(vertical.get()))
    horizontal_label = Label(main, text=horizontal.get()).pack()
    vertical_label = Label(main, text=vertical.get()).pack()

my_btn = Button(main, text="Click Me!", command=AAAAA).pack()

root.mainloop()