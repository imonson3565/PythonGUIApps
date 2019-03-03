from tkinter import *
root = Tk()
root.title("Calculator Application")
root.geometry("380x550+850+200")
root.resizable(False, False)
###################################

# Functions
def enterNumber(x):
    if entry_box.get() == "0":
        entry_box.delete(0, "end")
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        # print("Index of entry box: " + str(length))
        entry_box.insert(length, str(x))

def enterOperator(x):
    if entry_box.get() != "0":
        length = len(entry_box.get())
        entry_box.insert(length, btn_operators[x]['text'])

def funcClear():
    entry_box.delete(0, END)
    entry_box.insert(0, "0")
result = 0
result_list = []
def funcOperator():
    # Get our content
    content = entry_box.get()
    # Use the eval() function to process our result
    result = eval(content)
    entry_box.delete(0, END)
    entry_box.insert(0, str(result))

    # Take our result and put it into our list
    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text = 'History: ' + '|'.join(result_list))

def funcDelete():
    length = len(entry_box.get())
    entry_box.delete(length - 1, 'end')
    if length == 1:
        entry_box.insert(0, '0')


entry_box = Entry(font = 'verdana 10 bold', width = 34, bd = 10, justify = RIGHT, bg = '#e6e6fa')
entry_box.insert(0, "0")
entry_box.place(x = 20, y = 10)

# Create our empty list, append buttons
btn_numbers = []
for i in range(10):
    btn_numbers.append(Button(width = 4, text = str(i), font = 'times 13 bold', bd = 4,
                       command = lambda x = i:enterNumber(x)))

btn_text = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn_numbers[btn_text].place(x = 25 + j * 90, y = 70 + i * 70)
        btn_text += 1

# Create our operator buttons
btn_operators = []
for i in range(4):
    btn_operators.append(Button(width = 4, font = 'times 13 bold', bd = 4, command = lambda x = i:enterOperator(x)))
btn_operators[0]['text'] = "+"
btn_operators[1]['text'] = "-"
btn_operators[2]['text'] = "*"
btn_operators[3]['text'] = "/"

# Place them
for i in range(4):
    btn_operators[i].place(x = 290, y = 70 + i * 70)

# Other buttons (clear, 0, ., =)
btn_zero = Button(width = 19, text = '0', font = 'times 13 bold', bd = 4, command = lambda x = 0: enterNumber(x))
btn_clear = Button(width = 4, text = 'C', font = 'times 13 bold', bd = 4, command = funcClear)
btn_dot = Button(width = 4, text = '.', font = 'times 13 bold', bd = 4, command = lambda x = '.': enterNumber(x))
btn_equal = Button(width = 4, text = '=', font = 'times 13 bold', bd = 4, command = funcOperator)

icon = PhotoImage(file = 'arrow.png')
btn_delete = Button(width = 50, height = 27, font = 'times 13 bold', bd = 4, command =funcDelete, image = icon )
btn_delete.place(x = 290, y = 340)

# Status bar
statusBar = Label(root, text = 'History: ', relief = SUNKEN, height = 3, anchor = W, font = 'verdana 10 bold')
statusBar.pack(side = BOTTOM, fill = X)

btn_dot.place(x = 110, y = 340)
btn_zero.place(x = 25, y = 280)
btn_clear.place(x = 25, y = 340)
btn_equal.place(x = 200, y = 340)



root.mainloop()