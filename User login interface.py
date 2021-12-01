# Create user login interface
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def loginStatus():
    uName = e1.get()
    pWord = e2.get()

    if(uName == "" or pWord ==""):
        messagebox.showinfo("","Blank not allowed")
    elif(uName == "Admin" or pWord =="123"):
        messagebox.showinfo("","Logged in Successfully")
        root.destroy()
    else:
        messagebox.showinfo("","Incorrect Username or Password")
    
root = tk.Tk()
root.title("Login")
root.geometry("300x300")
global e1
global e2

Label(root,text = "Username: ").place(x=10,y=10)
Label(root,text = "Password: ").place(x=10,y=40)

e1=Entry(root)
e1.place(x=140,y=10)

e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")

Button(root,text="Login",command=loginStatus,height=3,width=13).place(x=10,y=100)

root.mainloop()
