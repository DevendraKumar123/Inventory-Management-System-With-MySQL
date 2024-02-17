import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
from company_update import*
from company_insert import*
from company_find import *
from company_delete import*
from customers_update import*
from customers_insert import*
from customers_find import *
from customers_delete import*
from bill_update import*
from bill_insert import*
from bill_find import *
from bill_delete import*
from dispatch_update import*
from dispatch_insert import*
from dispatch_find import *
from dispatch_delete import*
from orders_update import*
from orders_insert import*
from orders_find import *
from orders_delete import*
from items_update import*
from items_insert import*
from items_find import *
from items_delete import*



t=tkinter.Tk()
t.geometry('600x800')
t.iconbitmap('ims.ico')
t.title('Dash Board Inventory Management System')


#----------------------------------------Label--------------------------------------
company=Label(t,text='Comapny',height=2,width=100,bg='yellow',font=('arial',10,'bold')).place(x=-100,y=0)
customer=Label(t,text='Customers',height=2,width=100,bg='yellow',font=('arial',10,'bold')).place(x=-100,y=100)
bill=Label(t,text='Bill',height=2,width=100,bg='yellow',font=('arial',10,'bold')).place(x=-100,y=200)
dispatch=Label(t,text='Dispatch',height=2,width=100,bg='yellow',font=('arial',10,'bold')).place(x=-100,y=300)
items=Label(t,text='Items',height=2,width=100,bg='yellow',font=('arial',10,'bold')).place(x=-100,y=400)
order=Label(t,text='Orders',height=2,width=100,bg='yellow',font=('arial',10,'bold')).place(x=-100,y=500)

#----------------------------------------Company Button-----------------------------
c_insert=Button(t,text='Insert',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=cinsert)
c_insert.place(x=50,y=50)
c_update=Button(t,text='Update',command=cupdate,height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'))
c_update.place(x=180,y=50)
c_find=Button(t,text='Find',command=cfind,height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'))
c_find.place(x=310,y=50)
c_delete=Button(t,text='Delete',command=cdelete,height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'))
c_delete.place(x=440,y=50)
#-------------------------------Customers----------------------------------------
cust_insert=Button(t,text='Insert',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=custinsert)
cust_insert.place(x=50,y=150)
cust_update=Button(t,text='Update',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=custupdate)
cust_update.place(x=180,y=150)
cust_find=Button(t,text='Find',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=custfind)
cust_find.place(x=310,y=150)
cust_delete=Button(t,text='Delete',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=custdelete)
cust_delete.place(x=440,y=150)
#------------------------------------bill----------------------------------------
bill_insert=Button(t,text='Insert',height=2,width=10,activeforeground='red',bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=billinsert)
bill_insert.place(x=50,y=250)
bill_update=Button(t,text='Update',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=billupdate)
bill_update.place(x=180,y=250)
bill_find=Button(t,text='Find',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=billfind)
bill_find.place(x=310,y=250)
bill_delete=Button(t,text='Delete',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=billdelete)
bill_delete.place(x=440,y=250)
#---------------------------------dispatch--------------------------------------
dispatch_insert=Button(t,text='Insert',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=disinsert)
dispatch_insert.place(x=50,y=350)
dispatch_update=Button(t,text='Update',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=disupdate)
dispatch_update.place(x=180,y=350)
dispatch_find=Button(t,text='Find',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=disfind)
dispatch_find.place(x=310,y=350)
dispatch_delete=Button(t,text='Delete',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=disdelete)
dispatch_delete.place(x=440,y=350)
#---------------------------------item------------------------------------------
items_insert=Button(t,text='Insert',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=iteminsert)
items_insert.place(x=50,y=450)
items_update=Button(t,text='Update',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=itemupdate)
items_update.place(x=180,y=450)
items_find=Button(t,text='Find',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=itemfind)
items_find.place(x=310,y=450)
items_delete=Button(t,text='Delete',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=itemdelete)
items_delete.place(x=440,y=450)
#----------------------------------orders------------------------------------
order_insert=Button(t,text='Insert',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=orderinsert)
order_insert.place(x=50,y=550)
order_update=Button(t,text='Update',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=orderupdate)
order_update.place(x=180,y=550)
order_find=Button(t,text='Find',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=itemfind)
order_find.place(x=310,y=550)
order_delete=Button(t,text='Delete',height=2,width=10,bg='white',activebackground='sky blue',font=('arial',10,'bold'),command=orderdelete)
order_delete.place(x=440,y=550)
#--------------------------------------Entry-----------------------------------

t.mainloop()