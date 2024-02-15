# Simple calculator 
# https://youtu.be/oq3lJdhnPp8?si=NwElDDY-CZ_obCGT

from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_ce():
    e.delete(0, END)

def button_plus():
    first_number = e.get()
    global f_num 
    global math 
    math = "plus"
    f_num = int(first_number)
    e.delete(0, END)

def button_minus():
    first_number = e.get()
    global f_num 
    global math 
    math = "minus"
    f_num = int(first_number)
    e.delete(0, END)

def button_times():
    first_number = e.get()
    global f_num 
    global math 
    math = "times"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num 
    global math 
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "plus":
        e.insert(0, f_num + int(second_number))

    if math == "minus":
        e.insert(0, f_num - int(second_number))

    if math == "times":
        e.insert(0, f_num * int(second_number))

    if math == "divide":
        e.insert(0, f_num / int(second_number))



# Define layout
button_1 = Button(root, text="1", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=17, pady=10, fg="#e49245", bg="#4c5b5f", command= button_plus)
button_equal = Button(root, text="=", padx=100, pady=10, fg="#e49245", bg="#4c5b5f", command=button_equal)
button_clear = Button(root, text="Clear", padx=37, pady=10, fg="#e49245", bg="#4c5b5f", command=button_ce)

button_minus = Button(root, text="-", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_minus)
button_times = Button(root, text="*", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_times)
button_divide = Button(root, text="/", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_divide)

# Button Layout

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0,)

button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=0, columnspan=4)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_times.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
