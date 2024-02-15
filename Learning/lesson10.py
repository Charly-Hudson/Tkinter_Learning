#Img status bar
#https://youtu.be/MGu7zKi5azQ?feature=shared

# icon, image and exit buttons
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('crap baskets')
# Needs to be an .ico file, use krita for its ez gg 
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')

#adding an imags
my_img1 = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/cha0scharly.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/background1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/background2.png"))
my_img4 = ImageTk.PhotoImage(Image.open("Testing_Grounds_PY/Tk_images/background3.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text="Image 1 / " + str(len(image_list)), bd=1,relief=SUNKEN, anchor=W)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

# Buttons

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command = lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    #status
    status = Label(root, text="Image "+ str(image_number) +" / " + str(len(image_list)), bd=1,relief=SUNKEN, anchor=W)

    status.grid(row=2,column=0,columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command = lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Status
    status = Label(root, text="Image " + str(image_number) + " / " + str(len(image_list)), bd=1,relief=SUNKEN, anchor=W)
    
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)


# buttons
button_back = Button(root, text="<<", command=back, state=DISABLED, padx=20 ,pady=10)
button_exit = Button(root, text="Exit", command=root.quit, padx=20 ,pady=10)
button_forward = Button(root, text=">>", command=lambda: forward(2), padx=20 ,pady=10)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)

root.mainloop()