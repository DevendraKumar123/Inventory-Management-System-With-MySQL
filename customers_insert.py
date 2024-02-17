import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def custinsert():
        
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Company Customers')
    lt=[]
    #----------------------------Function------------------------------------------------------
    def insertdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        xa=int(custid_entry.get())
        xb=name_entry.get()
        xc=address_entry.get()
        xd=city_entry.get()
        xe=email_entry.get()
        xf=phoneno_entry.get()
        sql="insert into customers values(%d,'%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Saved Record')
        name_entry.delete(0,100)
        address_entry.delete(0,100)
        city_entry.delete(0,100)
        email_entry.delete(0,100)
        phoneno_entry.delete(0,100)
        db.close()


    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    custid=Label(t,text='Customer Id :-',font=('Arial',10,'bold')).place(x=10,y=60)
    name=Label(t,text='Name :-',font=('Arial',10,'bold')).place(x=10,y=100)
    address=Label(t,text='Address :-',font=('Arial',10,'bold')).place(x=10,y=140)
    city=Label(t,text='City :-',font=('Arial',10,'bold')).place(x=10,y=180)
    email=Label(t,text='Email Id :-',font=('Arial',10,'bold')).place(x=10,y=220)
    phoneno=Label(t,text='Phone No :-',font=('Arial',10,'bold')).place(x=10,y=260)

    #-----------------------------Entry----------------------------------------------------------------------------------
    custid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    custid_entry.place(x=150,y=60)
    name_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    name_entry.place(x=150,y=100)
    address_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    address_entry.place(x=150,y=140)
    city_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    city_entry.place(x=150,y=180)
    email_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    email_entry.place(x=150,y=220)
    phoneno_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    phoneno_entry.place(x=150,y=260)
    #-----------------------------Button-----------------------------------------------------------
    insert=Button(t,text='Insert Record',height=2,width=10,command=insertdata).place(x=50,y=320)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=200,y=320)


    t.mainloop()
