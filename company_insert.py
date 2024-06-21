import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def cinsert():
    t=tkinter.Tk()
    t.geometry('500x500+605+0')
    t.title('Company Insert')
    t.config(bg='sky blue')
    t.iconbitmap('img/ims.ico')
    # t.minsize(500,500)
    # t.maxsize(500,500)
    t.resizable(0,0)
    lt=[]
#----------------------------Function------------------------------------------------------

    def insertdata():
        if len(comid_entry.get())==0 or len(name_entry.get())==0  or len(address_entry.get())==0 or len(city_entry.get())==0  or len(email_entry.get())==0 or len(regno_entry.get())==0:
            # messagebox.showerror("Company","Pls fill all data")
            notif1.config(text='Plz fill all data..')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur=db.cursor()
            xa=int(comid_entry.get())
            xb=name_entry.get()
            xc=address_entry.get()
            xd=city_entry.get()
            xe=email_entry.get()
            xf=regno_entry.get()
            sql="insert into company values(%d,'%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Hi','Saved Record')
            name_entry.delete(0,100)
            address_entry.delete(0,100)
            city_entry.delete(0,100)
            email_entry.delete(0,100)
            regno_entry.delete(0,100)
            db.close()




    def closefile():
        t.destroy()

    def searchId():
        if len(comid_entry.get())==0:
            notif.config(text="Plz fill Company Id..")
            # messagebox.showerror("Company Insert','plz fill id..")
        else:
            x=int(comid_entry.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur=db.cursor()
            sql="select count(*) from company where comid=%d"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                notif.config(text='Pls go Ahead...')
                # messagebox.showerror('hi','Already Exists...')
            else:
                notif.config(text='Already Exists..')
                # messagebox.showinfo('hi','Pls go Ahead...')
            db.close()



    #-----------------------------Label----------------------------------------------------------------------------------
    ims=Label(t,text='Invantory Management System',height=2,width=50,bg='yellow',font=('Arial',15,'bold')).place(x=0,y=0)
    compid=Label(t,text='Company Id :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=60)
    name=Label(t,text='Name :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=100)
    address=Label(t,text='Address :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=140)
    city=Label(t,text='City :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=180)
    email=Label(t,text='Email Id :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=220)
    regno=Label(t,text='Reg No :-',font=('Arial',10,'bold'),bg='sky blue').place(x=10,y=260)

    notif=Label(t,fg='red',bg='sky blue',font=('arial',10,'bold'))
    notif.place(x=350,y=90)
    notif1=Label(t,fg='red',bg='sky blue',font=('arial',10,'bold'))
    notif1.place(x=50,y=400)

    #-----------------------------Entry----------------------------------------------------------------------------------
    comid_entry=Entry(t,width=25,font=('Arial',10,'bold'))
    comid_entry.place(x=150,y=60)
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
    insert=Button(t,text='Insert Record',height=2,width=15,font=('Arial',10,'bold'),command=insertdata).place(x=50,y=350)
    close=Button(t,text='Close File',height=2,width=15,font=('Arial',10,'bold'),command=closefile).place(x=200,y=350)
    search=Button(t,text='Check ID',height=1,width=10,font=('arial',10,'bold'),command=searchId).place(x=350,y=60)


    t.mainloop()
