import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def billdelete():
        
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Company Bill')
    lt=[]
    #----------------------------Function------------------------------------------------------
    def fillbillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        sql="select billid from bill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()

    def delbillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(billid_entry.get())
        sql="delete from bill where billid=%d"%(x)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Record Delete')
        db.close()

    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    billid=Label(t,text='Bill Id :-',font=('Arial',10,'bold')).place(x=10,y=60)

    #-----------------------------Entry----------------------------------------------------------------------------------
    billid_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    billid_entry.place(x=150,y=60)
    fillbillid()
    billid_entry['values']=lt
   
    #-----------------------------Button-----------------------------------------------------------
    delete=Button(t,text='Delete Record',height=2,width=10,command=delbillid).place(x=50,y=400)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=200,y=400)


    t.mainloop()
