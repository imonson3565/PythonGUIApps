from tkinter import *
import myPeople, addPeople, about
import datetime

date = datetime.datetime.now().date()

class Application(object):
    def __init__(self, master):
        self.master = master

        # Configure our frames
        self.top = Frame(master, height = 150, bg = 'white')
        self.top.pack(fill = X)
        self.bottom = Frame(master, height = 500, bg = '#adff2f')
        self.bottom.pack(fill = X)

        # Heading, image and our date label
        self.top_image = PhotoImage(file = 'icons/book.png')
        top_image_lbl = Label(self.top, image = self.top_image, bg = 'white')
        top_image_lbl.place(x = 120, y = 10)
        heading = Label(self.top, text = 'My Address Book APP', font = 'arial 15 bold', fg = '#ffa500', bg = 'white')
        heading.place(x = 260, y = 60)
        self.date_lbl = Label(self.top, text = "Today's Date: " + str(date), font = 'arial 12 bold', bg = 'white',
                              fg = '#ffa500')
        self.date_lbl.place(x = 450, y = 5)

        # Create buttons and place them
        self.btn1Icon = PhotoImage(file = 'icons/man.png')
        self.personBtn = Button(self.bottom, text = '  My Book       ', font = 'arial 12 bold',
                                command = self.openMyPeople)
        self.personBtn.configure(image = self.btn1Icon, compound = LEFT)

        self.btn2Icon = PhotoImage(file = 'icons/add.png')
        self.addBtn = Button(self.bottom, text = '  Add Person ', font = 'arial 12 bold', command = self.funcAddPeople)
        self.addBtn.configure(image = self.btn2Icon, compound = LEFT)

        self.btn3Icon = PhotoImage(file = 'icons/info.png')
        self.abtUsBtn = Button(self.bottom, text = '  About Us      ', font = 'arial 12 bold',
                               command = about.main)
        self.abtUsBtn.configure(image = self.btn3Icon, compound = LEFT)

        self.personBtn.place(x = 250, y = 10)
        self.addBtn.place(x = 250, y = 70)
        self.abtUsBtn.place(x = 250, y = 130)

    def openMyPeople(self):
        people = myPeople.MyPeople()

    def funcAddPeople(self):
        addpeoplewindow = addPeople.AddPeople()

def main():
    root = Tk()
    app = Application(root)
    root.title('Address Book Application')
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()
if __name__ == '__main__':
    main()