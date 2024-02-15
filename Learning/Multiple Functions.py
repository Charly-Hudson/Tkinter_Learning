#Import the Tkinter Library
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of window
win.geometry("700x350")

#Define functions
def display_msg():
   label.config(text="Top List of Programming Language")

def show_list():
   listbox= Listbox(win, height=10, width= 15, bg= 'grey', activestyle= 'dotbox',font='aerial')
   listbox.insert(1,"Go")
   listbox.insert(1,"Java")
   listbox.insert(1,"Python")
   listbox.insert(1,"C++")
   listbox.insert(1,"Ruby")
   listbox.pack()
   button.destroy()

#Create a Label widget to display the message
label= Label(win, text= "", font= ('aerial 18 bold'))
label.pack(pady= 20)

#Define a Button widget
button= Button(win, text= "Click Here",command= lambda:[display_msg(), show_list()])
button.pack()
win.mainloop()