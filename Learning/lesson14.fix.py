from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Notice me Senpai')
root.iconbitmap('Testing_Grounds_PY/Tk_images/ThorBitmapIcon.ico')

def new_window():
    global my_img
    global top
    top = Toplevel()
    top.title('Second Window')
    top.iconbitmap('Testing_Grounds_PY/Tk_images/ThorBitmapIcon.ico')
    my_img = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/background1.jpg"))
    my_label = Label(top, image=my_img).pack()

btn = Button(root, text="Open Second Window", command=new_window).pack()



mainloop()