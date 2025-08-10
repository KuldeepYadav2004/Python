from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

w = Tk()

w.title("Mini Calculator")

l1 = Label(w, text = "Enter first number:")
l1.grid(row=0, column=0)

e1 = Entry(w)
e1.grid(row=0, column=1)

l2 = Label(w, text = "Enter second number:")
l2.grid(row=1, column=0)

e2 = Entry(w)
e2.grid(row=1, column=1)

def validate():
    if e1.get() == "":
        e1.focus()
        return "Please enter first number"
    elif not e1.get().isdigit():
        e1.delete(0, len(e1.get()))
        e1.focus()
        return "Invalid first number"
    elif e2.get() == "":
        e2.focus()
        return "Please enter second number"
    elif not e2.get().isdigit():
        e2.delete(0, len(e2.get()))
        e2.focus()
        return "Invalid second number"
    else:
        return "Data is Valid"
    
def add_numbers():
    msg = validate()
    if msg == "Data is Valid":
        r = int(e1.get()) + int(e2.get())
        messagebox.showinfo("Success Message", "Addition: " + str(r))
    else:
        messagebox.showerror("Error Message", msg)
        
def subtract_numbers():
    msg = validate()
    if msg == "Data is Valid":
        r = int(e1.get()) - int(e2.get())
        messagebox.showinfo("Success Message", "Subtraction: " + str(r))
    else:
        messagebox.showerror("Error Message", msg)
        
def multiply_numbers():
    msg = validate()
    if msg == "Data is Valid":
        r = int(e1.get()) * int(e2.get())
        messagebox.showinfo("Success Message", "Multiplication: " + str(r))
    else:
        messagebox.showerror("Error Message", msg)
        
def divide_numbers():
    msg = validate()
    if msg == "Data is Valid":
        try:
            r = int(e1.get()) / int(e2.get())
        except Exception as e:
            messagebox.showerror("Error Message", str(e) + "\nPlease try again")
        else:
            messagebox.showinfo("Success Message", "Division: " + str(round(r, 2)))
    else:
        messagebox.showerror("Error Message", msg)
        
        
b1 = Button(w, text = "Add", command=add_numbers)
b1.grid(row=2,column=0)

b2 = Button(w, text = "Subtract", command=subtract_numbers)
b2.grid(row=2,column=1)

b1 = Button(w, text = "Multiply", command=multiply_numbers)
b1.grid(row=3,column=0)

b2 = Button(w, text = "Divide", command=divide_numbers)
b2.grid(row=3,column=1)

w.mainloop()
