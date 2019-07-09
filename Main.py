from tkinter import *
from tkinter import PhotoImage
import tkinter

newscreen = Tk()
newscreen.geometry('1366x768')
newscreen.configure(background='black')
t1=Canvas(newscreen,bg="black",width=1500,height=800)
img1 = PhotoImage(file="limegreen.png")
img2 = PhotoImage(file="red.png")
img3 = PhotoImage(file="grey.png")
img4 = PhotoImage(file="midden.png")

Label(newscreen,image=img1,bd=0).place(x=946,y=40)

Label(newscreen,image=img2,bd=0).place(x=40,y=40)

Label(newscreen,image=img3,text="Te besteden: \n\n $500",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)
Label(newscreen,image=img3,bd=0).place(x=470,y=280)
Label(newscreen,image=img3,bd=0).place(x=470,y=520)
Entry(newscreen,font=('arial',))
#Label(newscreen,bg='black',width=20,height=4,text='$500',fg="white",font=('arial',20,'bold')).place(x=600,y=140)
#f3.create_text (0, 0, text ="$5464567", font = ("arial", 20,'bold'))

#img3.text((0, 0),"Sample Text",(255,255,255))

