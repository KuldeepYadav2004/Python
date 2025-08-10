from tkinter import *
w =Tk()
w.title("My First Window")
w.geometry("400x300")
l1 =Label(w,text="Hello, hi how are you")
l1.place(x = 10,y= 25)

l2=Label(w,text = "I am fine thank you")
l2.place(x = 125,y= 150)


w.mainloop()
