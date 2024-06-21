import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def orderfind():
        
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Orders Find')
    t.iconbitmap('ims.ico')
    t.config(bg='sky blue')
    t.resizable(0,0)
    lt=[]
    #----------------------------Function------------------------------------------------------
    def fillorderid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()



    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(orderid_entry.get())
        sql="select custid,itemno,dateoforder,qty from orders where orderid=%d"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        orderid_entry.delete(0,100)
        custid_entry.delete(0,100)
        itemno_entry.delete(0,100)
        dateoforder_entry.delete(0,100)
        qty_entry.delete(0,100)
        custid_entry.insert(1,data[0])
        itemno_entry.insert(1,data[1])
        dateoforder_entry.insert(1,data[2])
        qty_entry.insert(1,data[3])
        db.close()


    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    orderid=Label(t,text='Order Id :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=60)
    custid=Label(t,text='Customer Id :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=100)
    itemno=Label(t,text='Item No :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=140)
    dateoforder=Label(t,text='Date of Order :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=180)
    qty=Label(t,text='QTY :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=220)

    #-----------------------------Entry----------------------------------------------------------------------------------
    orderid_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    orderid_entry.place(x=150,y=60)
    fillorderid()
    orderid_entry['values']=lt
    custid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    custid_entry.place(x=150,y=100)
    itemno_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    itemno_entry.place(x=150,y=140)
    dateoforder_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    dateoforder_entry.place(x=150,y=180)
    qty_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    qty_entry.place(x=150,y=220)
    #-----------------------------Button-----------------------------------------------------------
    find=Button(t,text='Find Record',height=2,width=10,font=('Arial',10,'bold'),command=finddata).place(x=300,y=400)
    close=Button(t,text='Close File',height=2,width=10,font=('Arial',10,'bold'),command=closefile).place(x=200,y=400)


    t.mainloop()
