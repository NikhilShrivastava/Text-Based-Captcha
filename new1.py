from tkinter import *
import sqlite3
import tkinter.messagebox
import tkinter as tk
master= Tk()
master.geometry('800x600+0+0')
master.title("Text Based Captcha")
regno=StringVar()
password=StringVar()
def check():
    regno1=regno.get()
    password1=password.get()
    x=sqlite3.connect("q1.db")
    #x.execute("Create table a1(regno text, password text)")
    x.execute("insert into a1(regno, password) values(?,?)",(regno1 , password1))
    y=x.execute("Select * from a1")
    for i in y:
        print(i)
    x.commit()
    if "8H72C"==cap.get():
        tkinter.messagebox.showinfo("WELCOME","Welcome to our site")
    else:
        photo=PhotoImage(file="3.png")
        label3=Label(frame2,image=photo)
        label3.grid(row=2, columnspan=2)
#FRAME1
frame1=Frame(master)
frame1.pack()
label=Label(frame1,text="Password Reminder",fg="white",bg='Blue',width=500, height=4,font=("arial",10,"bold"))
label.pack()
#FRAME 2 
frame2=Frame(master)
label2=tkinter.Label(frame2,text="Registration No",pady=20,font=("arial",9,"bold"))
label2.grid(row=0)
reg=Entry(frame2,textvariable=regno, bd=5)
reg.grid(row=0,column=1)
label4=Label(frame2,text="Password",font=("arial",9,"bold"))
password=StringVar()
pas=Entry(frame2,textvariable=password,show="*", bd=5)
label4.grid(row=1,sticky=E)
pas.grid(row=1,column=1)
photo=PhotoImage(file="1.png")
label3=Label(frame2,image=photo)
label3.grid(row=2,columnspan=2)
text=Label(frame2,text="Type The code you see above",pady=20)
text.grid(row=3,columnspan=3)
cap=StringVar()
cap=Entry(frame2,textvariable=cap,bd=5)
cap.grid(row=4,columnspan=3)
colors="#195fd1"
color="#1f577f"
c=Checkbutton(frame2,text="Keep me logged in")
c.grid(columnspan=2)
button=Button(frame2,text="SUBMIT",relief="groove",bg=colors,fg="white",width=8,height=1,activebackground=color,font=("arial",12,"bold"), command=check)
button.grid(row=6,columnspan=2)
frame2.pack()
master.mainloop
        
