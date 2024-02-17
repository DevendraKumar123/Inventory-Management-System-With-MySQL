import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def iteminsert():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Company Dispatch')
    lt=[]
    #----------------------------Function------------------------------------------------------


    def insertdata():
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
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    itemsno=Label(t,text='Items No :-',font=('Arial',10,'bold')).place(x=10,y=60)
    itemname=Label(t,text='Items Name :-',font=('Arial',10,'bold')).place(x=10,y=100)
    price=Label(t,text='Price :-',font=('Arial',10,'bold')).place(x=10,y=140)
    qty=Label(t,text='QTY :-',font=('Arial',10,'bold')).place(x=10,y=180)

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
    insert=Button(t,text='Insert Record',height=2,width=10,command=insertdata).place(x=50,y=320)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=200,y=320)


    t.mainloop()
