import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def custupdate():
        
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Customers Update')
    t.iconbitmap('ims.ico')
    t.config(bg='sky blue')
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


    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(custid_entry.get())
        xa=name_entry.get()
        xb=address_entry.get()
        xc=city_entry.get()
        xd=email_entry.get()
        xe=phoneno_entry.get()
        sql="update customers set name='%s',address='%s',city='%s',email='%s',phoneno='%s' where custid=%d"%(xa,xb,xc,xd,xe,x) 
        cur.execute(sql)
        db.commit()
        name_entry.delete(0,100)
        address_entry.delete(0,100)
        city_entry.delete(0,100)
        email_entry.delete(0,100)
        phoneno_entry.delete(0,100)
        messagebox.showinfo('Hi','Record updated')


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
    update=Button(t,text='Update Record',height=2,width=15,command=updatedata).place(x=50,y=320)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=200,y=320)


    t.mainloop()
