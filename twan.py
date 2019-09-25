from tkinter import *
from tkinter import PhotoImage
import tkinter
##from PIL import Image, ImageTk
##import tkinter as tk
##
##
##class BkgrFrame(tk.Frame):
##    def __init__(self, parent, file_path, width, height, bd, bg):
##        super(BkgrFrame, self).__init__(parent, borderwidth=0, highlightthickness=0)
##
##        self.canvas = tk.Canvas(self, width=width, height=height, bd=bd, bg=bg)
##        self.canvas.pack()
##
##        pil_img = Image.open(file_path)
##        self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.ANTIALIAS))
##        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
##
##    def add(self, widget, x, y):
##        canvas_window = self.canvas.create_window(x, y, anchor=tk.NW, window=widget)
##        return widget

newscreen = Tk()
newscreen.geometry('1366x768')
newscreen.configure(background='black')
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    
t1=Canvas(newscreen,bg="black",width=1500,height=800)
img1 = PhotoImage(file="limegreen.png")
img2 = PhotoImage(file="red.png")
img3 = PhotoImage(file="grey.png")
img4 = PhotoImage(file="midden.png")
money=StringVar()
Label(newscreen,image=img1,bd=0).place(x=946,y=40)

Label(newscreen,image=img2,bd=0).place(x=40,y=40)

Label(newscreen,image=img3,text="Te besteden: \n\n $500",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)
Label(newscreen,image=img3,bd=0).place(x=470,y=280)
Label(newscreen,image=img3,bd=0).place(x=470,y=520)
Entry(newscreen,bd=0, font=('arial',15),textvariable=money).place(x=585,y=394, width=197,height=65)
Label (newscreen,text="invoer:",font=('arial',15,)).place(x=585,y=308, width=197,height=65)
##IMAGE_PATH = 'limegreen.png'
##WIDTH, HEIGTH = 400, 600
##bkrgframe = BkgrFrame(newscreen, IMAGE_PATH, WIDTH, HEIGTH, 0,"black")
##bkrgframe.place(x=946,y=40)
##button1 = bkrgframe.add(tk.Button(newscreen, text="Start"), 10, 10)
##button2 = bkrgframe.add(tk.Button(newscreen, text="Continue"), 50, 10)
def add():
    moneycount = money.get()
    if "+" in moneycount:
        a4 = open("plus.txt", "r").readlines()[0]; plus1=a4.strip()
        count = 0 
        current = "" 
        for i in plus1:
            count += 1
            current += i
            if current == plus1:
                nu=count
        y1=int
        if nu == (1): y1=(60)
        if nu == (2): y1=(120)
        if nu == (3): y1=(180)
        if nu == (4): y1=(240)
        if nu == (5): y1=(300)
        if nu == (6): y1=(360)
        Label(newscreen,text=f"{moneycount}"+"€",font=("arial",25)).place(x=986,y=y1)
        replace_line("plus.txt",0,(plus1)+("1"))
    if "-" in moneycount:
        a4 = open("min.txt", "r").readlines()[0]; plus1=a4.strip()
        count = 0 
        current = "" 
        for i in plus1:
            count += 1
            current += i
            if current == plus1:
                nu=count
        y1=int
        if nu == (1): y1=(60)
        if nu == (2): y1=(120)
        if nu == (3): y1=(180)
        if nu == (4): y1=(240)
        if nu == (5): y1=(300)
        if nu == (6): y1=(360)
        Label(newscreen,text=f"{moneycount}"+"€",font=("arial",25)).place(x=80,y=y1)
        replace_line("min.txt",0,(plus1)+("1"))
Button(newscreen,bd=0,  font=('arial',15),text=("<"),command=add).place(x=809,y=308, width=65,height=150)
Button(newscreen,bd=0, bg="limegreen", font=('arial',15),text=("+"),command=add).place(x=500,y=308, width=65,height=65)
Button(newscreen,bd=0, bg="red", font=('arial',15),text=("-"),command=add).place(x=500,y=396, width=65,height=65)
#Label(newscreen,bg='black',width=20,height=4,text='$500',fg="white",font=('arial',20,'bold')).place(x=600,y=140)
#f3.create_text (0, 0, text ="$5464567", font = ("arial", 20,'bold'))

#img3.text((0, 0),"Sample Text",(255,255,255))

