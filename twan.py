from tkinter import *
import tkinter
from sys import argv
import tkinter as tk
import time, re, webbrowser, zipfile, shutil, os#, win32api
from tkinter import Tk, PhotoImage, messagebox, ttk, colorchooser
import urllib.request as urllib2
from pathlib import Path

newscr = Tk()
newscr.geometry('1366x768')
newscr.configure(background='white')
newscr.resizable(False, False)
needed="1"
access1 = float
access1 = (0)
username = os.getlogin()
class app():
    def __init__(self):
        #Button(LG,text="run",command=self.run_progressBar).place(x=0,y=0)
        Label(newscr,text="Bezig met Updaten", font=('arial',20,'bold'),bg="white").place(x=530,y=400)
        s = ttk.Style()
        s.theme_use('default')
        s.configure("Horizontal.TProgressbar", foreground='red', background='red')
        self.progress_bar = ttk.Progressbar(newscr,style="Horizontal.TProgressbar", orient = 'horizontal', length = 400)
        self.progress_bar.place(x=450,y=500)
        #def run_progressBar(self):
         
        self.progress_bar['maximum']=100

        for i in range(101):
            time.sleep(0.03)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0
def internet_on():
    def wifi():
        data = urllib2.urlopen('https://github.com/bramteunis/bankcode/blob/master/test.txt').read()
        data1 = re.findall(r'<td id="LC1" class="blob-code blob-code-inner js-file-line">(.*?)</td>',str(data))
        if data1[0] == needed: pass
        else:
            if messagebox.askyesno("Systeem", "Je hebt een update nodig. Wil je deze downloaden") == True:
                access1 = (1)
                webbrowser.open_new_tab('https://github.com/bramteunis/bankcode/archive/master.zip')
                for x in range (0,500):
                    app()
                    my_file = Path('C:/Users/'+str(username)+'/Downloads/bankcode-master.zip')
                    if my_file.is_file():
                        shutil.rmtree('C:/Users/'+str(username)+'/Downloads/SchoolSysteem/bankcode-master')   
                        #shutil.move('-myprogram-master.zip','C:/Users/bramt/Desktop')
                        zib_obj = zipfile.ZipFile('C:/Users/'+str(username)+'/Downloads/bankcode-master.zip','r')
                        zib_obj.extractall('C:/Users/'+str(username)+'/Downloads/SchoolSysteem')
                        zib_obj.close()
                        os.remove("C:/Users/"+str(username)+"/Downloads/bankcode-master.zip")
                        break
                    else:
                        #counter = float
                        #counter += (1)
                        #if counter == (99):
                        #    messagebox.showinfo("Systeem", "Controleer of je Internet hebt en probeer het opnieuw")
                        pass
            else: app()
        

    def geenwifi():
        messagebox.showinfo("Systeem", "Zorg ervoor dat je wifi hebt");internet_on()
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        wifi()
    except urllib2.URLError as err:
        geenwifi()

