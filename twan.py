from tkinter import *
from tkinter import PhotoImage
import tkinter
from sys import argv

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

can = Canvas(newscreen,bg="black",bd=0, highlightthickness=0);can.place(x=946,y=40);can.config(width=img1.width(), height=img1.height());can.create_image(2, 2, image=img1, anchor=NW)
can2 = Canvas(newscreen,bg="black",bd=0, highlightthickness=0);can2.place(x=40,y=40);can2.config(width=img2.width(), height=img2.height());can2.create_image(2, 2, image=img2, anchor=NW)

a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
Label(newscreen,image=img3,text=f"Te besteden: \n\n €{besteden}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)
Label(newscreen,image=img3,bd=0).place(x=470,y=280)
Label(newscreen,image=img3,bd=0).place(x=470,y=520)
Entry(newscreen,bd=0, font=('arial',15),textvariable=money).place(x=585,y=394, width=197,height=65)
Label (newscreen,text="invoer:",font=('arial',15,)).place(x=585,y=308, width=197,height=65)
a4 = open("plus.txt", "r").readlines()[5]; line5=a4.strip()
a4 = open("plus.txt", "r").readlines()[6]; line6=a4.strip()
a4 = open("plus.txt", "r").readlines()[7]; line7=a4.strip()
a4 = open("plus.txt", "r").readlines()[8]; line8=a4.strip()
a4 = open("plus.txt", "r").readlines()[9]; line9=a4.strip()
a4 = open("plus.txt", "r").readlines()[10]; line10=a4.strip()
a4 = open("plus.txt", "r").readlines()[11]; line11=a4.strip()
a4 = open("plus.txt", "r").readlines()[12]; line12=a4.strip()
a4 = open("plus.txt", "r").readlines()[13]; line13=a4.strip()
a4 = open("plus.txt", "r").readlines()[14]; line14=a4.strip()
a4 = open("plus.txt", "r").readlines()[15]; line15=a4.strip()
a4 = open("plus.txt", "r").readlines()[16]; line16=a4.strip()
a4 = open("plus.txt", "r").readlines()[17]; line17=a4.strip()
a4 = open("plus.txt", "r").readlines()[18]; line18=a4.strip()
a4 = open("plus.txt", "r").readlines()[19]; line19=a4.strip()
a4 = open("plus.txt", "r").readlines()[20]; line20=a4.strip()
def CanCreate(bedrag,x1): can.create_text (180, x1, text =f"{bedrag}"+"€",font=("arial",25))
if line5 != "":CanCreate(line5,30)
if line6 != "":CanCreate(line6,70)
if line7 != "":CanCreate(line7,110)
if line8 != "":CanCreate(line8,150)
if line9 != "":CanCreate(line9,190)
if line10 != "":CanCreate(line10,230)
if line11 != "":CanCreate(line11,270)
if line12 != "":CanCreate(line12,310)
if line13 != "":CanCreate(line13,350)
if line14 != "":CanCreate(line14,390)
if line15 != "":CanCreate(line15,430)
if line16 != "":CanCreate(line16,470)
if line17 != "":CanCreate(line17,510)
if line18 != "":CanCreate(line18,550)
if line19 != "":CanCreate(line19,590)
if line20 != "":CanCreate(line20,630)

a4 = open("min.txt", "r").readlines()[5]; aline5=a4.strip()
a4 = open("min.txt", "r").readlines()[6]; aline6=a4.strip()
a4 = open("min.txt", "r").readlines()[7]; aline7=a4.strip()
a4 = open("min.txt", "r").readlines()[8]; aline8=a4.strip()
a4 = open("min.txt", "r").readlines()[9]; aline9=a4.strip()
a4 = open("min.txt", "r").readlines()[10]; aline10=a4.strip()
a4 = open("min.txt", "r").readlines()[11]; aline11=a4.strip()
a4 = open("min.txt", "r").readlines()[12]; aline12=a4.strip()
a4 = open("min.txt", "r").readlines()[13]; aline13=a4.strip()
a4 = open("min.txt", "r").readlines()[14]; aline14=a4.strip()
a4 = open("min.txt", "r").readlines()[15]; aline15=a4.strip()
a4 = open("min.txt", "r").readlines()[16]; aline16=a4.strip()
a4 = open("min.txt", "r").readlines()[17]; aline17=a4.strip()
a4 = open("min.txt", "r").readlines()[18]; aline18=a4.strip()
a4 = open("min.txt", "r").readlines()[19]; aline19=a4.strip()
a4 = open("min.txt", "r").readlines()[20]; aline20=a4.strip()
def CanCreate(bedrag,x1): can2.create_text (180, x1, text =f"{bedrag}"+"€",font=("arial",25))
if aline5 != "":CanCreate(aline5,30)
if aline6 != "":CanCreate(aline6,70)
if aline7 != "":CanCreate(aline7,110)
if aline8 != "":CanCreate(aline8,150)
if aline9 != "":CanCreate(aline9,190)
if aline10 != "":CanCreate(aline10,230)
if aline11 != "":CanCreate(aline11,270)
if aline12 != "":CanCreate(aline12,310)
if aline13 != "":CanCreate(aline13,350)
if aline14 != "":CanCreate(aline14,390)
if aline15 != "":CanCreate(aline15,430)
if aline16 != "":CanCreate(aline16,470)
if aline17 != "":CanCreate(aline17,510)
if aline18 != "":CanCreate(aline18,550)
if aline19 != "":CanCreate(aline19,590)
if aline20 != "":CanCreate(aline20,630)
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
        if nu == (1): y1=(30)
        if nu == (2): y1=(70)
        if nu == (3): y1=(110)
        if nu == (4): y1=(150)
        if nu == (5): y1=(190)
        if nu == (6): y1=(230)
        if nu == (7): y1=(270)
        if nu == (8): y1=(310)
        if nu == (9): y1=(350)
        if nu == (10): y1=(390)
        if nu == (11): y1=(430)
        if nu == (12): y1=(470)
        if nu == (13): y1=(510)
        if nu == (14): y1=(550)
        if nu == (15): y1=(590)
        if nu == (16): y1=(630)
        can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
        moneycount2 = moneycount.replace("+", "")
        moneycount3 = int(moneycount2)
        a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
        bedrag = int(besteden)
        subtotaal = bedrag + moneycount3
        subtotaal2 = str(subtotaal)
        a4 = open("plus.txt", "r").readlines()[1]; ccounter1=a4.strip(); counter1=int(ccounter1)
        nnewcounter1=counter1+(1); newcounter1=str(nnewcounter1)
        replace_line("bedrag.txt",0,subtotaal2+"\n")
        replace_line("plus.txt",0,(plus1)+("1\n"))
        replace_line("plus.txt",counter1,moneycount+"\n")
        replace_line("plus.txt",1,newcounter1+"\n")
        a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
        Label(newscreen,image=img3,text=f"Te besteden: \n\n €{besteden}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)
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
        if nu == (1): y1=(30)
        if nu == (2): y1=(70)
        if nu == (3): y1=(110)
        if nu == (4): y1=(150)
        if nu == (5): y1=(190)
        if nu == (6): y1=(230)
        if nu == (7): y1=(270)
        if nu == (8): y1=(310)
        if nu == (9): y1=(350)
        if nu == (10): y1=(390)
        if nu == (11): y1=(430)
        if nu == (12): y1=(470)
        if nu == (13): y1=(510)
        if nu == (14): y1=(550)
        if nu == (15): y1=(590)
        if nu == (16): y1=(630)
        can2.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
        moneycount2 = moneycount.replace("-", "")
        moneycount3 = int(moneycount2)
        a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
        bedrag = int(besteden)
        subtotaal = bedrag - moneycount3
        subtotaal2 = str(subtotaal)
        a4 = open("min.txt", "r").readlines()[1]; ccounter1=a4.strip(); counter1=int(ccounter1)
        nnewcounter1=counter1+(1); newcounter1=str(nnewcounter1)
        replace_line("bedrag.txt",0,subtotaal2+"\n")
        replace_line("min.txt",0,(plus1)+("1\n"))
        replace_line("min.txt",counter1,moneycount+"\n")
        replace_line("min.txt",1,newcounter1+"\n")
        a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
        Label(newscreen,image=img3,text=f"Te besteden: \n\n €{besteden}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)
def plus():
    moneycount = money.get()
    if "-" in moneycount: moneycount = moneycount.replace("-", "+")
    a4 = open("plus.txt", "r").readlines()[0]; plus1=a4.strip()
    count = 0 
    current = "" 
    for i in plus1:
        count += 1
        current += i
        if current == plus1:
            nu=count
    y1=int
    if nu == (1): y1=(30)
    if nu == (2): y1=(70)
    if nu == (3): y1=(110)
    if nu == (4): y1=(150)
    if nu == (5): y1=(190)
    if nu == (6): y1=(230)
    if nu == (7): y1=(270)
    if nu == (8): y1=(310)
    if nu == (9): y1=(350)
    if nu == (10): y1=(390)
    if nu == (11): y1=(430)
    if nu == (12): y1=(470)
    if nu == (13): y1=(510)
    if nu == (14): y1=(550)
    if nu == (15): y1=(590)
    if nu == (16): y1=(630)
    can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
    moneycount2 = moneycount.replace("+", "")
    moneycount3 = int(moneycount2)
    a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
    bedrag = int(besteden)
    subtotaal = bedrag + moneycount3
    subtotaal2 = str(subtotaal)
    a4 = open("plus.txt", "r").readlines()[1]; ccounter1=a4.strip(); counter1=int(ccounter1)
    nnewcounter1=counter1+(1); newcounter1=str(nnewcounter1)
    replace_line("bedrag.txt",0,subtotaal2+"\n")
    replace_line("plus.txt",0,(plus1)+("1\n"))
    replace_line("plus.txt",counter1,moneycount+"\n")
    replace_line("plus.txt",1,newcounter1+"\n")
    a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
    Label(newscreen,image=img3,text=f"Te besteden: \n\n €{besteden}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)
def min():
    moneycount = money.get()
    if "+" in moneycount: moneycount = moneycount.replace("+", "-")
    a4 = open("min.txt", "r").readlines()[0]; plus1=a4.strip()
    count = 0 
    current = "" 
    for i in plus1:
        count += 1
        current += i
        if current == plus1:
            nu=count
    y1=int
    if nu == (1): y1=(30)
    if nu == (2): y1=(70)
    if nu == (3): y1=(110)
    if nu == (4): y1=(150)
    if nu == (5): y1=(190)
    if nu == (6): y1=(230)
    if nu == (7): y1=(270)
    if nu == (8): y1=(310)
    if nu == (9): y1=(350)
    if nu == (10): y1=(390)
    if nu == (11): y1=(430)
    if nu == (12): y1=(470)
    if nu == (13): y1=(510)
    if nu == (14): y1=(550)
    if nu == (15): y1=(590)
    if nu == (16): y1=(630)
    can2.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
    moneycount2 = moneycount.replace("-", "")
    moneycount3 = int(moneycount2)
    a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
    bedrag = int(besteden)
    subtotaal = bedrag - moneycount3
    subtotaal2 = str(subtotaal)
    a4 = open("min.txt", "r").readlines()[1]; ccounter1=a4.strip(); counter1=int(ccounter1)
    nnewcounter1=counter1+(1); newcounter1=str(nnewcounter1)
    replace_line("bedrag.txt",0,subtotaal2+"\n")
    replace_line("min.txt",0,(plus1)+("1\n"))
    replace_line("min.txt",counter1,moneycount+"\n")
    replace_line("min.txt",1,newcounter1+"\n")
    a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
    Label(newscreen,image=img3,text=f"Te besteden: \n\n €{besteden}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)

Button(newscreen,bd=0,  font=('arial',15),text=("<"),command=add).place(x=809,y=308, width=65,height=150)
Button(newscreen,bd=0, bg="limegreen", font=('arial',15),text=("+"),command=plus).place(x=500,y=308, width=65,height=65)
Button(newscreen,bd=0, bg="red", font=('arial',15),text=("-"),command=min).place(x=500,y=396, width=65,height=65)



