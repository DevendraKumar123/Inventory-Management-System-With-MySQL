import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def itemdelete():
        
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Item Delete')
    t.iconbitmap('ims.ico')
    t.config(bg='sky blue')
    t.resizable(0,0)
    lt=[]
    #----------------------------Function------------------------------------------------------
    def fillitemsno():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        sql="select itemsno from items"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()


    def delitemsid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur=db.cursor()
        x=int(itemsno_entry.get())
        sql="delete from items where itemsno=%d"%(x)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Record Delete')
        db.close()

    def closefile():
        t.destroy()
    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    itemsno=Label(t,text='Items No :-',font=('Arial',10,'bold')).place(x=10,y=60)

    #-----------------------------Entry----------------------------------------------------------------------------------
    itemsno_entry=ttk.Combobox(t,width=25,font=('Arial',10,'bold'))
    itemsno_entry.place(x=150,y=60)
    fillitemsno()
    itemsno_entry['values']=lt
   
    #-----------------------------Button-----------------------------------------------------------
    delete=Button(t,text='Delete Record',height=2,width=15,font=('Arial',10,'bold'),command=delitemsid).place(x=50,y=400)
    close=Button(t,text='Close File',height=2,width=15,font=('Arial',10,'bold'),command=closefile).place(x=200,y=400)


    t.mainloop()