internet_on()
if access1 == (0):
    newscreen = Frame(newscr,bg="black",bd=0,width=1400,height=900).place(x=0,y=0)
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

    can = Canvas(newscreen,bg="black",bd=0, highlightthickness=0,scrollregion=(0,0,0,500),height = 1000)
    #vbar=Scrollbar(newscreen,orient=VERTICAL)
    #vbar.pack(side=RIGHT,fill=Y)
    #vbar.config(command=can.yview)
    can.place(x=946,y=40)
    can.config(width=img1.width(), height=img1.height())
    can.create_image(2, 2, image=img1, anchor=NW)

    can2 = Canvas(newscreen,bg="black",bd=0, highlightthickness=0);can2.place(x=40,y=40);can2.config(width=img2.width(), height=img2.height());can2.create_image(2, 2, image=img2, anchor=NW)

    a4 = open("bedrag.txt", "r").readlines()[0]; besteden=a4.strip()
    a4 = open("spaardoel.txt", "r").readlines()[0]; spaardoel=a4.strip()
    Label(newscreen,image=img3,text=f"Te besteden: \n\n €{besteden}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=40)
    Label(newscreen,image=img3,bd=0).place(x=470,y=280)
    Label(newscreen,image=img3,text=f"Nog te sparen:\n\n €{spaardoel}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=520)
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
            if nu == (1): y1=(30);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (2): y1=(70);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (3): y1=(110);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (4): y1=(150);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (5): y1=(190);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (6): y1=(230);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (7): y1=(270);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (8): y1=(310);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (9): y1=(350);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (10): y1=(390);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (11): y1=(430);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (12): y1=(470);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (13): y1=(510);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (14): y1=(550);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (15): y1=(590);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (16): y1=(630);can.create_text (180, y1, text =f"{moneycount}"+"€",font=("arial",25))
            def reset():
                can = Canvas(newscreen,bg="black",bd=0, highlightthickness=0,scrollregion=(0,0,0,500),height = 1000)
                can.place(x=946,y=40)
                can.config(width=img1.width(), height=img1.height())
                can.create_image(2, 2, image=img1, anchor=NW)
                def loop1(var1):replace_line("plus.txt",var1,""+"\n")
                loop1(5);loop1(6);loop1(7);loop1(8);loop1(9);loop1(10);loop1(11);loop1(12);loop1(13);loop1(14);loop1(15);loop1(16);loop1(17);loop1(18);loop1(19);loop1(20)
                replace_line("plus.txt",0,"1"+"\n")
                replace_line("plus.txt",1,"5"+"\n")
                can.create_text (180, 30, text =f"{moneycount}"+"€",font=("arial",25))
            if nu == (17): reset()
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

            a4 = open("spaardoel.txt", "r").readlines()[0]; spaardoel1=a4.strip(); spaardoel=int(spaardoel1)
            totaal1 = spaardoel - moneycount3; totaal=str(totaal1)
            replace_line("spaardoel.txt",0,totaal+"\n")
            a4 = open("spaardoel.txt", "r").readlines()[0]; spaardoel=a4.strip()
            Label(newscreen,image=img3,text=f"Nog te sparen:\n\n €{spaardoel}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=520)
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

            a4 = open("spaardoel.txt", "r").readlines()[0]; spaardoel1=a4.strip(); spaardoel=int(spaardoel1)
            totaal1 = spaardoel + moneycount3; totaal=str(totaal1)
            replace_line("spaardoel.txt",0,totaal+"\n")
            a4 = open("spaardoel.txt", "r").readlines()[0]; spaardoel=a4.strip()
            Label(newscreen,image=img3,text=f"Nog te sparen:\n\n €{spaardoel}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=520)
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
    def we():
        a4 = open("bedrag.txt", "r").readlines()[0]; bested=a4.strip(); besteden = int(bested)
        #moneycount2 = money.get()
        moneycount3 = int(money.get())
        ns= moneycount3 - besteden
        ns2 = str(ns)
        #print(ns)
        replace_line("spaardoel.txt",0,ns2)
        a4 = open("spaardoel.txt", "r").readlines()[0]; spaardoel=a4.strip()
        Label(newscreen,image=img3,text=f"Nog te sparen:\n\n €{spaardoel}",font=('arial',25), compound=tkinter.CENTER,bd=0,bg="black").place(x=470,y=520)
    Button(newscreen,bd=0,  font=('arial',15),text=("<"),command=add).place(x=809,y=308, width=65,height=65)
    Button(newscreen,bd=0,  font=('arial',15),text=("€"),command=we).place(x=809,y=396, width=65,height=65)
    Button(newscreen,bd=0, bg="limegreen", font=('arial',15),text=("+"),command=plus).place(x=500,y=308, width=65,height=65)
    Button(newscreen,bd=0, bg="red", font=('arial',15),text=("-"),command=min).place(x=500,y=396, width=65,height=65)
else:
    newscr.destroy()


