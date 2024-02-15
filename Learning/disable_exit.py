#Import the tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry of the function
win.geometry("750x250")
win.attributes('-toolwindow', True)
def close_win():
   win.destroy()
def disable_event():
   pass
#Create a button to close the window
btn = ttk.Button(win, text ="Click here to Close",command=close_win)
btn.pack()
#Disable the Close Window Control Icon
win.protocol("WM_DELETE_WINDOW", disable_event)
win.mainloop()