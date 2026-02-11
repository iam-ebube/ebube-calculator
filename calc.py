import math
from tkinter import *

root = Tk()
root.title("ebube calculator")
root.geometry("400x500")

e = Entry(root, borderwidth=5, width=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math_op == "addition":
        e.insert(0, f_num + int(second_number))

    if math_op == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math_op == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math_op == "division":
        e.insert(0, f_num / int(second_number))


def button_add():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "division"
    f_num = int(first_number)
    e.delete(0, END)


# ---------------- BUTTONS ----------------

Button(root, text="1", command=lambda: button_click(1)).grid(row=3, column=0, sticky="nsew")
Button(root, text="2", command=lambda: button_click(2)).grid(row=3, column=1, sticky="nsew")
Button(root, text="3", command=lambda: button_click(3)).grid(row=3, column=2, sticky="nsew")

Button(root, text="4", command=lambda: button_click(4)).grid(row=2, column=0, sticky="nsew")
Button(root, text="5", command=lambda: button_click(5)).grid(row=2, column=1, sticky="nsew")
Button(root, text="6", command=lambda: button_click(6)).grid(row=2, column=2, sticky="nsew")

Button(root, text="7", command=lambda: button_click(7)).grid(row=1, column=0, sticky="nsew")
Button(root, text="8", command=lambda: button_click(8)).grid(row=1, column=1, sticky="nsew")
Button(root, text="9", command=lambda: button_click(9)).grid(row=1, column=2, sticky="nsew")

Button(root, text="0", command=lambda: button_click(0)).grid(row=4, column=0, sticky="nsew")
Button(root, text="Clear", command=button_clear).grid(row=4, column=1, columnspan=2, sticky="nsew")

Button(root, text="+", command=button_add).grid(row=5, column=0, sticky="nsew")
Button(root, text="=", command=button_equal).grid(row=5, column=1, columnspan=2, sticky="nsew")

Button(root, text="-", command=button_subtract).grid(row=6, column=0, sticky="nsew")
Button(root, text="*", command=button_multiply).grid(row=6, column=1, sticky="nsew")
Button(root, text="/", command=button_divide).grid(row=6, column=2, sticky="nsew")


# ---------------- MAKE WINDOW RESPONSIVE ----------------

for i in range(7):   # total rows
    root.grid_rowconfigure(i, weight=1)

for i in range(3):   # total columns
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
