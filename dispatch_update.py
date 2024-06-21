import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def disupdate():
        
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Dispatch Update')
    t.iconbitmap('ims.ico')
    t.config(bg='sky blue')
    t.resizable(0,0)
    lt=[]
    #----------------------------Function------------------------------------------------------
    def fillorderid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        sql="select orderid from dispatch"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()

    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(orderid_entry.get())
        xa=orderid_entry.get()
        xb=custid_entry.get()
        xc=itemno_entry.get()
        xd=dispatchdate_entry.get()
        xe=qty.get()
        sql="update bill set custid='%d',itemno='%d',dispatchdate='%s',qty='%d' where orderid=%d"%(xa,xb,xc,xd,xe,x) 
        cur.execute(sql)
        db.commit()
        orderid_entry.delete(0,100)
        custid_entry.delete(0,100)
        itemno_entry.delete(0,100)
        dispatchdate_entry.delete(0,100)
        qty_entry.delete(0,100)
        messagebox.showinfo('Hi','Record updated')



    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    orderid=Label(t,text='Order Id :-',font=('Arial',10,'bold')).place(x=10,y=60)
    custid=Label(t,text='Customer Id :-',font=('Arial',10,'bold')).place(x=10,y=100)
    itemno=Label(t,text='Item No :-',font=('Arial',10,'bold')).place(x=10,y=140)
    dispatchdate=Label(t,text='Dispatch Date :-',font=('Arial',10,'bold')).place(x=10,y=180)
    qty=Label(t,text='QTY :-',font=('Arial',10,'bold')).place(x=10,y=220)

    #-----------------------------Entry----------------------------------------------------------------------------------
    orderid_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    orderid_entry.place(x=150,y=60)
    fillorderid()
    orderid_entry['values']=lt
    custid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    custid_entry.place(x=150,y=100)
    itemno_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    itemno_entry.place(x=150,y=140)
    dispatchdate_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    dispatchdate_entry.place(x=150,y=180)
    qty_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    qty_entry.place(x=150,y=220)
    #-----------------------------Button-----------------------------------------------------------
    update=Button(t,text='Update Record',height=2,width=15,font=('Arial',10,'bold'),command=updatedata).place(x=50,y=350)
    close=Button(t,text='Close File',height=2,width=10,font=('Arial',10,'bold'),command=closefile).place(x=250,y=350)


    t.mainloop()
