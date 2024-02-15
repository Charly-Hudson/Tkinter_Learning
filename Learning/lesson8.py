# image
# link = https://youtu.be/NoTM8JciWaQ?si=m9ewOZg3Ua_dG3zT

# icon, image and exit buttons
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('crap baskets')
# Needs to be an .ico file, use krita for its ez gg 
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')

#adding an image
my_img = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/cha0scharly.png"))
my_label = Label(image=my_img)
my_label.pack()

# Exit button
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()