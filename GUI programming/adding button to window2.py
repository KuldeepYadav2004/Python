from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

w =Tk()
w.title("My First Window")
w.geometry("400x300")
def button_click():
    messagebox.showinfo("Message","you have clicked me")

b = Button(w,text="click me ",command= button_click)
b.pack()


w.mainloop()
