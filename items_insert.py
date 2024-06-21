import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def iteminsert():
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Item Insert')
    t.iconbitmap('ims.ico')
    t.config(bg='sky blue')
    t.resizable(0,0)
    lt=[]
    #----------------------------Function------------------------------------------------------


    def insertdata():
        if len(itemsno_entry.get())==0 or len(itemname_entry.get())==0 or len(price_entry.get())==0 or len(qty_entry.get())==0:
            # messagebox.showerror('Item','Please Fill all data')
            notif1.config(text='Plz fill all Data..')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur=db.cursor()
            x=int(itemsno_entry.get())
            xa=itemsno_entry.get()
            xb=itemname_entry.get()
            xc=price_entry.get()
            xd=qty.get()
            sql="insert into items values(%d,'%d','%d','%s','%d')"%(x,xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Hi','Saved Record')
            itemname_entry.delete(0,100)
            price_entry.delete(0,100)
            qty_entry.delete(0,100)
            db.close()
        
    def closefile():
        t.destroy()

    def searchId():
        if len(itemsno_entry.get())==0:
            notif.config(text='Plz fill Item No..')
        else:
            x=int(itemsno_entry.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur=db.cursor()
            sql="select count(*) from items where itemsno=%d"%(x)
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
    itemsno=Label(t,text='Items No :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=60)
    itemname=Label(t,text='Items Name :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=100)
    price=Label(t,text='Price :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=140)
    qty=Label(t,text='QTY :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=180)

    notif=Label(t,fg='red',bg='sky blue',font=('arial',10,'bold'))
    notif.place(x=350,y=90)
    notif1=Label(t,fg='red',bg='sky blue',font=('arial',10,'bold'))
    notif1.place(x=50,y=400)
    #-----------------------------Entry----------------------------------------------------------------------------------
    itemsno_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    itemsno_entry.place(x=150,y=60)
    itemname_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    itemname_entry.place(x=150,y=100)
    price_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    price_entry.place(x=150,y=140)
    qty_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    qty_entry.place(x=150,y=180)
    #-----------------------------Button-----------------------------------------------------------
    insert=Button(t,text='Insert Record',height=2,width=15,font=('Arial',10,'bold'),command=insertdata).place(x=50,y=350)
    close=Button(t,text='Close File',height=2,width=15,font=('Arial',10,'bold'),command=closefile).place(x=200,y=350)
    search=Button(t,text='Check ID',height=1,width=10,font=('arial',10,'bold'),command=searchId).place(x=350,y=60)


    t.mainloop()
