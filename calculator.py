from tkinter import *

def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(num))

def clear():
    entry.delete(0, END)

def calculate():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(END, str(result))

root = Tk()
root.title("Calculator")
root.geometry("300x400")

entry = Entry(root, width=20, font=("Arial", 20))
entry.pack(pady=10)

Button(root, text="1", command=lambda: click(1)).pack(fill="x")
Button(root, text="2", command=lambda: click(2)).pack(fill="x")
Button(root, text="3", command=lambda: click(3)).pack(fill="x")
Button(root, text="+", command=lambda: click("+")).pack(fill="x")

Button(root, text="=", command=calculate).pack(fill="x")
Button(root, text="Clear", command=clear).pack(fill="x")

root.mainloop()