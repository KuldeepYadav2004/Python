from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

w =Tk()
w.title("My First Window")
w.geometry("400x300")
def button_click():
    l= Label(w,text="You have clicked me")
    l.pack()



b = Button(w,text="click me ",command= button_click)
b.pack()


w.mainloop()
