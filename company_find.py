import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def cfind():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Company Find')
    lt=[]
#----------------------------Function------------------------------------------------------

    def fillcomid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        sql="select comid from company"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()

    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(comid_entry.get())
        sql="select name,address,city,email,regno from company where comid=%d"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        name_entry.delete(0,100)
        address_entry.delete(0,100)
        city_entry.delete(0,100)
        email_entry.delete(0,100)
        regno_entry.delete(0,100)
        name_entry.insert(1,data[0])
        address_entry.insert(1,data[1])
        city_entry.insert(1,data[2])
        email_entry.insert(1,data[3])
        regno_entry.insert(1,data[4])
        db.close()


    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    compid=Label(t,text='Company Id :-',font=('Arial',10,'bold')).place(x=10,y=60)
    name=Label(t,text='Name :-',font=('Arial',10,'bold')).place(x=10,y=100)
    address=Label(t,text='Address :-',font=('Arial',10,'bold')).place(x=10,y=140)
    city=Label(t,text='City :-',font=('Arial',10,'bold')).place(x=10,y=180)
    email=Label(t,text='Email Id :-',font=('Arial',10,'bold')).place(x=10,y=220)
    regno=Label(t,text='Reg No :-',font=('Arial',10,'bold')).place(x=10,y=260)

    #-----------------------------Entry----------------------------------------------------------------------------------
    comid_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    comid_entry.place(x=150,y=60)
    fillcomid()
    comid_entry['values']=lt
    name_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    name_entry.place(x=150,y=100)
    address_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    address_entry.place(x=150,y=140)
    city_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    city_entry.place(x=150,y=180)
    email_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    email_entry.place(x=150,y=220)
    regno_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    regno_entry.place(x=150,y=260)
    #-----------------------------Button-----------------------------------------------------------
    find=Button(t,text='Find Record',height=2,width=10,command=finddata).place(x=100,y=320)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=300,y=320)


    t.mainloop()
