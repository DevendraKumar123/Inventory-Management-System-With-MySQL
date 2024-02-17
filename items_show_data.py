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
i=0
lt=[]
def fillitemno():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur=db.cursor()
    sql="select itemsno,itemname,price,qty from items"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        aa.append(res[0])
        ab.append(res[1])
        ac.append(res[2])
        ad.append(res[3])

    db.close()
def firstdata():
    global i
    i=0
    itemsno_entry.delete(0,100)
    itemname_entry.delete(0,100)
    price_entry.delete(0,100)
    qty_entry.delete(0,100)
    

    itemsno_entry.insert(0,aa[i])
    itemname_entry.insert(0,ab[i])
    price_entry.insert(0,ac[i])
    qty_entry.insert(0,ad[i])

def nextdata():
    global i
    i=i+1
    itemsno_entry.delete(0,100)
    itemname_entry.delete(0,100)
    price_entry.delete(0,100)
    qty_entry.delete(0,100)
    

    itemsno_entry.insert(0,aa[i])
    itemname_entry.insert(0,ab[i])
    price_entry.insert(0,ac[i])
    qty_entry.insert(0,ad[i])
def prevdata():
    global i
    i=i-1
    itemsno_entry.delete(0,100)
    itemname_entry.delete(0,100)
    price_entry.delete(0,100)
    qty_entry.delete(0,100)
    

    itemsno_entry.insert(0,aa[i])
    itemname_entry.insert(0,ab[i])
    price_entry.insert(0,ac[i])
    qty_entry.insert(0,ad[i])
def lastdata():
    global i
    i=len(aa)-1
    itemsno_entry.delete(0,100)
    itemname_entry.delete(0,100)
    price_entry.delete(0,100)
    qty_entry.delete(0,100)
    

    itemsno_entry.insert(0,aa[i])
    itemname_entry.insert(0,ab[i])
    price_entry.insert(0,ac[i])
    qty_entry.insert(0,ad[i])

def closefile():
    t.destroy()
#---------Label--------------------------------------------------
ims=Label(t,text='Invantory Management System',height=2,width=80,bg='yellow',font=('Arial',10,'bold')).place(x=0,y=0)
itemsno=Label(t,text='Item No -')
itemsno.place(x=50,y=50)
itemname=Label(t,text='Item Name -')
itemname.place(x=50,y=100)
price=Label(t,text="Price -: ")
price.place(x=50,y=150)
qty=Label(t,text='QTY -:')
qty.place(x=50,y=200)

#------------------------Entry-------------------------------------------------
itemsno_entry=Entry(t,width=25)
itemsno_entry.place(x=250,y=50)
itemname_entry=Entry(t,width=25)
itemname_entry.place(x=250,y=100)
price_entry=Entry(t,width=25)
price_entry.place(x=250,y=150)
qty_entry=Entry(t,width=25)
qty_entry.place(x=250,y=200)

#-----------------------Button----------------------------------------------
first=Button(t,text='First',height=2,width=10,command=firstdata).place(x=20,y=350)
next=Button(t,text='Next',height=2,width=10,command=nextdata).place(x=120,y=350)
last=Button(t,text='Last',height=2,width=10,command=lastdata).place(x=250,y=350)
previous=Button(t,text='Previous',height=2,width=10,command=prevdata).place(x=350,y=350)
close=Button(t,text='Close',height=2,width=10,command=closefile).place(x=200,y=430)

fillitemno()
t.mainloop()


