from tkinter import *

root = Tk()
root.geometry("300x450")
root.title("Simple Calculator")

entry = Entry(root, font="Arial 20", width=16, borderwidth=5, relief=RIDGE, justify=RIGHT)
entry.pack(pady=10)

button_frame = Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["Back"]
]

def on_click(event):
    bt = event.widget["text"]
    if bt == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, result)
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif bt == "C":
        entry.delete(0, END)
    elif bt == "Back":
        current = entry.get()
        entry.delete(0, END)
        entry.insert(END, current[:-1])
    else:
        entry.insert(END, bt)

for row in buttons:
    row_frame = Frame(button_frame)
    row_frame.pack()
    for btn_text in row:
        btn = Button(row_frame, text=btn_text, font="Arial 18", width=5, height=2)
        btn.pack(side=LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()
