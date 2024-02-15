# Radio Buttons 
#https://youtu.be/uqJZWLlnSqs?feature=shared

from tkinter import *
from PIL import ImageTk,Image

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
r = IntVar()
r.set("2")

# Call this the what you need ie MODES = Toppings
TOPPINGS = [
    ("Peperoni","Peperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set ("pepperoni")

for text, Topping in TOPPINGS:
    Radiobutton(main, text=text, variable=pizza, value=Topping).pack(anchor=W)

def clicked(value):
    my_label = Label(main, text=value)
    my_label.pack()

#Radiobutton(main, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(main, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#my_label = Label(main, text=pizza.get())
#my_label.pack()

my_button = Button(main, text="Click Me", command=lambda: clicked(pizza.get()))
my_button.pack()


mainloop()