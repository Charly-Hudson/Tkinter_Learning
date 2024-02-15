from tkinter import *

main = Tk()
main.geometry("300x200")

entrys = Frame(main)
entrys.grid(row=0, column=0)

e_1 = Entry(entrys)
e_1.pack()

e_2 = Entry (entrys)
e_2.pack()

math = 5 

# MAF IS HARD PLEASE LOOK INTO THIS LATER CHARLY AND STOP PLAYING AROUND AHHDFVIHFVPIFVJHOPIOBG GOT IT!
# on to osmehting need more brian power for now first method will work just over multiple functions
# Each tab will have to have its own version, this may actually be better off for the Json files, or creating tabs within the menu
# Next task is forming the tabs to work appropriately

def calc_1():

    entry_number = e_1.get or e_2.get

    formatted_output = "\n"(entry_number + math)
    print(formatted_output)

    #ingredient_output.config(text=formatted_output)


calcs = Frame(main)
calcs.grid(row=0, column=1)

calculate_1 = Button(calcs, text="Calc 1", command=calc_1)
calculate_1.pack()

calculate_2 = Button(calcs)
calculate_2.pack()

calculate_3 = Button(calcs)
calculate_3.pack()


output_frame = LabelFrame(main)
output_frame.grid(row=1, column=0, columnspan=2)

ingredient_output = Label(output_frame, text="", fg="#e49245", bg="#26363a", padx=10, pady=1)
ingredient_output.pack()


main.mainloop()