import tkinter 
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry('500x600')
t.title('Customers Show Data')
#------------------------function----------------------------------------------
aa=[]
ab=[]
ac=[]
ad=[]
ae=[]
af=[]
i=0
lt=[]
def fillcustid():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur=db.cursor()
    sql="select custid,name,city,address,phoneno,email from customers"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        aa.append(res[0])
        ab.append(res[1])
        ac.append(res[2])
        ad.append(res[3])
        ae.append(res[4])
        af.append(res[5])
    db.close()

def firstdata():
    global i
    i=0
    custid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    address_entry.delete(0,100)
    phoneno_entry.delete(0,100)
    email_entry.delete(0,100)
    
    custid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    address_entry.insert(0,ad[i])
    phoneno_entry.insert(0,ae[i])
    email_entry.insert(0,af[i])
    

def nextdata():
    global i
    i=i+1
    custid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    address_entry.delete(0,100)
    phoneno_entry.delete(0,100)
    email_entry.delete(0,100)
    
    custid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    address_entry.insert(0,ad[i])
    phoneno_entry.insert(0,ae[i])
    email_entry.insert(0,af[i])

def prevdata():
    global i
    i=i-1
    custid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    address_entry.delete(0,100)
    phoneno_entry.delete(0,100)
    email_entry.delete(0,100)
    
    custid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    address_entry.insert(0,ad[i])
    phoneno_entry.insert(0,ae[i])
    email_entry.insert(0,af[i])

def lastdata():
    global i
    i=len(aa)-1
    custid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    address_entry.delete(0,100)
    phoneno_entry.delete(0,100)
    email_entry.delete(0,100)
    
    custid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    address_entry.insert(0,ad[i])
    phoneno_entry.insert(0,ae[i])
    email_entry.insert(0,af[i])
    

def closefile():
    t.destroy()
#---------Label--------------------------------------------------
ims=Label(t,text='Invantory Management System',height=2,width=80,bg='yellow',font=('Arial',10,'bold')).place(x=0,y=0)
custid=Label(t,text='Company Id -')
custid.place(x=50,y=50)
name=Label(t,text='Name -')
name.place(x=50,y=100)
city=Label(t,text='City -:')
city.place(x=50,y=150)
address=Label(t,text="Address -: ")
address.place(x=50,y=200)
phoneno=Label(t,text='Phone No -:')
phoneno.place(x=50,y=250)
email=Label(t,text='Email Id -:')
email.place(x=50,y=300)

#------------------------Entry-------------------------------------------------
custid_entry=Entry(t,width=25)
custid_entry.place(x=250,y=50)
name_entry=Entry(t,width=25)
name_entry.place(x=250,y=100)
city_entry=Entry(t,width=25)
city_entry.place(x=250,y=150)
address_entry=Entry(t,width=25)
address_entry.place(x=250,y=200)
phoneno_entry=Entry(t,width=25)
phoneno_entry.place(x=250,y=250)
email_entry=Entry(t,width=25)
email_entry.place(x=250,y=300)

#-----------------------Button----------------------------------------------
first=Button(t,text='First',height=2,width=10,command=firstdata).place(x=20,y=350)
next=Button(t,text='Next',height=2,width=10,command=nextdata).place(x=120,y=350)
last=Button(t,text='Last',height=2,width=10,command=lastdata).place(x=250,y=350)
previous=Button(t,text='Previous',height=2,width=10,command=prevdata).place(x=350,y=350)
close=Button(t,text='Close',height=2,width=10,command=closefile).place(x=200,y=430)

fillcustid()
t.mainloop()


