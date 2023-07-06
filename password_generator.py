
from tkinter import *
import tkinter as t
import random


pas=t.Tk()
pas.title("Password Generator")
pas.geometry("500x500")


#value
c1=IntVar()
c2=IntVar()
c3=IntVar()
c4=IntVar()
length=IntVar()

#charcters list for passwords

p1= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

p2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

p3=['!', '@', '#', '$', '%', '^', '&', '*']



p4=[0,1,2,3,4,5,6,7,8,9]

def pass1():
    pasi=[]
    ln=length.get()
    if (c1.get()):
        pasi.append(p1)
    if (c2.get()):
        pasi.append(p2)
    if (c3.get()):
        pasi.append(p3)
    if (c3.get()):
        pasi.append(p4)
    passd=c1.get()+c2.get()+c3.get()+c4.get()
    if not(passd):
        return ("Please select two checks")
    pass1=[]
    for i in range (ln):
        if (i==0):
            a=1
        else:
            a=random.randint(1, passd)
        b=pasi[a-1]
        c=random.randint(0,len(b)-1)
        pass1.append(str(b[c]))
    return ("".join(pass1))





#Genearted password
pg=StringVar()
pg.set(pass1())
re=t.Entry(pas,textvariable=pg,font=("Times New Roman Baltic",14))

def fun2():
    global re
    re.pack_forget()
    pg.set(pass1())
    re=t.Entry(pas,textvariable=pg,font=("Times New Roman",14))
    re.config=("readonly")
    re.pack()










label1 = t.Label(pas, text="\nPassword Generator", font=("Times New Roman", 14))
label2 = t.Label(pas, text="Select atleast two options\n", font=("Times New Roman", 14))
label1.pack()
label2.pack()














#CHECKBUTTONS
check1=t.Checkbutton(pas,variable=c1,text="Lower Case [From:=a-z]",onvalue=1, offvalue=0)
check2=t.Checkbutton(pas,variable=c2,text="Upper Case [From:=A-Z]",onvalue=1, offvalue=0)
check3=t.Checkbutton(pas,variable=c3,text="Special Characters [example:=!@#$]",onvalue=1, offvalue=0)
check4=t.Checkbutton(pas,variable=c4,text="Numeric Value [example:=12345]",onvalue=1, offvalue=0)

sl=t.Scale(pas,variable=length,label="Please select Length of your Password",orient=HORIZONTAL,length=130,from_=8 ,to=30)
bt=t.Button(pas,text="Generate My Password Bro",command=fun2)

check1.pack()
check2.pack()
check3.pack()
check4.pack()
sl.pack()
bt.pack()
pas.mainloop()