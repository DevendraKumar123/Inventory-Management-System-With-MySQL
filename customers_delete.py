import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def custdelete():
        
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Customers Delete')
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



    def delcomid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(custid_entry.get())
        sql="delete from customers where custid=%d"%(x)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Record Delete')
        db.close()

    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    custid=Label(t,text='Customer Id :-',font=('Arial',10,'bold')).place(x=10,y=60)
    

    #-----------------------------Entry----------------------------------------------------------------------------------
    custid_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    custid_entry.place(x=150,y=60)
    fillcustid()
    custid_entry['values']=lt
   
    #-----------------------------Button-----------------------------------------------------------
    delete=Button(t,text='Delete Record',height=2,width=15,font=('Arial',10,'bold'),command=delcomid).place(x=50,y=400)
    close=Button(t,text='Close File',height=2,width=15,font=('Arial',10,'bold'),command=closefile).place(x=200,y=400)


    t.mainloop()
