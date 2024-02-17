import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def itemupdate():
        
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Company Dispatch')
    lt=[]
    #----------------------------Function------------------------------------------------------
    def fillitemsno():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        sql="select itemsno from items"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()

    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(itemsno_entry.get())
        xa=itemsno_entry.get()
        xb=itemname_entry.get()
        xc=price_entry.get()
        xd=qty.get()
        sql="update items set itemname='%s',price='%d',qty='%d' where itemsno=%d"%(xa,xb,xc,xd,x) 
        cur.execute(sql)
        db.commit()
        itemsno_entry.delete(0,100)
        itemname_entry.delete(0,100)
        price_entry.delete(0,100)
        qty_entry.delete(0,100)
        messagebox.showinfo('Hi','Record updated')


    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    itemsno=Label(t,text='Items No :-',font=('Arial',10,'bold')).place(x=10,y=60)
    itemname=Label(t,text='Items Name :-',font=('Arial',10,'bold')).place(x=10,y=100)
    price=Label(t,text='Price :-',font=('Arial',10,'bold')).place(x=10,y=140)
    qty=Label(t,text='QTY :-',font=('Arial',10,'bold')).place(x=10,y=180)

    #-----------------------------Entry----------------------------------------------------------------------------------
    itemsno_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    itemsno_entry.place(x=150,y=60)
    fillitemsno()
    itemsno_entry['values']=lt
    itemname_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    itemname_entry.place(x=150,y=100)
    price_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    price_entry.place(x=150,y=140)
    qty_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    qty_entry.place(x=150,y=180)
    #-----------------------------Button-----------------------------------------------------------
    update=Button(t,text='Update Record',height=2,width=15,command=updatedata).place(x=50,y=320)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=200,y=320)


    t.mainloop()
