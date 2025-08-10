from tkinter import *
w =Tk()
w.title("My First Window")
w.geometry("400x300")
l1 =Label(w,text="This is our first window")
l1.pack()
l2=Label(w,text = "Example of Gui programming")
l2.pack(side= BOTTOM)
w.mainloop()
