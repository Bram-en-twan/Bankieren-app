from tkinter import *

newscreen = Tk()
newscreen.geometry('1366x768')
newscreen.configure(background='black')

Frame(newscreen,bg="orangered",width=380,height=682).place(x=40,y=40)

Frame(newscreen,bg="darkgray",width=430,height=200).place(x=470,y=40)
Frame(newscreen,bg="darkgray",width=430,height=200).place(x=470,y=280)
Frame(newscreen,bg="darkgray",width=430,height=200).place(x=470,y=520)

Frame(newscreen,bg="limegreen",width=380,height=682).place(x=946,y=40)

Label(newscreen,bg='darkgray',text='$500',font=('arial',20,'bold')).place(x=600,y=140)
