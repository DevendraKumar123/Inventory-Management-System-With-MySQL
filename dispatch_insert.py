import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def disinsert():
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Company Dispatch')
    t.config(bg='sky blue')
    t.iconbitmap('ims.ico')
    t.resizable(0,0)
    lt=[]
    #----------------------------Function------------------------------------------------------

    def insertdata():
        if len(orderid_entry.get())==0 or len(custid_entry.get())==0 or len(itemno_entry.get())==0 or len(dispatchdate_entry.get())==0 or len(qty_entry.get())==0 :
            # messagebox.showerror('Dispatch','Please Fill all data')
            notif1.config(text='Plz fill All data..')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur=db.cursor()
            x=int(orderid_entry.get())
            xa=orderid_entry.get()
            xb=custid_entry.get()
            xc=itemno_entry.get()
            xd=dispatchdate_entry.get()
            xe=qty.get()
            sql="insert into dispatch values(%d,'%d','%d','%d','%s','%d')"%(x,xa,xb,xc,xd,xe)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Hi','Saved Record')
            orderid_entry.delete(0,100)
            custid_entry.delete(0,100)
            itemno_entry.delete(0,100)
            dispatchdate_entry.delete(0,100)
            db.close()

    def closefile():
        t.destroy()

    def searchId():
        if len(orderid_entry.get())==0:
            notif.config(text='Plz fill Id..')
        else:
            x=int(orderid_entry.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur=db.cursor()
            sql="select count(*) from dispatch where orderid=%d"%(x)
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
    orderid=Label(t,text='Order Id :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=60)
    custid=Label(t,text='Customer Id :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=100)
    itemno=Label(t,text='Item No :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=140)
    dispatchdate=Label(t,text='Dispatch Date :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=180)
    qty=Label(t,text='QTY :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=220)

    notif=Label(t,fg='red',bg='sky blue',font=('arial',10,'bold'))
    notif.place(x=350,y=90)
    notif1=Label(t,fg='red',bg='sky blue',font=('arial',10,'bold'))
    notif1.place(x=50,y=400)
    #-----------------------------Entry----------------------------------------------------------------------------------
    orderid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    orderid_entry.place(x=150,y=60)
    custid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    custid_entry.place(x=150,y=100)
    itemno_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    itemno_entry.place(x=150,y=140)
    dispatchdate_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    dispatchdate_entry.place(x=150,y=180)
    qty_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    qty_entry.place(x=150,y=220)
    #-----------------------------Button-----------------------------------------------------------
    insert=Button(t,text='Insert Record',height=2,width=15,command=insertdata,font=('Arial',10,'bold')).place(x=50,y=350)
    close=Button(t,text='Close File',height=2,width=15,command=closefile,font=('Arial',10,'bold')).place(x=200,y=350)
    search=Button(t,text='Check ID',height=1,width=10,font=('arial',10,'bold'),command=searchId).place(x=350,y=60)


    t.mainloop()
