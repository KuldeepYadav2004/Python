from tkinter import *
w =Tk()
w.title("My First Window")
w.geometry("400x300")
l1 =Label(w,text="Hello")
l1.grid(row = 0,column= 0)

l2=Label(w,text = "Hi")
l2.grid(row = 0,column= 1)

l3=Label(w,text = "Welcome")
l3.grid(row = 1,column= 0)

l4=Label(w,text = "bye")
l4.grid(row = 1,column= 1)
w.mainloop()
