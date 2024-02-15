from tkinter import *
from tkinter import ttk
import os
import json
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import pyperclip
import os

main = Tk()
main.title('Lesson 64 - Tabs')
main.geometry("500x500")

def calculate():
    def input_var():
        if len(req_amt_1.get()) == 0:
            req_amt_2.get()
            
        required_amount = input_var

        formatted_output = "\n".join(float(required_amount) * 10)
        ingredient_output.config(text=formatted_output)

tile1 = Frame(main)
tile1.grid(row=0,column=0)

my_notebook = ttk.Notebook(tile1)
my_notebook.pack(pady=15)

tab1=Frame(my_notebook,width=100, height=200, bg="blue")
tab1.pack(fill="both", expand=1)
my_notebook.add(tab1, text="tab 1")
req_amt_1 = Entry(tab1)
req_amt_1.pack()

tab2=Frame(my_notebook,width=100, height=200, bg="red")
tab2.pack(fill="both", expand=1)
my_notebook.add(tab2, text="tab 2")
req_amt_2 = Entry(tab2)
req_amt_2.pack()

calc_btn_frame = Frame(main)
calc_btn_frame.grid(row=1,column=0)

calc_btn= Button(calc_btn_frame, text="Calculate", command=calculate)
calc_btn.pack()

calc_output = Frame(main)
calc_output.grid(row=2,column=0)

result_label = Label(calc_output, text="", fg="#e49245", bg="#26363a", padx=10, pady=1)
result_label.pack()
ingredient_output = Label(calc_output, text="", fg="#e49245", bg="#26363a", padx=10, pady=1)
ingredient_output.pack()

main.mainloop()