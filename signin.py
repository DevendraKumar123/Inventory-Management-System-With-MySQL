# ------------------------------Module--------------------------
from tkinter import *
from PIL import ImageTk
#-----------------------------Title Bar-----------------------
t=Tk()
t.geometry('990x660+50+50')
t.resizable(0,0)
t.title('Login Page')
#-------------------------Function---------------------------
def hide():
    openeye.config(file='closeye.png')
    password_Entry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password_Entry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if username_Entry.get()=='Enter Username':
        username_Entry.delete(0,END)

def pass_enter(event):
    if password_Entry.get()=='Enter Password':
        password_Entry.delete(0,END)

#---------------------------Backgraound Image----------------------------------
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(t,image=bgImage)
bgLabel.place(x=0,y=0)
#--------------------------User Login-----------------------------
heading=Label(t,text='USER LOGIN',font=('arial',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)
#---------------------------Entry--------------------------
username_Entry=Entry(t,width=25,font=('arial',10,'bold'),bd=0,fg='firebrick1')
username_Entry.place(x=580,y=200)
username_Entry.insert(0,'Enter Username')
username_Entry.bind('<FocusIn>',user_enter)

password_Entry=Entry(t,width=25,font=('arial',10,'bold'),bd=0,fg='firebrick1')
password_Entry.place(x=580,y=240)
password_Entry.insert(0,'Enter Password')
password_Entry.bind('<FocusIn>',pass_enter)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(t,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=235)

forget_button=Button(t,text='Forget Password',bd=0,bg='white',font=('arial',10,'bold'),activebackground='white',fg='firebrick1',activeforeground='firebrick1')
forget_button.place(x=720,y=265)

login_button=Button(t,text='Login',font=('Open Sans',15,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',bd=0,width=20)
login_button.place(x=578,y=320)

or_label=Label(t,text='-------------  OR  -------------',bg='white',font=('Open Sans',16),fg='firebrick1')
or_label.place(x=578,y=360)

signuplabel=Label(t,text='Don`t have a account?',font=('open sans',10,'bold'),fg='firebrick1',bg=
                  'white')
signuplabel.place(x=570,y=500)

newaccount_button=Button(t,text='Create new one',font=('Open Sans',10,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',bd=0)
newaccount_button.place(x=728,y=498)

#--------------------Icon---------------------------------
facebook_logo=PhotoImage(file='facebook.png')
fblabel=Label(t,image=facebook_logo,bg='white')
fblabel.place(x=630,y=400)

google_logo=PhotoImage(file='google.png')
googlelabel=Label(t,image=google_logo,bg='white')
googlelabel.place(x=680,y=400)

twitter_logo=PhotoImage(file='twitter.png')
twitterlabel=Label(t,image=twitter_logo,bg='white')
twitterlabel.place(x=730,y=400)



#-------------------------------line Drow------------------------------
frame1=Frame(t,width=250,height=2,bg='firebrick1').place(x=580,y=220)
frame2=Frame(t,width=250,height=2,bg='firebrick1').place(x=580,y=260)
t.mainloop()