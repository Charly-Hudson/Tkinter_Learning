# Frames
#https://youtu.be/_auZ8TTkojQ?feature=shared

# icon, image and exit buttons
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('crap baskets')
# need to path to folder \/
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')

#frame: think of DIVs in HTML/CSS
# You can use pack for the frame but then within the pack you can use grid and vice versa
frame = LabelFrame(root, text="this is my Frame....")
frame.pack(padx=20, pady=20)

b = Button(frame, text="Dont Click Here", command=root.quit)
b.grid(row=0, column=0)

b2 = Button(frame, text="Or Here", command=root.quit)
b2.grid(row=1, column=1)

root.mainloop()