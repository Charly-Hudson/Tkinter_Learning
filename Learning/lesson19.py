# Dropdown Boxes
#https://youtu.be/3E_fK5hCUnI?feature=shared

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('crap baskets')
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')
root.geometry("400x400")

# exit button frame
topbar = LabelFrame(root)
topbar.grid(row=1, column=0)
exit_button = Button(topbar, text="Exit",command=root.quit)
exit_button.grid(row=0, column=0, sticky=W, pady=10)


# main window frame
main = LabelFrame(root, borderwidth=5).grid(row=0, column=0)

# Databases

#Create or connect to a database
conn = sqlite3.connect('Testing_Grounds_PY/Tkinter-Test/Learning/Database/Address Book/address_book.db')

# Create a curser
c = conn.cursor()

'''
# Database Table creation
c.execute("""CREATE TABLE addresses(
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          postcode integer
          )""")
'''

# Submit function
def submit():
    #Create or connect to a database
    conn = sqlite3.connect('Testing_Grounds_PY/Tkinter-Test/Learning/Database/Address Book/address_book.db')

    # Create a curser
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :postcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'postcode': postcode.get()
              })

    # commit changes to database
    conn.commit()

    # Close connetion
    conn.close()

    # Clear text box
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    postcode.delete(0, END)

# Submit function
def query():
    #Create or connect to a database
    conn = sqlite3.connect('Testing_Grounds_PY/Tkinter-Test/Learning/Database/Address Book/address_book.db')

    # Create a curser
    c = conn.cursor()

    # Query DB
    c.execute("SELECT *, oid FROM addresses")
    # Fetch can be det to different things, one many(def num)
    records = c.fetchall()
    # To print in terminal
    # print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"
    
    query_label = Label(main, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # commit changes to database
    conn.commit()

    # Close connetion
    conn.close()


   
# DB Layout
f_name = Entry(main, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(main, width=30)
l_name.grid(row=1, column=1)
address = Entry(main, width=30)
address.grid(row=2, column=1)
city = Entry(main, width=30)
city.grid(row=3, column=1)
state = Entry(main, width=30)
state.grid(row=4, column=1)
postcode = Entry(main, width=30)
postcode.grid(row=5, column=1)

# Text box labels
f_name_label = Label(main, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(main, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(main, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(main, text="City")
city_label.grid(row=3, column=0)
state_label = Label(main, text="State")
state_label.grid(row=4, column=0)
postcode_label = Label(main, text="Postcode")
postcode_label.grid(row=5, column=0)

# Submit button

submit_btn = Button(main, text="Submit", command=submit)
submit_btn.grid(row=6, column=0, pady=10, padx=10, columnspan=2, ipadx=100)

# Query Button
query_btn = Button(main, text="Query", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)


# commit changes to database
conn.commit()

# Close connetion
conn.close()

root.mainloop()