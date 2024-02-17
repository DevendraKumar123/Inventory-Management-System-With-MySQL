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
af=[]
i=0
lt=[]
def fillcomid():
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
        af.append(res[5])
    db.close()
def firstdata():
    global i
    i=0
    comid_entry.delete(0,100)
    name_entry.delete(0,100)
    address_entry.delete(0,100)
    city_entry.delete(0,100)
    email_entry.delete(0,100)
    regno_entry.delete(0,100)

    comid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    address_entry.insert(0,ac[i])
    city_entry.insert(0,ad[i])
    email_entry.insert(0,ae[i])
    regno_entry.insert(0,af[i])

def nextdata():
    global i
    i=i+1
    comid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    address_entry.delete(0,100)
    regno_entry.delete(0,100)
    email_entry.delete(0,100)
    comid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    address_entry.insert(0,ac[i])
    city_entry.insert(0,ad[i])
    email_entry.insert(0,ae[i])
    regno_entry.insert(0,af[i])
def prevdata():
    global i
    i=i-1
    comid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    address_entry.delete(0,100)
    regno_entry.delete(0,100)
    email_entry.delete(0,100)
    comid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    address_entry.insert(0,ac[i])
    city_entry.insert(0,ad[i])
    email_entry.insert(0,ae[i])
    regno_entry.insert(0,af[i])
def lastdata():
    global i
    i=len(aa)-1
    comid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    address_entry.delete(0,100)
    regno_entry.delete(0,100)
    email_entry.delete(0,100)
    comid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    address_entry.insert(0,ac[i])
    city_entry.insert(0,ad[i])
    email_entry.insert(0,ae[i])
    regno_entry.insert(0,af[i])

def closefile():
    t.destroy()
#---------Label--------------------------------------------------
ims=Label(t,text='Invantory Management System',height=2,width=80,bg='yellow',font=('Arial',10,'bold')).place(x=0,y=0)
comid=Label(t,text='Company Id -')
comid.place(x=50,y=50)
name=Label(t,text='Name -')
name.place(x=50,y=100)
address=Label(t,text="Address -: ")
address.place(x=50,y=150)
city=Label(t,text='City -:')
city.place(x=50,y=200)
email=Label(t,text='Email Id -:')
email.place(x=50,y=250)
regno=Label(t,text='Registration No -:')
regno.place(x=50,y=300)
#------------------------Entry-------------------------------------------------
comid_entry=Entry(t,width=25)
comid_entry.place(x=250,y=50)
name_entry=Entry(t,width=25)
name_entry.place(x=250,y=100)
address_entry=Entry(t,width=25)
address_entry.place(x=250,y=150)
city_entry=Entry(t,width=25)
city_entry.place(x=250,y=200)
email_entry=Entry(t,width=25)
email_entry.place(x=250,y=250)
regno_entry=Entry(t,width=25)
regno_entry.place(x=250,y=300)
#-----------------------Button----------------------------------------------
first=Button(t,text='First',height=2,width=10,command=firstdata).place(x=20,y=350)
next=Button(t,text='Next',height=2,width=10,command=nextdata).place(x=120,y=350)
last=Button(t,text='Last',height=2,width=10,command=lastdata).place(x=250,y=350)
previous=Button(t,text='Previous',height=2,width=10,command=prevdata).place(x=350,y=350)
close=Button(t,text='Close',height=2,width=10,command=closefile).place(x=200,y=430)
fillcomid()
t.mainloop()


