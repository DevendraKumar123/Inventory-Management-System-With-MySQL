import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def cdelete():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.title('Company Delete')
    t.config(bg='sky blue')
    t.iconbitmap('ims.ico')
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


    def delcomid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(comid_entry.get())
        sql="delete from company where comid=%d"%(x)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Record Delete')
        db.close()

    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    compid=Label(t,text='Company Id :-',font=('Arial',10,'bold')).place(x=10,y=60)
    

    #-----------------------------Entry----------------------------------------------------------------------------------
    comid_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    comid_entry.place(x=150,y=60)
    fillcomid()
    comid_entry['values']=lt

    #-----------------------------Button-----------------------------------------------------------
    delete=Button(t,text='Delete Record',height=2,width=10,command=delcomid).place(x=50,y=400)
    close=Button(t,text='Close File',height=2,width=10,command=closefile).place(x=200,y=400)


    t.mainloop()
