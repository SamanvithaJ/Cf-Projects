import tkinter as tk
from tkinter import *
from tkinter import messagebox


def display():
    name = e1.get()
    Class = e2.get()
    roll = e3.get()
    Math = int(e4.get())
    Science = int(e5.get())
    English = int(e6.get())

    if(Math>=40 and Science>=40 and English>=40):
        messagebox.showinfo("","Remarks: Passed!")
    else:
        messagebox.showinfo("","Remarks: Failed")
    

root = tk.Tk()
root.title("Student Portfolio")
root.geometry("600x600")

global e1
global e2
global e3
global e4
global e5
global e6

Label(root,text = "Name : ").place(x=20,y=10)
Label(root,text = "Class : ").place(x=20,y=40)
Label(root,text = "Roll No. : ").place(x=20,y=70)

Label(root,text = "Subject").place(x=100,y=140)
Label(root,text = "Marks").place(x=170,y=140)
Label(root,text = "Maths").place(x=100,y=160)
Label(root,text = "Science").place(x=100,y=180)
Label(root,text = "English").place(x=100,y=200)
Label(root,text = "Maximum Marks").place(x=340,y=140)
Label(root,text = "100").place(x=340,y=160)
Label(root,text = "100").place(x=340,y=180)
Label(root,text = "100").place(x=340,y=200)

e1=Entry(root)
e1.place(x=80,y=10)
e2=Entry(root)
e2.place(x=80,y=40)
e3=Entry(root)
e3.place(x=80,y=80)
e4=Entry(root)
e4.place(x=150,y=160)
e5=Entry(root)
e5.place(x=150,y=180)
e6=Entry(root)
e6.place(x=150,y=200)

Button(root,text="Enter",command=display,height=3,width=13).place(x=80,y=300)

root.mainloop()
