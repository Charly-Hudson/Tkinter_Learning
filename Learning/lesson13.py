# Message Boxes
#https://youtu.be/S3AaSwpb5GE?feature=shared

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('crap baskets')
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')

# exit button frame
frame1 = LabelFrame(root)
frame1.pack(anchor=W)
exit_button = Button(frame1, text="Exit",command=root.quit)
exit_button.pack(anchor=W)
# main window frame
main = LabelFrame(root).pack()

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# Different types of popups, they have different sounds and icons

def popup():
    responce = messagebox.askquestion("This is my popup", "Yoyo World")
    #Label(main, text=responce).pack()
    if responce == "yes":
        Label(main, text="You Clicked Yes").pack()
    else:
        Label(main, text="You Clicked No").pack()

Button(main, text="Popup", command=popup).pack()

mainloop()