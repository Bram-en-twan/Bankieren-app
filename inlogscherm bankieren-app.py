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

Label(newscreen,image=img1,bd=0).place(x=650, y=0)

box=ttk.Combobox(newscreen,font=font1,state='readonly')
box['values']=("gebruiker1","gebruiker2","gebruiker3")
box.current(0)
box.place(x=70,y=200)

Entry(newscreen,show='*',textvariable=value1,bd=2,font=font1,relief='groove').place(x=70,y=300)

def test():
    if value1.get() == "gebruiker1":
        Frame(newscreen,width=8000,height=1000,bg="white").place(x=0,y=0)
               
    else:
        Label(newscreen,width=20,height=2,font=("Arial",20),bg="black",text="wachtwoord onjuist",bd=0,fg="white").place(x=80,y=400)
    value1.set("")

Button(newscreen,width=20,height=1,font=("Arial",20),bg="black",text="inloggen",bd=0, fg="white",command=test).place(x=70,y=400)
