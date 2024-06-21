import tkinter 
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry('500x600')
t.title('Company Show Data')
#------------------------function----------------------------------------------
aa=[]
ab=[]
ac=[]
ad=[]
ae=[]
i=0
lt=[]
def fillorderid():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur=db.cursor()
    sql="select comid,name,address,city,email,regno from company"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        aa.append(res[0])
        ab.append(res[1])
        ac.append(res[2])
        ad.append(res[3])
        ae.append(res[4])
    db.close()

def firstdata():
    global i
    i=0
    orderid_entry.delete(0,100)
    custid_entry.delete(0,100)
    itemno_entry.delete(0,100)
    dispatchdate_entry.delete(0,100)
    qty_entry.delete(0,100)

    orderid_entry.insert(0,aa[i])
    custid_entry.insert(0,ab[i])
    itemno_entry.insert(0,ac[i])
    dispatchdate_entry.insert(0,ad[i])
    qty_entry.insert(0,ae[i])

def nextdata():
    global i
    i=i+1
    orderid_entry.delete(0,100)
    custid_entry.delete(0,100)
    itemno_entry.delete(0,100)
    dispatchdate_entry.delete(0,100)
    qty_entry.delete(0,100)

    orderid_entry.insert(0,aa[i])
    custid_entry.insert(0,ab[i])
    itemno_entry.insert(0,ac[i])
    dispatchdate_entry.insert(0,ad[i])
    qty_entry.insert(0,ae[i])

def prevdata():
    global i
    i=i-1
    orderid_entry.delete(0,100)
    custid_entry.delete(0,100)
    itemno_entry.delete(0,100)
    dispatchdate_entry.delete(0,100)
    qty_entry.delete(0,100)

    orderid_entry.insert(0,aa[i])
    custid_entry.insert(0,ab[i])
    itemno_entry.insert(0,ac[i])
    dispatchdate_entry.insert(0,ad[i])
    qty_entry.insert(0,ae[i])

def lastdata():
    global i
    i=len(aa)-1
    orderid_entry.delete(0,100)
    custid_entry.delete(0,100)
    itemno_entry.delete(0,100)
    dispatchdate_entry.delete(0,100)
    qty_entry.delete(0,100)

    orderid_entry.insert(0,aa[i])
    custid_entry.insert(0,ab[i])
    itemno_entry.insert(0,ac[i])
    dispatchdate_entry.insert(0,ad[i])
    qty_entry.insert(0,ae[i])

def closefile():
    t.destroy()
#---------Label--------------------------------------------------
ims=Label(t,text='Invantory Management System',height=2,width=80,bg='yellow',font=('Arial',10,'bold')).place(x=0,y=0)
orderid=Label(t,text='Order Id -')
orderid.place(x=50,y=50)
custid=Label(t,text='Customer Id -')
custid.place(x=50,y=100)
itemno=Label(t,text="Item No -: ")
itemno.place(x=50,y=150)
dispatchdate=Label(t,text='Dispatch Date -:')
dispatchdate.place(x=50,y=200)
qty=Label(t,text='QTY -:')
qty.place(x=50,y=250)
#------------------------Entry-------------------------------------------------
orderid_entry=Entry(t,width=25)
orderid_entry.place(x=250,y=50)
custid_entry=Entry(t,width=25)
custid_entry.place(x=250,y=100)
itemno_entry=Entry(t,width=25)
itemno_entry.place(x=250,y=150)
dispatchdate_entry=Entry(t,width=25)
dispatchdate_entry.place(x=250,y=200)
qty_entry=Entry(t,width=25)
qty_entry.place(x=250,y=250)
#-----------------------Button----------------------------------------------
first=Button(t,text='First',height=2,width=10,command=firstdata).place(x=20,y=350)
next=Button(t,text='Next',height=2,width=10,command=nextdata).place(x=120,y=350)
last=Button(t,text='Last',height=2,width=10,command=lastdata).place(x=250,y=350)
previous=Button(t,text='Previous',height=2,width=10,command=prevdata).place(x=350,y=350)
close=Button(t,text='Close',height=2,width=10,command=closefile).place(x=200,y=430)

fillorderid()
t.mainloop()


