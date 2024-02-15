# Multiple windows
#https://youtu.be/qC3FYdpJI5Y?feature=shared

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
top_label = Label(main, text="Those eyes").pack()

my_img2 = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/cha0scharly.png"))
my_label = Label(main, image=my_img2).pack()

# Window 2
def open():
    # If something dosent work within the function in a second window run it as a global
    # The global can reach what your looking for ? Not sure why this is a thing Tk go Burrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    global my_img
    top = Toplevel()
    top.title('Crap Baskets 2')
    top.iconbitmap('Testing_Grounds_PY/Tk_images/ThorBitmapIcon.ico')

    #Window2 Frame
    frame2 = LabelFrame(top)
    frame2.pack(anchor=W)
    exit_button = Button(frame2, text="Exit",command=root.quit)
    exit_button.grid(row=0, column=0)
    close_window = Button(frame2, text="Close Window", command=top.destroy)
    close_window.grid(row=0, column=1)

    # Window 2 Main Frame
    main_2 = LabelFrame(top)
    main_2.pack()
    top_label = Label(main_2, text="hows this")
    top_label.pack()

    my_img = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/ThorBitmapIcon.png"))
    my_label = Label(top, image=my_img)
    my_label.pack()
    
# Open second Window
button_thor = Button(main, text="Reveal The God of Hammers!", command=open)
button_thor.pack()


mainloop()

