import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def billinsert():
        
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Bill Insert')
    t.iconbitmap('ims.ico')
    t.config(bg='sky blue')
    t.resizable(0,0)
    lt=[]
    #----------------------------Function------------------------------------------------------

    def insertdata():
        if len(billid_entry.get())==0 or len(orderid_entry.get())==0  or len(custid_entry.get())==0 or len(billdate_entry.get())==0  or len(amount_entry.get())==0 :
            # messagebox.showerror("hi","Pls fill all data")
            notif1.config(text='Plz fill all Data..')
        else:
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
    
    def searchId():
        if len(billid_entry.get())==0:
            notif.config(text='Plz fill Bill Id..')
        else:
            x=int(billid_entry.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur=db.cursor()
            sql="select count(*) from bill where billid=%d"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                notif.config(text='Pls go Ahead...')
                # messagebox.showerror('hi','Already Exists...')
            else:
                notif.config(text='Already Exists..')
                # messagebox.showinfo('hi','Pls go Ahead...')
            db.close()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    billid=Label(t,text='Bill Id :-',font=('Arial',13,'bold'),bg='sky blue').place(x=10,y=60)
    orderid=Label(t,text='Order Id :-',font=('Arial',13,'bold'),bg='sky blue').place(x=10,y=100)
    custid=Label(t,text='Customer Id :-',font=('Arial',13,'bold'),bg='sky blue').place(x=10,y=140)
    billid=Label(t,text='Bill Date :-',font=('Arial',13,'bold'),bg='sky blue').place(x=10,y=180)
    amount_=Label(t,text='Amount :-',font=('Arial',13,'bold'),bg='sky blue').place(x=10,y=220)
    
    notif=Label(t,fg='red',bg='sky blue',font=('arial',13,'bold'))
    notif.place(x=350,y=90)
    notif1=Label(t,fg='red',bg='sky blue',font=('arial',13,'bold'))
    notif1.place(x=50,y=400)
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
    insert=Button(t,text='Insert Record',height=2,width=15,font=('Arial',10,'bold'),command=insertdata).place(x=50,y=350)
    close=Button(t,text='Close File',height=2,width=15,font=('Arial',10,'bold'),command=closefile).place(x=200,y=350)
    search=Button(t,text='Check ID',height=1,width=10,font=('arial',10,'bold'),command=searchId).place(x=350,y=60)


    t.mainloop()
