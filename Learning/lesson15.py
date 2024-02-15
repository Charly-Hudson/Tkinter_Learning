# File Dialog box
#https://youtu.be/Aim_7fC-inw?feature=shared

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('crap baskets')
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')

# Returning file location for opening 
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="H:\Code\Testing_Grounds_PY\Tk_images", title="Select File", filetypes=(("png Files","*.png"),("Icons","*.ico"),("All File Types","*.*"),("JPG Files",".jpg")))
    my_label = Label(root, text=root.filename)
    my_label.pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()

open_button = Button(root, text="Open Image", command=open).pack()


root.mainloop()