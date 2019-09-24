from tkinter import *
from tkinter import PhotoImage
import tkinter
from tkinter import ttk

newscreen=Tk()
newscreen.geometry('1366x768')
newscreen.configure(background='black')

img1 = PhotoImage(file="flappen.png")

font1=("Arial",20)

value1=StringVar()


Label(newscreen,image=img1,bd=0).place(x=450, y=0)

box=ttk.Combobox(newscreen,font=font1,state='readonly')
box['values']=("gebruiker1","gebruiker2","gebruiker3")
box.current(0)
box.place(x=65,y=275, width=300,height=75)

Entry(newscreen,show='*',textvariable=value1,bd=2,font=font1,relief='groove').place(x=65,y=400, width=300,height=75)

def test():
    if value1.get() == "1":
        Frame(newscreen,width=8000,height=1000,bg="white").place(x=0,y=0)
               
    else:
        Button(newscreen,width=20,height=2,font=("Arial",20),bg="black",text="wachtwoord onjuist",bd=0,fg="white",command=test).place(x=20,y=400)
    value1.set("")

Button(newscreen,width=20,height=1,font=("Arial",25),bg="black",text="inloggen",bd=0, fg="white",command=test).place(x=20,y=500)
