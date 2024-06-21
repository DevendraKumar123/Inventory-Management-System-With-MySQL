import tkinter 
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry('500x600+605+0')
t.title('Company Show Data')
t.resizable(0,0)
t.iconbitmap('ims.ico')
t.config(bg='sky blue')
#------------------------function----------------------------------------------
aa=[]
ab=[]
ac=[]
ad=[]
ae=[]
af=[]
i=0
lt=[]
def fillempid():
    db=pymysql.connect(host='localhost',user='root',password='root',database='testdb')
    cur=db.cursor()
    sql="select empid,name,city,salary from employee"
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
    empid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    
    salary_entry.delete(0,100)

    empid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    salary_entry.insert(0,ad[i])
    

def nextdata():
    global i
    i=i+1
    empid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    salary_entry.delete(0,100)
    empid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    salary_entry.insert(0,ad[i])
def prevdata():
    global i
    i=i-1
    empid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    city_entry.delete(0,100)

    salary_entry.delete(0,100)
    empid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    salary_entry.insert(0,ad[i])
def lastdata():
    global i
    i=len(aa)-1
    empid_entry.delete(0,100)
    name_entry.delete(0,100)
    city_entry.delete(0,100)
    city_entry.delete(0,100)
    salary_entry.delete(0,100)
    empid_entry.insert(0,aa[i])
    name_entry.insert(0,ab[i])
    city_entry.insert(0,ac[i])
    salary_entry.insert(0,ad[i])

def closefile():
    t.destroy()
#---------Label--------------------------------------------------
ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',13,'bold')).place(x=0,y=0)
empid=Label(t,text='Company Id -',bg='sky blue',font=('Arial',13,'bold'))
empid.place(x=50,y=50)
name=Label(t,text='Name -',bg='sky blue',font=('Arial',13,'bold'))
name.place(x=50,y=100)
city=Label(t,text='City -:',bg='sky blue',font=('Arial',13,'bold'))
city.place(x=50,y=150)
salary=Label(t,text='salary Id -:',bg='sky blue',font=('Arial',13,'bold'))
salary.place(x=50,y=200)
#------------------------Entry-------------------------------------------------
empid_entry=Entry(t,width=25)
empid_entry.place(x=250,y=50)
name_entry=Entry(t,width=25)
name_entry.place(x=250,y=100)
city_entry=Entry(t,width=25)
city_entry.place(x=250,y=150)
salary_entry=Entry(t,width=25)
salary_entry.place(x=250,y=200)

#-----------------------Button----------------------------------------------
first=Button(t,text='First',height=2,width=10,command=firstdata).place(x=20,y=350)
next=Button(t,text='Next',height=2,width=10,command=nextdata).place(x=120,y=350)
last=Button(t,text='Last',height=2,width=10,command=lastdata).place(x=250,y=350)
previous=Button(t,text='Previous',height=2,width=10,command=prevdata).place(x=350,y=350)
close=Button(t,text='Close',height=2,width=10,command=closefile).place(x=200,y=430)
fillempid()
t.mainloop()


