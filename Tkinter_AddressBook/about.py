from tkinter import *

class About:
    def __init__(self, root):
        self.root = root

        frame = Frame(root, bg = "#ffa500", width = 550, height = 550)
        frame.pack(fill = BOTH)

        text = Label(frame, text = 'This is our about page, you can find more information here.'
                      '\n This application/project was created for educational purposes'
                      '\n based upon the learning from the python tkinter udemy course',
                     font = 'arial 12 bold', bg = '#ffa500', fg = 'white'
                     )
        text.place(x = 50, y = 70)


def main():
    root = Tk()
    app = About(root)
    root.title("About Us")
    root.geometry("550x550+550+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()