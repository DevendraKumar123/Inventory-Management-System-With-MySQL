import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def custfind():
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Customers Find')
    t.iconbitmap('ims.ico')
    t.config(bg='sky blue')
    t.resizable(0,0)
    lt=[]
    #----------------------------Function------------------------------------------------------
    def fillcustid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()

    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(custid_entry.get())
        sql="select name,address,city,email,phoneno from customers where custid=%d"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        name_entry.delete(0,100)
        address_entry.delete(0,100)
        city_entry.delete(0,100)
        email_entry.delete(0,100)
        phoneno_entry.delete(0,100)
        name_entry.insert(1,data[0])
        address_entry.insert(1,data[1])
        city_entry.insert(1,data[2])
        email_entry.insert(1,data[3])
        phoneno_entry.insert(1,data[4])
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
    custid_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    custid_entry.place(x=150,y=60)
    fillcustid()
    custid_entry['values']=lt
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
    find=Button(t,text='Find Record',height=2,width=12,font=('Arial',10,'bold'),command=finddata).place(x=100,y=320)
    close=Button(t,text='Close File',height=2,width=12,font=('Arial',10,'bold'),command=closefile).place(x=300,y=320)


    t.mainloop()
