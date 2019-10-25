'''Simple Python Database Application using Oracle Database to Create , Insert , Update and View Remainders on the Current Day and View all Remainders.
   Remainder Button Displays all the Events on the Current Date(MM) Only(System Date).
   View All Button Displays all the Avaliable Remainders.
   Update works taking the 'NAME' Field into Consideration.
   NOTE : Running the program multiple times causes error because the 'Create Table' is executed multiple times.
          So COMMENT 'Create Table' line when running the program multiple times'''
from tkinter import *
import cx_Oracle
 
root = Tk()
root.geometry('600x600')
root.title("Registration Form")

day=StringVar()
month=StringVar()
name = StringVar()
event= StringVar()

#Function to Create and Insert Values into the Database
def database():
   day1=day.get()
   month1=month.get()
   name1=name.get()
   event1=event.get()
   conn = cx_Oracle.connect("system/saint12345@localhost/XE")
   cursor=conn.cursor()
   #cursor.execute('CREATE TABLE Details (day varchar(30) not null,month varchar(30) not null,name varchar(30) not null,event varchar(30) not null)')
   cursor.execute('INSERT INTO Details (day,month,name,event) VALUES(:1,:2,:3,:4)',(day1,month1,name1,event1))
   conn.commit()
   ll6.config(text="Remainder Added")

#Function to Update the Remainder. Field 'Name' is taken into consideration for the update condition as no primary key is used
def update():
   day1=day.get()
   month1=month.get()
   name1=name.get()
   event1=event.get()
   conn = cx_Oracle.connect("system/saint12345@localhost/XE")
   cursor=conn.cursor()
   cursor.execute('UPDATE Details SET day = :1,month=:2,event=:4 WHERE name = :3',(day1,month1,event1,name1))
   conn.commit()
   ll6.config(text="Remainder Updated")

#Fucntion that returns the events on the Current Date(Taken from system date)
def remind():
   import time
   conn = cx_Oracle.connect("system/saint12345@localhost/XE")
   cursor=conn.cursor()
   cursor.execute('SELECT day,month,name,event FROM Details ')
   today=time.strftime('%d')
   #print(today)
   x=cursor.fetchall();
   count=cursor.rowcount
   #print(count)
   e=""
   for i in range(0,count):
      if x[i][0]==today:
         e=e+'Name : '+str(x[i][2])+' -- '+'Event : '+str(x[i][3]+'\n')
   ll6.config(text="%s"%e,font=("bold", 10))
   conn.commit()

#Functions that returns all the available events in the Database   
def view():
   import time
   conn = cx_Oracle.connect("system/saint12345@localhost/XE")
   cursor=conn.cursor()
   cursor.execute('SELECT day,month,name,event FROM Details ')
   x=cursor.fetchall();
   count=cursor.rowcount
   e=""
   for i in range(0,count):
         e=e+'Date : '+str(x[i][0])+'/'+str(x[i][1])+' -- '+'Name :'+str(x[i][2])+' -- '+'Event : '+str(x[i][3]+'\n')
   ll6.config(text="%s"%e,font=("bold", 10))
   conn.commit()

l1 = Label(root, text="REMAINDER APP",width=20,font=("bold", 25))
l1.place(x=120,y=33)


l2= Label(root, text="Day",width=20,font=("bold", 10))
l2.place(x=80,y=130)
e1 = Entry(root,width=30,textvar=day)
e1.place(x=240,y=130)

l3 = Label(root, text="Month",width=20,font=("bold", 10))
l3.place(x=80,y=180)
e2 = Entry(root,width=30,textvar=month)
e2.place(x=240,y=180)

l4 = Label(root, text="Name",width=20,font=("bold", 10))
l4.place(x=80,y=230)
e3 = Entry(root,width=30,textvar=name)
e3.place(x=240,y=230)


l5 = Label(root, text="Event",width=20,font=("bold", 10))
l5.place(x=80,y=280)
e4 = Entry(root,width=30,textvar=event)
e4.place(x=240,y=280)

ll6 = Label(root,font=("bold", 10))
ll6.place(x=150,y=450)

b1=Button(root, text='Submit',width=15,bg='brown',fg='white',command=database)
b1.place(x=60,y=380)


b2=Button(root, text='Remainder',width=15,bg='brown',fg='white',command=remind)
b2.place(x=180,y=380)

b3=Button(root, text='Update',width=15,bg='brown',fg='white',command=update)
b3.place(x=300,y=380)

b4=Button(root, text='View All',width=15,bg='brown',fg='white',command=view)
b4.place(x=420,y=380)


root.mainloop()
