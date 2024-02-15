# Deleting Records
#https://youtu.be/c9_gcIeAru0?feature=shared

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import os

root = Tk()
root.title('crap baskets')
root.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')
root.geometry("378x600")


# Menu Button frame
topbar = LabelFrame(root)
topbar.pack(anchor=W)
exit_button = Button(topbar, text="Exit",command=root.quit)
exit_button.grid(row=0, column=0, pady=5)

# main window frame
main = LabelFrame(root, borderwidth=5)
main.pack()

# DB Result

result = LabelFrame(root, borderwidth=5, text="Results")
result.pack()

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

def update():
    conn = sqlite3.connect('Testing_Grounds_PY/Tkinter-Test/Learning/Database/Address Book/address_book.db')

    # Create a curser
    c = conn.cursor('''
    'first': 

'''
                    )

    # commit changes to database
    conn.commit()

    # Close connetion
    conn.close()


# Edit Function to update records
def edit():
    #Create or connect to a database
    conn = sqlite3.connect('Testing_Grounds_PY/Tkinter-Test/Learning/Database/Address Book/address_book.db')

    # Create a curser
    c = conn.cursor()

    # Get OID
    record_id = delete_box.get()
    # Query DB
    c.execute("SELECT *, oid FROM addresses WHERE oid =" + record_id)
    # Fetch can be det to different things, one many(def num)
    records = c.fetchall()
    
    editer = Tk()
    editer.title('crap baskets')
    editer.iconbitmap('Testing_Grounds_PY/Tk_images/cha0scharly.ico')
    editer.geometry("378x600")

    editor_menu=LabelFrame(editer)
    editor_menu.grid(row=0,column=0,columnspan=3,sticky=W)

    editor_exit=Button(editor_menu, text="Exit", command=editer.destroy)
    editor_exit.grid(row=0,column=0)

    editor = LabelFrame(editer)
    editor.grid(row=1, column=0, columnspan=3)

    # DB input Layout
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    postcode_editor = Entry(editor, width=30)
    postcode_editor.grid(row=5, column=1)

    # Text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    postcode_label = Label(editor, text="Postcode")
    postcode_label.grid(row=5, column=0)

    # print record for oid
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        postcode_editor.insert(0, record[5])

    # Save editoed Record
    save_btn = Button(editor, text="Save", command=lambda :[edit(), editer.destroy()])
    save_btn.grid(row=6, column=0, pady=5, padx=5, columnspan=2, ipadx=100)


# Delete Record Function
def delete():
        #Create or connect to a database
    conn = sqlite3.connect('Testing_Grounds_PY/Tkinter-Test/Learning/Database/Address Book/address_book.db')

    # Create a curser
    c = conn.cursor()

    #delete record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    # commit changes to database
    conn.commit()

    # Close connetion
    conn.close()


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
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[6]) + "\n"
    #    print_records += str(record) + "\n"
    
    query_label = Label(result, text=print_records)
    query_label.grid(row=0, column=0)

    # commit changes to database
    conn.commit()

    # Close connetion
    conn.close()

#Globalise Entrys
global f_name
global l_name
global address
global city
global state
global postcode
   
# DB input Layout
f_name = Entry(main, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
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

# Delete Box
delete_box = Entry(main, width=20)
delete_box.grid(row=8, column=1, pady=5)

# Text box labels
f_name_label = Label(main, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
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

#Delete Label
delete_label = Label(main, text="Enter ID")
delete_label.grid(row=8, column=0, sticky=E, pady=5)


# Submit button
submit_btn = Button(main, text="Submit", command=submit)
submit_btn.grid(row=6, column=0, pady=5, padx=5, columnspan=2, ipadx=100)

# Query Button
query_btn = Button(main, text="Show Record", command=query)
query_btn.grid(row=7, column=0, pady=5, padx=5, columnspan=2, ipadx=85)

#Delete Button
query_btn = Button(main, text="Delete Record", command=delete)
query_btn.grid(row=10, column=0, pady=5, ipadx=25) 

#Create an Update Button
edit_btn = Button(main, text="Edit Record", command=edit)
edit_btn.grid(row=10, column=1, pady=5, ipadx=25) 


# commit changes to database
conn.commit()

# Close connetion
conn.close()

root.mainloop()