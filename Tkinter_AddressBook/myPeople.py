from tkinter import *
from tkinter import messagebox
import sqlite3
import addPeople

con = sqlite3.connect('database.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def funcAddPeople(self):
        addpage = addPeople.AddPeople()
        self.destroy()

    def funcUpdatePerson(self):
        global person_id
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]

        # Go to our Update class (window)
        updatepage = Update()

    def funcDisplayPerson(self):
        global person_id
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]

        displayPage = Display()
        self.destroy()

    def funcDeletePerson(self):
        global person_id
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]

        try:
            deleteQuery = "DELETE FROM persons WHERE person_id = ?"
            cur.execute(deleteQuery, (person_id))
            con.commit()

            messagebox.showinfo("Success", "Contact has been deleted from the database")
            self.destroy()
        except:
            messagebox.showinfo("Warning", "Unable to delete contact", icon = 'warning')

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("My People")
        self.resizable(False, False)

        # Configure our frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and our date label
        self.top_image = PhotoImage(file='icons/person_icon.png')
        top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.top, text='Contact List', font='arial 15 bold', fg='#003f8a', bg='white')
        heading.place(x=260, y=60)

        # Scrollbar
        self.sb = Scrollbar(self.bottomFrame, orient = VERTICAL)

        # Listbox
        self.listBox = Listbox(self.bottomFrame, width = 60, height = 31)
        self.listBox.grid(row = 0, column = 0, padx = (20, 0))
        self.sb.config(command = self.listBox.yview)
        self.listBox.config(yscrollcommand = self.sb.set)
        self.sb.grid(row = 0, column = 1, sticky = N + S)

        persons = cur.execute("SELECT * FROM persons").fetchall()
        # print(persons)
        # control var
        count = 0

        # Loop through our list of contacts and display them in our listbox
        for person in persons:
            self.listBox.insert(count, str(person[0]) + "-" + person[1] + " " + person[2])
            count += 1


        # Configure our buttons on the right side of the frame
        btnAdd = Button(self.bottomFrame, text = 'Add', width = 12, font = 'Sans 12 bold',
                        command = self.funcAddPeople)
        btnAdd.grid(row = 0, column = 2, sticky = N, padx = 10, pady = 10)

        btnUpdate = Button(self.bottomFrame, text = 'Update', width = 12, font = 'Sans 12 bold',
                           command = self.funcUpdatePerson)
        btnUpdate.grid(row = 0, column = 2, sticky = N, padx = 10, pady = 50)

        btnDisplay = Button(self.bottomFrame, text = 'Display', width = 12, font = 'Sans 12 bold',
                            command = self.funcDisplayPerson)
        btnDisplay.grid(row = 0, column = 2, sticky = N, padx = 10, pady = 90)

        btnDelete = Button(self.bottomFrame, text = 'Delete', width = 12, font = 'Sans 12 bold',
                           command = self.funcDeletePerson)
        btnDelete.grid(row = 0, column = 2, sticky = N, padx = 10, pady = 130)

class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Update Contact")
        self.resizable(False, False)

        global person_id
        person = cur.execute("SELECT * FROM persons WHERE person_id = ?", (person_id))
        person_info = person.fetchall()
        print(person_info)

        ## Person Info ##
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surename = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]
        #################

        # Configure our frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and our date label
        self.top_image = PhotoImage(file='icons/update.png')
        top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.top, text='Update Contact', font='arial 15 bold', fg='#003f8a', bg='white')
        heading.place(x = 200, y = 60)

        #################################################################

        # Entries and Labels
        self.lbl_name = Label(self.bottomFrame, text='Name:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_name.insert(0, self.person_name)
        self.ent_name.place(x=150, y=45)

        self.lbl_surname = Label(self.bottomFrame, text='Surname:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_surname.insert(0, self.person_surename)
        self.ent_surname.place(x=150, y=85)

        self.lbl_email = Label(self.bottomFrame, text='Email:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_email.insert(0, self.person_email)
        self.ent_email.place(x=150, y=125)

        self.lbl_phone = Label(self.bottomFrame, text='Phone:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_phone.insert(0, self.person_phone)
        self.ent_phone.place(x=150, y=165)

        self.lbl_address = Label(self.bottomFrame, text='Address:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.ent_address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.ent_address.insert('1.0', self.person_address)
        self.ent_address.place(x=150, y=200)

        button = Button(self.bottomFrame, text='Update Person', command = self.updatePerson)
        button.place(x = 250, y = 460)

    def updatePerson(self):
        person_id = self.person_id
        person_name = self.ent_name.get()
        person_surname = self.ent_surname.get()
        person_email = self.ent_email.get()
        person_phone = self.ent_phone.get()
        person_address = self.ent_address.get(1.0, 'end-1c')

        try:
            uPerson = "UPDATE persons SET person_name = ?, person_surname = ?, person_email = ?, person_phone = ?, person_address = ? WHERE person_id = ?"
            cur.execute(uPerson, (person_name, person_surname, person_email, person_phone, person_address, person_id))
            con.commit()
            messagebox.showinfo("Success", "Contact has been updated")
            self.destroy()
        except:
            messagebox.showinfo("Warning", "Contact has not been updated", icon = 'warning')

class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Display Contact")

        global person_id
        person = cur.execute("SELECT * FROM persons WHERE person_id = ?", (person_id))
        person_info = person.fetchall()
        print(person_info)

        ## Person Info ##
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surename = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]
        #################

        # Configure our frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and our date label
        self.top_image = PhotoImage(file='icons/addPerson.png')
        top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.top, text='Contact Info', font='arial 15 bold', fg='#003f8a', bg='white')
        heading.place(x=260, y=60)

        #################################################################

        # Entries and Labels
        self.lbl_name = Label(self.bottomFrame, text='Name:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_name.insert(0, self.person_name)
        self.ent_name.config(state = 'disabled')
        self.ent_name.place(x=150, y=45)

        self.lbl_surname = Label(self.bottomFrame, text='Surname:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_surname.insert(0, self.person_surename)
        self.ent_surname.config(state = 'disabled')
        self.ent_surname.place(x=150, y=85)

        self.lbl_email = Label(self.bottomFrame, text='Email:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_email.insert(0, self.person_email)
        self.ent_email.config(state = 'disabled')
        self.ent_email.place(x=150, y=125)

        self.lbl_phone = Label(self.bottomFrame, text='Phone:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_phone.insert(0, self.person_phone)
        self.ent_phone.config(state = 'disabled')
        self.ent_phone.place(x=150, y=165)

        self.lbl_address = Label(self.bottomFrame, text='Address:', font='arial 14 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.ent_address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.ent_address.insert('1.0', self.person_address)
        self.ent_address.config(state = 'disabled')
        self.ent_address.place(x=150, y=200)