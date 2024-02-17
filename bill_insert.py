import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def billinsert():
        
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Company Bill')
    lt=[]
    #----------------------------Function------------------------------------------------------

    def insertdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(billid_entry.get())
        xa=int(orderid_entry.get())
        xb=int(custid_entry.get())
        xc=billdate_entry.get()
        xd=int(amount_entry.get())
        sql="insert into bill values(%d,'%d','%d','%s','%d')"%(x,xa,xb,xc,xd)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Saved Record')
        orderid_entry.delete(0,100)
        custid_entry.delete(0,100)
        billdate_entry.delete(0,100)
        amount_entry.delete(0,100)
        db.close()

    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    billid=Label(t,text='Bill Id :-',font=('Arial',10,'bold')).place(x=10,y=60)
    orderid=Label(t,text='Order Id :-',font=('Arial',10,'bold')).place(x=10,y=100)
    custid=Label(t,text='Customer Id :-',font=('Arial',10,'bold')).place(x=10,y=140)
    billid=Label(t,text='Bill Date :-',font=('Arial',10,'bold')).place(x=10,y=180)
    amount_=Label(t,text='Amount :-',font=('Arial',10,'bold')).place(x=10,y=220)

    #-----------------------------Entry----------------------------------------------------------------------------------
    billid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    billid_entry.place(x=150,y=60)
    orderid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    orderid_entry.place(x=150,y=100)
    custid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    custid_entry.place(x=150,y=140)
    billdate_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    billdate_entry.place(x=150,y=180)
    amount_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    amount_entry.place(x=150,y=220)
    #-----------------------------Button-----------------------------------------------------------
    insert=Button(t,text='Insert Record',height=2,width=10,command=insertdata).place(x=50,y=320)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=200,y=320)


    t.mainloop()
