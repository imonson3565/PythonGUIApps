from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

class AddPeople(Toplevel):
    def addPerson(self):
        # Retrive our values from our entries
        name = self.ent_name.get()
        surname = self.ent_surname.get()
        email = self.ent_email.get()
        phone = self.ent_phone.get()
        address = self.ent_address.get(1.0, 'end-1c')

        # Check if fields are NULL, if so show error message box
        if (name and surname and email and phone and address != ""):
            try:
                # Execute SQL query
                query = "INSERT INTO 'persons' (person_name, person_surname, person_email, person_phone, person_address) " \
                        "VALUES (?,?,?,?,?)"
                cur.execute(query, (name, surname, email, phone, address))
                con.commit()
                messagebox.showinfo("Success", "Sucessfully added contact to database!", icon = "info")

            except:
                messagebox.showerror("Error", "Unable to add contact to database!", icon = "warning")
        else:
            messagebox.showerror("Error", "Fields cannot be empty!", icon = "warning")

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Person")
        self.resizable(False, False)

        # Configure our frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and our date label
        self.top_image = PhotoImage(file='icons/addPerson.png')
        top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.top, text='Add Contact', font='arial 15 bold', fg='#003f8a', bg='white')
        heading.place(x=260, y=60)

        #################################################################

        # Entries and Labels
        self.lbl_name = Label(self.bottomFrame, text = 'Name:', font = 'arial 14 bold', fg = 'white', bg = '#fcc324')
        self.lbl_name.place(x = 40, y = 40)
        self.ent_name = Entry(self.bottomFrame, width = 30, bd = 3)
        self.ent_name.insert(0, 'Please enter a name')
        self.ent_name.place(x = 150, y = 45)

        self.lbl_surname = Label(self.bottomFrame, text = 'Surname:', font = 'arial 14 bold', fg = 'white', bg = '#fcc324')
        self.lbl_surname.place(x = 40 , y = 80)
        self.ent_surname = Entry(self.bottomFrame, width = 30, bd = 3)
        self.ent_surname.insert(0, "Please enter a surname")
        self.ent_surname.place(x = 150, y = 85)

        self.lbl_email = Label(self.bottomFrame, text = 'Email:', font = 'arial 14 bold', fg = 'white', bg = '#fcc324')
        self.lbl_email.place(x = 40, y = 120)
        self.ent_email = Entry(self.bottomFrame, width = 30, bd = 3)
        self.ent_email.insert(0, 'Please enter an email')
        self.ent_email.place(x = 150, y = 125)

        self.lbl_phone = Label(self.bottomFrame, text = 'Phone:', font = 'arial 14 bold', fg = 'white', bg = '#fcc324')
        self.lbl_phone.place(x = 40, y = 160)
        self.ent_phone = Entry(self.bottomFrame, width = 30, bd = 3)
        self.ent_phone.insert(0, 'Please enter a phone number')
        self.ent_phone.place(x = 150, y = 165)

        self.lbl_address = Label(self.bottomFrame, text = 'Address:', font = 'arial 14 bold', fg = 'white', bg = '#fcc324')
        self.lbl_address.place(x = 40, y = 300)
        self.ent_address = Text(self.bottomFrame, width = 23, height = 15, wrap = WORD)
        self.ent_address.place(x = 150, y = 200)

        button = Button(self.bottomFrame, text = 'Add Person', command = self.addPerson)
        button.place(x = 270, y = 460)

