from tkcalendar import Calendar, DateEntry
from tkinter import *
from tkinter import messagebox
import os
'''try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk'''
import re

  
top = Tk()  
top.title("LETTER GENERATOR")
top.geometry("600x600+0+0")

myFont = ('Helvetica',20,'bold')

canvas = Canvas(width=1366, height=768)
canvas.place(x=0,y=0)
photo = PhotoImage(file='newkeyboard3.png')
canvas.create_image(0,0,anchor=NW,image=photo)

class Queala:
     def __init__(root):
          root=Tk()
          root.title("Annual leave application")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')

          def print_sel1():
               fp=open('Annualleaveapplication.txt','r+')
               data=fp.read()
               
               A_name=e2.get()
               regex11=re.compile('\d')
               match11=re.findall(regex11,A_name)
               regex12=re.compile('\w+')
               match12=re.findall(regex12,A_name)
               if len(match11)>0:
                         messagebox.showerror("error","Enter alphabates only in Applicant name")
               elif len(match12)<=0:
                         messagebox.showerror("error","Enter the applicant name")
               else:
                         data=data.replace("$name",A_name)

               Auth_gen=v.get()
               if Auth_gen==0:
                    data=data.replace("$auth_gen","Mr.")
               else:
                    data=data.replace("$auth_gen","Mrs./Ms.")
               
               Auth_name=e1.get()
               regex31=re.compile('\d')
               match31=re.findall(regex31,Auth_name)
               regex32=re.compile('\w+')
               match32=re.findall(regex32,Auth_name)
               if len(match31)>0:
                         messagebox.showerror("error","Enter alphabates only in authority name")
               elif len(match32)<=0:
                         messagebox.showerror("error","Enter the authority")
               else:
                         data=data.replace("$auth_name",Auth_name)

               D_leave=e3.get()
               regex21=re.compile('\D')
               match21=re.findall(regex21,D_leave)
               regex22=re.compile('\d')
               match22=re.findall(regex22,D_leave)
               if len(match21)>0:
                         messagebox.showerror("error","Enter numbers only no. of leave days")
               elif len(match22)<=0:
                         messagebox.showerror("error","Enter the no. of days")
               else:
                         data=data.replace("$period",D_leave)
               
               reason=e4.get()
               regex41=re.compile('\d')
               match41=re.findall(regex41,reason)
               regex42=re.compile('\w+')
               match42=re.findall(regex42,reason)
               if len(match41)>0:
                         messagebox.showerror("error","Enter alphabates only in reason")
               elif len(match42)<=0:
                         messagebox.showerror("error","Enter the reason")
               else:
                         data=data.replace("$reason",reason)
               P_gen=v.get()
               if P_gen==0:
                    data=data.replace("$p'sgen","Mr.")
               else:
                    data=data.replace("$p'sgen","Mrs./Ms.")
               P_name=e7.get()
               regex71=re.compile('\d')
               match71=re.findall(regex71,P_name)
               regex72=re.compile('\w+')
               match72=re.findall(regex72,P_name)
               if len(match71)>0:
                         messagebox.showerror("error","Enter alphabates only in person's name")
               elif len(match72)<=0:
                         messagebox.showerror("error","Enter the person's name")
               else:
                         data=data.replace("$p'sname",P_name)

               Mail=e8.get()
               match81=re.search("@",Mail)
               if (match81):
                         data=data.replace("$email",Mail)
               else:
                         messagebox.showerror("error","Enter the valid email")

               Mob=e9.get()
               regex91=re.compile('\D')
               match91=re.findall(regex91,Mob)
               regex92=re.compile('\d')
               match92=re.findall(regex92,Mob)
               if len(match91)>0:
                         messagebox.showerror("error","Enter numbers only in contact no.")
               elif len(match92)<=0:
                         messagebox.showerror("error","Enter the contact no.")
               elif len(match92)<10 or len(match92)>10:
                         messagebox.showerror("error","no. must be 10 digits only")
               else:
                         data=data.replace("$contact",Mob)
               
               S_date=str(startdate.selection_get())
               E_date=str(enddate.selection_get())
               R_date=str(Rejoining.selection_get())
               if (S_date>E_date)or(E_date>R_date)or((S_date)==(E_date)==(R_date)=='None'):
                         messagebox.showerror("error",'enter valid dates')
               else:
                         data=data.replace("$s_date",S_date)
                         data=data.replace("$e_date",E_date)
                         data=data.replace("$r_date",R_date)
                              
               count=data.count("$")
               if count==0:
                    
                    f=open('Annualleave.txt','w+')
                    f.write(data)
              
                    messagebox.showinfo("Letter saved","Letter saved as:Annualleave")
               
#applicant's name
          
          
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          
#gender of authority          
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar() 
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)

          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          
#no. of days to apply for leave          
          Label(root, text='No. of Days for leave:',font=myFont).place(x=100,y=200)
          e3 = Entry(root,font=myFont) 
          e3.place(x=350,y=200)
          
#reason
          Label(root, text='Reason:',font=myFont).place(x=100,y=250)
          e4 = Entry(root,font=myFont) 
          e4.place(x=350,y=250,width=750)

#person's gender
          Label(root, text='Person whome you delegated current project:',font=myFont).place(x=100,y=300)
          v = IntVar() 
          Radiobutton(root, text='Mr.', variable=v, value=1,font=myFont).place(x=650,y=300) 
          Radiobutton(root, text='Mrs./Ms.', variable=v, value=2,font=myFont).place(x=700,y=300)

          e7 = Entry(root,font=myFont) 
          e7.place(x=880,y=300)
          
#Email and mobile detail
          Label(root, text="Applicant's email:",font=myFont).place(x=100,y=350)
          e8 = Entry(root,font=myFont) 
          e8.place(x=350,y=350)
          Label(root, text="Applicant's phone no.:",font=myFont).place(x=650,y=350)
          e9 = Entry(root,font=myFont)
          e9.place(x=880,y=350)
          
#start date
          Label(root, text='Leave starts from:',font=myFont).place(x=100,y=400)
          startdate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          startdate.place(x=100,y=450)
          
#end date
          Label(root, text='Leave ends on:',font=myFont).place(x=500,y=400)
          enddate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          enddate.place(x=500,y=450)
         
#Rejoining date
          Label(root, text='Rejoining date:',font=myFont).place(x=900,y=400)
                  
          Rejoining = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          Rejoining.place(x=900,y=450)
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont, command=print_sel1)
          
          letter_button.place(x=900,y=650)
          
          root.mainloop()
          
class Quecla:
          def __init__(root):
               root=Tk()
               root.title("Casual leave application")
               root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
               myFont = ('Helvetica',15,'bold')
               def print_sel1():
                    fp=open('Casualleaveapplication.txt','r+')
                    data=fp.read()
                    
                    A_name=e2.get()
                    regex11=re.compile('\d')
                    match11=re.findall(regex11,A_name)
                    regex12=re.compile('\w+')
                    match12=re.findall(regex12,A_name)
                    if len(match11)>0:
                              messagebox.showerror("error","Enter alphabates only in applicant name")
                    elif len(match12)<=0:
                              messagebox.showerror("error","Enter the applicant name")
                    else:
                              data=data.replace("$name",A_name)

                    Auth_gen=v.get()
                    if Auth_gen==0:
                         data=data.replace("$auth_gen","Mr.")
                    else:
                         data=data.replace("$auth_gen","Mrs./Ms.")
                    
                    Auth_name=e1.get()
                    regex31=re.compile('\d')
                    match31=re.findall(regex31,Auth_name)
                    regex32=re.compile('\w+')
                    match32=re.findall(regex32,Auth_name)
                    if len(match31)>0:
                              messagebox.showerror("error","Enter alphabates only in authority name")
                    elif len(match32)<=0:
                              messagebox.showerror("error","Enter the authority name")
                    else:
                              data=data.replace("$auth_name",Auth_name)

                    D_leave=e3.get()
                    regex21=re.compile('\D')
                    match21=re.findall(regex21,D_leave)
                    regex22=re.compile('\d')
                    match22=re.findall(regex22,D_leave)
                    if len(match21)>0:
                              messagebox.showerror("error","Enter numbers only in no. of days")
                    elif len(match22)<=0:
                              messagebox.showerror("error","Enter the no. of days")
                    else:
                              data=data.replace("$period",D_leave)
                    Des=e8.get()
                    regex81=re.compile('\d')
                    match81=re.findall(regex81,Des)
                    regex82=re.compile('\w+')
                    match82=re.findall(regex82,Des)
                    if len(match81)>0:
                         messagebox.showerror("error","Enter alphabates only in description")
                    elif len(match82)<=0:
                         messagebox.showerror("error","Enter the description")
                    else:
                         data=data.replace("$description",Des)
                    reason=e4.get()
                    regex41=re.compile('\d')
                    match41=re.findall(regex41,reason)
                    regex42=re.compile('\w+')
                    match42=re.findall(regex42,reason)
                    if len(match41)>0:
                         messagebox.showerror("error","Enter alphabates only in reason")
                    elif len(match42)<=0:
                         messagebox.showerror("error","Enter the reason")
                    else:
                         data=data.replace("$reason",reason)
                    R_date=str(Rejoining.selection_get())
                    if R_date!='None':
                                   data=data.replace("$r_date",R_date)
                    else:
                              messagebox.showerror("error",'provide dates')
                    count=data.count("$")
                    if count==0:
                         f=open('Casualleave.txt','w')
                         f.write(data)
              
                         messagebox.showinfo("Letter saved","Letter saved as:Casualleave")
               Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
               e2 = Entry(root, font=myFont)
               e2.place(x=350,y=100)
               w = Label(root, text='Name of authority:', font=myFont) 
               w.place(x=100,y=150) 
               v = IntVar() 
               Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
               Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)

               e1 = Entry(root,font=myFont) 
               e1.place(x=880,y=150)
               Label(root, text='No. of Days for leave:',font=myFont).place(x=100,y=200)
               e3 = Entry(root,font=myFont) 
               e3.place(x=350,y=200)
               Label(root, text='Reason:',font=myFont).place(x=100,y=250)
               e4 = Entry(root,font=myFont) 
               e4.place(x=350,y=250,width=750)
               Label(root, text="Description of reason:",font=myFont).place(x=100,y=350)
               e8 = Entry(root,font=myFont) 
               e8.place(x=350,y=350,width=750)
               Label(root, text='Rejoining date:',font=myFont).place(x=900,y=400)
                       
               Rejoining = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
               Rejoining.place(x=900,y=450)
               letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont, command=print_sel1)
               
               letter_button.place(x=900,y=650)
               
               root.mainloop()
class Quehdla:
     def __init__(root):
          root=Tk()
          root.title("Half day leave application")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')
          def print_sel1():
                    fp=open('Halfdayleaveapplication.txt','r+')
                    data=fp.read()
                    
                    A_name=e2.get()
                    regex11=re.compile('\d')
                    match11=re.findall(regex11,A_name)
                    regex12=re.compile('\w+')
                    match12=re.findall(regex12,A_name)
                    if len(match11)>0:
                              messagebox.showerror("error","Enter alphabates only in applicant name")
                    elif len(match12)<=0:
                              messagebox.showerror("error","Enter the applicant name")
                    else:
                              data=data.replace("$name",A_name)

                    Auth_gen=v.get()
                    if Auth_gen==0:
                         data=data.replace("$auth_gen","Mr.")
                    else:
                         data=data.replace("$auth_gen","Mrs./Ms.")
                    
                    Auth_name=e1.get()
                    regex31=re.compile('\d')
                    match31=re.findall(regex31,Auth_name)
                    regex32=re.compile('\w+')
                    match32=re.findall(regex32,Auth_name)
                    if len(match31)>0:
                              messagebox.showerror("error","Enter alphabates only in authority name")
                    elif len(match32)<=0:
                              messagebox.showerror("error","Enter the authority name")
                    else:
                              data=data.replace("$auth_name",Auth_name)
                    Des=e7.get()
                    regex71=re.compile('\d')
                    match71=re.findall(regex31,Des)
                    regex72=re.compile('\w+')
                    match72=re.findall(regex32,Des)
                    if len(match71)>0:
                         messagebox.showerror("error","Enter alphabates only in description")
                    elif len(match72)<=0:
                         messagebox.showerror("error","Enter the description")
                    else:
                         data=data.replace("$description",Des)

                    
                    reason=e4.get()
                    regex41=re.compile('\d')
                    match41=re.findall(regex41,reason)
                    regex42=re.compile('\w+')
                    match42=re.findall(regex42,reason)
                    if len(match41)>0:
                         messagebox.showerror("error","Enter alphabates only in reason")
                    elif len(match42)<=0:
                         messagebox.showerror("error","Enter the reason")
                    else:
                         data=data.replace("$reason",reason)
                    Mail=e8.get()
               
                    match81=re.search("@",Mail)
                    
                    if (match81):
                              data=data.replace("$email",Mail)
                    else:
                              messagebox.showerror("error","Enter the valid email")

                    Mob=e9.get()
                    regex91=re.compile('\D')
                    match91=re.findall(regex91,Mob)
                    regex92=re.compile('\d')
                    match92=re.findall(regex92,Mob)
                    if len(match91)>0:
                              messagebox.showerror("error","Enter numbers only in contact no.")
                    elif len(match92)<=0:
                              messagebox.showerror("error","Enter the contact no.")
                    elif len(match92)<10 or len(match92)>10:
                              messagebox.showerror("error","no. must be 10 digits only")
                    else:
                              data=data.replace("$contact",Mob)
                    
                    tH=str(th.get())
                    tM=str(tm.get())
                    
                    data=data.replace('$thour',tH)
                    data=data.replace('$tmin',tM)
                    R_date=str(Rejoining.selection_get())
                    if R_date!='None':
                                   data=data.replace("$date",R_date)
                    else:
                              messagebox.showerror("error",'provide dates')
                    count=data.count("$")
                    if count==0:
                         f=open('Halfdayleave.txt','w')
                         f.write(data)
              
                         messagebox.showinfo("Letter saved","Letter saved as:Halfdayleave")
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar() 
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)

          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          Label(root, text='Reason:',font=myFont).place(x=100,y=250)
          e4 = Entry(root,font=myFont) 
          e4.place(x=350,y=250,width=750)
          Label(root, text="Description of reason:",font=myFont).place(x=100,y=350)
          e7 = Entry(root,font=myFont) 
          e7.place(x=350,y=350,width=750)
          Label(root, text="Applicant's email:",font=myFont).place(x=100,y=450)
          e8 = Entry(root,font=myFont) 
          e8.place(x=350,y=450)
          Label(root, text="Applicant's phone no.:",font=myFont).place(x=100,y=550)
          e9 = Entry(root,font=myFont)
          e9.place(x=350,y=550)
          Label(root, text="Time when will you join office:",font=myFont).place(x=100,y=650)
          th = Spinbox(root,from_=1,to=24,font=myFont) 
          th.place(x=400,y=650,width=50)
          tm = Spinbox(root,from_=1,to=59,font=myFont)
          tm.place(x=500,y=650,width=50)
          Label(root, text="Date to take half leave:",font=myFont).place(x=900,y=400)
                       
          Rejoining = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          Rejoining.place(x=900,y=450)
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont,command=print_sel1)
               
          letter_button.place(x=900,y=650)
          root.mainloop()
class Quedif:
     def __init__(root):
          root=Tk()
          root.title("Leave application due to death in the family")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')
          def print_sel1():
               fp=open('Leaveapplicationduetodeathinthefamily.txt','r+')
               data=fp.read()
                    
               A_name=e2.get()
               regex11=re.compile('\d')
               match11=re.findall(regex11,A_name)
               regex12=re.compile('\w+')
               match12=re.findall(regex12,A_name)
               if len(match11)>0:
                         messagebox.showerror("error","Enter alphabates only in applicant name")
               elif len(match12)<=0:
                         messagebox.showerror("error","Enter the applicant name")
               else:
                         data=data.replace("$name",A_name)

               Auth_gen=v.get()
               if Auth_gen==0:
                    data=data.replace("$auth_gen","Mr.")
               else:
                    data=data.replace("$auth_gen","Mrs./Ms.")
               
               Auth_name=e1.get()
               regex31=re.compile('\d')
               match31=re.findall(regex31,Auth_name)
               regex32=re.compile('\w+')
               match32=re.findall(regex32,Auth_name)
               if len(match31)>0:
                         messagebox.showerror("error","Enter alphabates only in authority name")
               elif len(match32)<=0:
                         messagebox.showerror("error","Enter the authority name")
               else:
                         data=data.replace("$auth_name",Auth_name)

               D_leave=e3.get()
               regex21=re.compile('\D')
               match21=re.findall(regex21,D_leave)
               regex22=re.compile('\d')
               match22=re.findall(regex22,D_leave)
               if len(match21)>0:
                         messagebox.showerror("error","Enter numbers only in no. of days")
               elif len(match22)<=0:
                         messagebox.showerror("error","Enter the no. of days")
               else:
                         data=data.replace("$period",D_leave)
               relation=e8.get()
               regex81=re.compile('\d')
               match81=re.findall(regex81,relation)
               regex82=re.compile('\w+')
               match82=re.findall(regex82,relation)
               if len(match81)>0:
                         messagebox.showerror("error","Enter alphabates only in relation")
               elif len(match82)<=0:
                         messagebox.showerror("error","Enter the relation")
               else:
                         data=data.replace("$relation",relation)
               Day=(day.get())
               data=data.replace("$day",Day)
               E_date=str(enddate.selection_get())
               R_date=str(Rejoining.selection_get())
               if (E_date>R_date)or((E_date)==(R_date)=='None'):
                         messagebox.showerror("error",'enter valid dates')
               else:
                         data=data.replace("$e_date",E_date)
                         data=data.replace("$r_date",R_date)
               
               count=data.count("$")
               if count==0:
                    f=open('DeathInFamilyleave.txt','w')
                    f.write(data)
              
                    messagebox.showinfo("Letter saved","Letter saved as:DeathInFamilyleave")
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar() 
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)
          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          Label(root, text='Rejoining date:',font=myFont).place(x=900,y=400)
          Label(root, text='Days for leave:',font=myFont).place(x=100,y=200)
          e3 = Entry(root,font=myFont) 
          e3.place(x=350,y=200)
          Label(root, text='Day when relative passed away',font=myFont).place(x=100,y=300)
          day = StringVar(root)
          day.set("Sunday")
          
          week = OptionMenu(root, day,"Sunday", "Monday", "Tuesday", "Wednesday","Thursday","Friday","Satureday" )
          
          week.place(x=500,y=300)
          
          Label(root, text="Relation:",font=myFont).place(x=100,y=450)
          e8 = Entry(root,font=myFont) 
          e8.place(x=350,y=450)
          Label(root, text='Leave ends on:',font=myFont).place(x=600,y=400)
          enddate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          enddate.place(x=600,y=450)
          Rejoining = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          Rejoining.place(x=900,y=450)
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont,command=print_sel1)
               
          letter_button.place(x=900,y=650)
          root.mainloop()
class Queifm:
     def __init__(root):
          root=Tk()
          root.title("Leave application due to the illness of a family member")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')
          def print_sel1():
               fp=open('Leaveapplicationduetotheillnessofafamilymember.txt','r+')
               data=fp.read()
               
               A_name=e2.get()
               regex11=re.compile('\d')
               match11=re.findall(regex11,A_name)
               regex12=re.compile('\w+')
               match12=re.findall(regex12,A_name)
               if len(match11)>0:
                         messagebox.showerror("error","Enter alphabates only in applicant name")
               elif len(match12)<=0:
                         messagebox.showerror("error","Enter the applicant name")
               else:
                         data=data.replace("$name",A_name)

               Auth_gen=v.get()
               if Auth_gen==0:
                    data=data.replace("$auth_gen","Mr.")
               else:
                    data=data.replace("$auth_gen","Mrs./Ms.")
               
               Auth_name=e1.get()
               regex31=re.compile('\d')
               match31=re.findall(regex31,Auth_name)
               regex32=re.compile('\w+')
               match32=re.findall(regex32,Auth_name)
               if len(match31)>0:
                         messagebox.showerror("error","Enter alphabates only in authority name")
               elif len(match32)<=0:
                         messagebox.showerror("error","Enter the authority name")
               else:
                         data=data.replace("$auth_name",Auth_name)
               reason=e4.get()
               regex41=re.compile('\d')
               match41=re.findall(regex41,reason)
               regex42=re.compile('\w+')
               match42=re.findall(regex42,reason)
               if len(match41)>0:
                         messagebox.showerror("error","Enter alphabates only in reason")
               elif len(match42)<=0:
                         messagebox.showerror("error","Enter the reason")
               else:
                         data=data.replace("$reason",reason)
               
               R_date=str(Rejoining.selection_get())
               if R_date!='None':
                                   data=data.replace("$r_date",R_date)
               else:
                              messagebox.showerror("error",'provide dates')
               
               mem_gen=v.get()
               if mem_gen==0:
                         data=data.replace("$genofmem",'his')
               else:
                         data=data.replace("$genofmem","her")
               count=data.count("$")
               if count==0:
                    f=open('IllnessOfFamilyMemberleave.txt','w')
                    f.write(data)
              
                    messagebox.showinfo("Letter saved","Letter saved as:IllnessOfFamilyMemberleave")
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar() 
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)

          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          Label(root, text='Reason:',font=myFont).place(x=100,y=250)
          e4 = Entry(root,font=myFont) 
          e4.place(x=350,y=250,width=750)
          Label(root, text='Rejoining date:',font=myFont).place(x=900,y=400)
          Label(root, text="Family member's gender:",font=myFont).place(x=100,y=300)
          v = IntVar() 
          Radiobutton(root, text='his', variable=v, value=1,font=myFont).place(x=650,y=300) 
          Radiobutton(root, text='her', variable=v, value=2,font=myFont).place(x=700,y=300)

          Rejoining = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          Rejoining.place(x=900,y=450)
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont,command=print_sel1)
          
          letter_button.place(x=900,y=650)
          
          root.mainloop()
class Quemla:
     def __init__(root):
          root=Tk()
          root.title("Maternity leave application")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')
          def print_sel1():
               fp=open('Maternityleaveapplication.txt','r+')
               data=fp.read()
               
               A_name=e2.get()
               regex11=re.compile('\d')
               match11=re.findall(regex11,A_name)
               regex12=re.compile('\w+')
               match12=re.findall(regex12,A_name)
               if len(match11)>0:
                         messagebox.showerror("error","Enter alphabates only in applicant name")
               elif len(match12)<=0:
                         messagebox.showerror("error","Enter the applicant name")
               else:
                         data=data.replace("$name",A_name)

               Auth_gen=v.get()
               if Auth_gen==0:
                    data=data.replace("$auth_gen","Mr.")
               else:
                    data=data.replace("$auth_gen","Mrs./Ms.")
               
               Auth_name=e1.get()
               regex31=re.compile('\d')
               match31=re.findall(regex31,Auth_name)
               regex32=re.compile('\w+')
               match32=re.findall(regex32,Auth_name)
               if len(match31)>0:
                         messagebox.showerror("error","Enter alphabates only in authority name")
               elif len(match32)<=0:
                         messagebox.showerror("error","Enter the authority name")
               else:
                         data=data.replace("$auth_name",Auth_name)

               D_leave=e3.get()
               regex21=re.compile('\D')
               match21=re.findall(regex21,D_leave)
               regex22=re.compile('\d')
               match22=re.findall(regex22,D_leave)
               if len(match21)>0:
                         messagebox.showerror("error","Enter numbers only in no. of days")
               elif len(match22)<=0:
                         messagebox.showerror("error","Enter the no. of days")
               else:
                         data=data.replace("$period",D_leave)
               P_gen=v.get()
               if P_gen==0:
                    data=data.replace("$p'sgen","Mr.")
               else:
                    data=data.replace("$p'sgen","Mrs./Ms.")
               P_name=e7.get()
               regex71=re.compile('\d')
               match71=re.findall(regex71,P_name)
               regex72=re.compile('\w+')
               match72=re.findall(regex72,P_name)
               if len(match71)>0:
                         messagebox.showerror("error","Enter alphabates only in person's name")
               elif len(match72)<=0:
                         messagebox.showerror("error","Enter the person's name")
               else:
                         data=data.replace("$p'sname",P_name)
               Mail=e8.get()
               
               match81=re.search("@",Mail)
               
               if (match81):
                         data=data.replace("$email",Mail)
               else:
                         messagebox.showerror("error","Enter the valid email")
               Mob=e9.get()
               regex91=re.compile('\D')
               match91=re.findall(regex91,Mob)
               regex92=re.compile('\d')
               match92=re.findall(regex92,Mob)
               if len(match91)>0:
                         messagebox.showerror("error","Enter numbers only in contact no.")
               elif len(match92)<=0:
                         messagebox.showerror("error","Enter the contact no.")
               elif len(match92)<10 or len(match92)>10:
                         messagebox.showerror("error","no. must be 10 digits only")
               else:
                         data=data.replace("$contact",Mob)
               S_date=str(startdate.selection_get())
               E_date=str(enddate.selection_get())
               
               if (S_date>E_date)or((S_date)==(E_date)=='None'):
                         messagebox.showerror("error",'enter valid dates')
               else:
                         data=data.replace("$s_date",S_date)
                         data=data.replace("$e_date",E_date)
               count=data.count("$")
               if count==0:
                    f=open('Maternityleave.txt','w')
                    f.write(data)
              
                    messagebox.showinfo("Letter saved","Letter saved as:Maternityleave")
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar() 
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)
          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          Label(root, text='Person whome you delegated current project:',font=myFont).place(x=100,y=300)
          v = IntVar() 
          Radiobutton(root, text='Mr.', variable=v, value=1,font=myFont).place(x=650,y=300) 
          Radiobutton(root, text='Mrs./Ms.', variable=v, value=2,font=myFont).place(x=700,y=300)

          e7 = Entry(root,font=myFont) 
          e7.place(x=880,y=300)
          
          Label(root, text="Applicant's email:",font=myFont).place(x=100,y=350)
          e8 = Entry(root,font=myFont) 
          e8.place(x=350,y=350)
          Label(root, text="Applicant's phone no.:",font=myFont).place(x=650,y=350)
          e9 = Entry(root,font=myFont)
          e9.place(x=880,y=350)
          Label(root, text='No. of Days for leave:',font=myFont).place(x=100,y=200)
          e3 = Entry(root,font=myFont) 
          e3.place(x=350,y=200)
          
          Label(root, text='Leave starts from:',font=myFont).place(x=100,y=400)
          startdate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          startdate.place(x=100,y=450)
          
          Label(root, text='Leave ends on:',font=myFont).place(x=550,y=400)
          enddate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          enddate.place(x=550,y=450)
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont,command=print_sel1)
          
          letter_button.place(x=900,y=650)
          root.mainloop()
class Queodla:
     def __init__(root):
          root=Tk()
          root.title("One day leave application")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')
          def print_sel1():
               fp=open('Onedayleaveapplication.txt','r+')
               data=fp.read()
               
               A_name=e2.get()
               regex11=re.compile('\d')
               match11=re.findall(regex11,A_name)
               regex12=re.compile('\w+')
               match12=re.findall(regex12,A_name)
               if len(match11)>0:
                         messagebox.showerror("error","Enter alphabates only in applicant name")
               elif len(match12)<=0:
                         messagebox.showerror("error","Enter the applicant name")
               else:
                         data=data.replace("$name",A_name)

               Auth_gen=v.get()
               if Auth_gen==0:
                    data=data.replace("$auth_gen","Mr.")
               else:
                    data=data.replace("$auth_gen","Mrs./Ms.")
               
               Auth_name=e1.get()
               regex31=re.compile('\d')
               match31=re.findall(regex31,Auth_name)
               regex32=re.compile('\w+')
               match32=re.findall(regex32,Auth_name)
               if len(match31)>0:
                         messagebox.showerror("error","Enter alphabates only in authority name")
               elif len(match32)<=0:
                         messagebox.showerror("error","Enter the authority name")
               else:
                         data=data.replace("$auth_name",Auth_name)
               reason=e4.get()
               regex41=re.compile('\d')
               match41=re.findall(regex41,reason)
               regex42=re.compile('\w+')
               match42=re.findall(regex42,reason)
               if len(match41)>0:
                         messagebox.showerror("error","Enter alphabates only in reason")
               elif len(match42)<=0:
                         messagebox.showerror("error","Enter the reason")
               else:
                         data=data.replace("$reason",reason)
               Mail=e8.get()
               
               match81=re.search("@",Mail)
               
               if (match81):
                         data=data.replace("$email",Mail)
               else:
                         messagebox.showerror("error","Enter the valid email")
               date=str(startdate.selection_get())
               if date!='None':
                                   data=data.replace("$date",date)
               else:
                              messagebox.showerror("error",'provide dates')
               Mob=e9.get()
               regex91=re.compile('\D')
               match91=re.findall(regex91,Mob)
               regex92=re.compile('\d')
               match92=re.findall(regex92,Mob)
               if len(match91)>0:
                         messagebox.showerror("error","Enter numbers only in cantact no.")
               elif len(match92)<=0:
                         messagebox.showerror("error","Enter the mobile no.")
               elif len(match92)<10 or len(match92)>10:
                         messagebox.showerror("error","Mobile no. must be 10 digits only")
               else:
                         data=data.replace("$contact",Mob)
               count=data.count("$")
               if count==0:
                    f=open('Onedayleave.txt','w')
                    f.write(data)
              
                    messagebox.showinfo("Letter saved","Letter saved as:Onedayleave")
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar()
          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)
          Label(root, text="Applicant's email:",font=myFont).place(x=100,y=350)
          e8 = Entry(root,font=myFont) 
          e8.place(x=350,y=350)
          Label(root, text="Applicant's phone no.:",font=myFont).place(x=650,y=350)
          e9 = Entry(root,font=myFont)
          e9.place(x=880,y=350)
          Label(root, text='Reason:',font=myFont).place(x=100,y=250)
          e4 = Entry(root,font=myFont) 
          e4.place(x=350,y=250,width=750)
          Label(root, text='Date for leave:',font=myFont).place(x=100,y=400)
          startdate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          startdate.place(x=100,y=450)
          
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont,command=print_sel1)
          
          letter_button.place(x=900,y=650)
          root.mainloop()
class Quepla:
     def __init__(root):
          root=Tk()
          root.title("Paternity leave application")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')
          def print_sel1():
               fp=open('Paternityleaveapplication.txt','r+')
               data=fp.read()
               
               A_name=e2.get()
               regex11=re.compile('\d')
               match11=re.findall(regex11,A_name)
               regex12=re.compile('\w+')
               match12=re.findall(regex12,A_name)
               if len(match11)>0:
                         messagebox.showerror("error","Enter alphabates only in applicant name")
               elif len(match12)<=0:
                         messagebox.showerror("error","Enter the applicant name")
               else:
                         data=data.replace("$name",A_name)

               Auth_gen=v.get()
               if Auth_gen==0:
                    data=data.replace("$auth_gen","Mr.")
               else:
                    data=data.replace("$auth_gen","Mrs./Ms.")
               
               Auth_name=e1.get()
               regex31=re.compile('\d')
               match31=re.findall(regex31,Auth_name)
               regex32=re.compile('\w+')
               match32=re.findall(regex32,Auth_name)
               if len(match31)>0:
                         messagebox.showerror("error","Enter alphabates only in authority name")
               elif len(match32)<=0:
                         messagebox.showerror("error","Enter the authority name")
               else:
                         data=data.replace("$auth_name",Auth_name)

               D_leave=e3.get()
               regex21=re.compile('\D')
               match21=re.findall(regex21,D_leave)
               regex22=re.compile('\d')
               match22=re.findall(regex22,D_leave)
               if len(match21)>0:
                         messagebox.showerror("error","Enter numbers only in no. of days")
               elif len(match22)<=0:
                         messagebox.showerror("error","Enter the no. of days")
               else:
                         data=data.replace("$period",D_leave)
               P_gen=v.get()
              
               for i in data:
                    if i.find("$p'gen"):
                         if P_gen==0:
                              data=data.replace("$p'gen","Mr.")
                         else:
                              data=data.replace("$p'gen","Mrs./Ms.")
                         
               P_name=e7.get()
               regex71=re.compile('\d')
               match71=re.findall(regex71,P_name)
               regex72=re.compile('\w+')
               match72=re.findall(regex72,P_name)
               for i in data:
                    if i.find("$p'sname"):
                         if len(match71)>0:
                              messagebox.showerror("error","Enter alphabates only in person's name")
                         elif len(match72)<=0:
                              messagebox.showerror("error","Enter the person's name")
                         else:
                              data=data.replace("$p'sname",P_name)
               date=str(startdate.selection_get())
               if date!='None':
                                   data=data.replace("$s_date",date)
               else:
                              messagebox.showerror("error",'provide dates')
               tH=int(th.get())
               if tH==1:
                    data=data.replace('$baby','1st')
               elif tH==2:
                    data=data.replace('$baby','2nd')
               elif tH==3:
                    data=data.replace('$baby','3rd')
               elif tH==4:
                    data=data.replace('$baby','4th')
               else:
                    data=data.replace('$baby','5th')
               count=data.count("$")
               if count==0:
                    f=open('Paternityleave.txt','w')
                    f.write(data)
              
                    messagebox.showinfo("Letter saved","Letter saved as:PaternityLeave")
               
                    
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar() 
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)
          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          Label(root, text='Person whome you delegated current project:',font=myFont).place(x=100,y=300)
          v = IntVar() 
          Radiobutton(root, text='Mr.', variable=v, value=1,font=myFont).place(x=650,y=300) 
          Radiobutton(root, text='Mrs./Ms.', variable=v, value=2,font=myFont).place(x=700,y=300)

          e7 = Entry(root,font=myFont) 
          e7.place(x=880,y=300)
          Label(root, text='No. of Days for leave:',font=myFont).place(x=100,y=200)
          e3 = Entry(root,font=myFont) 
          e3.place(x=350,y=200)
          Label(root, text="Which no. baby will:",font=myFont).place(x=550,y=400)
          th = Spinbox(root,from_=1,to=5,font=myFont) 
          th.place(x=750,y=400,width=50)
          Label(root, text='Leave starts from:',font=myFont).place(x=100,y=400)
          startdate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          startdate.place(x=100,y=450)
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont,command=print_sel1)
          
          letter_button.place(x=900,y=650)
          root.mainloop()
class Quevla:
     def __init__(root):
          root=Tk()
          root.title("Vacation leave application")
          root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
          myFont = ('Helvetica',15,'bold')
          def print_sel1():
               fp=open('Vacationleaveapplication.txt','r+')
               data=fp.read()
               
               A_name=e2.get()
               regex11=re.compile('\d')
               match11=re.findall(regex11,A_name)
               regex12=re.compile('\w+')
               match12=re.findall(regex12,A_name)
               if len(match11)>0:
                         messagebox.showerror("error","Enter alphabates only in applicant name")
               elif len(match12)<=0:
                         messagebox.showerror("error","Enter the applicant name")
               else:
                         data=data.replace("$name",A_name)

               Auth_gen=v.get()
               if Auth_gen==0:
                    data=data.replace("$auth_gen","Mr.")
               else:
                    data=data.replace("$auth_gen","Mrs./Ms.")
               
               Auth_name=e1.get()
               regex31=re.compile('\d')
               match31=re.findall(regex31,Auth_name)
               regex32=re.compile('\w+')
               match32=re.findall(regex32,Auth_name)
               if len(match31)>0:
                         messagebox.showerror("error","Enter alphabates only in authority name")
               elif len(match32)<=0:
                         messagebox.showerror("error","Enter the authority name")
               else:
                         data=data.replace("$auth_name",Auth_name)
               Season=day.get()
               data=data.replace("$season",Season)
               D_leave=e3.get()
               regex21=re.compile('\D')
               match21=re.findall(regex21,D_leave)
               regex22=re.compile('\d')
               match22=re.findall(regex22,D_leave)
               if len(match21)>0:
                         messagebox.showerror("error","Enter numbers only in no. of days")
               elif len(match22)<=0:
                         messagebox.showerror("error","Enter the no. of days")
               else:
                         data=data.replace("$period",D_leave)
               place=e7.get()
               regex71=re.compile('\d')
               match71=re.findall(regex31,place)
               regex72=re.compile('\w+')
               match72=re.findall(regex32,place)
               if len(match71)>0:
                         messagebox.showerror("error","Enter alphabates only in place")
               elif len(match72)<=0:
                         messagebox.showerror("error","Enter the place")
               else:
                         data=data.replace("$place",place)
               S_date=str(startdate.selection_get())
               E_date=str(enddate.selection_get())
               if (S_date>E_date)or((S_date)==(E_date)=='None'):
                         messagebox.showerror("error",'enter valid dates')
               else:
                         data=data.replace("$s_date",S_date)
                         data=data.replace("$e_date",E_date)
               count=data.count("$")
               if count==0:
                    f=open('Vacationalleave.txt','w')
                    f.write(data)
              
                    messagebox.showinfo("Letter saved","Letter saved as:Vacationalleave")
          Label(root, text="applicant's name:", font=myFont).place(x=100,y=100)
          e2 = Entry(root, font=myFont)
          e2.place(x=350,y=100)
          w = Label(root, text='Name of authority:', font=myFont) 
          w.place(x=100,y=150) 
          v = IntVar() 
          Radiobutton(root, text='Mr.',font=myFont, variable=v, value=1).place(x=650,y=150) 
          Radiobutton(root, text='Mrs./Ms.',font=myFont, variable=v, value=2).place(x=700,y=150)
          e1 = Entry(root,font=myFont) 
          e1.place(x=880,y=150)
          
          Label(root, text='Season',font=myFont).place(x=800,y=300)
          day = StringVar(root)
          day.set("Summer")
          
          week = OptionMenu(root, day,"Summer", "Winter", "Monsoon")
          
          week.place(x=880,y=300)
          Label(root, text='No. of Days for leave:',font=myFont).place(x=100,y=200)
          e3 = Entry(root,font=myFont) 
          e3.place(x=350,y=200)
          Label(root, text="Place where you're going for vacation:",font=myFont).place(x=100,y=300)
          e7 = Entry(root,font=myFont) 
          e7.place(x=500,y=300)
          Label(root, text='Leave starts from:',font=myFont).place(x=100,y=400)
          startdate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          startdate.place(x=100,y=450)
          letter_button = Button(root, text = 'Generate letter',bg='#000000',fg='#ffffff', font=myFont,command=print_sel1)
          Label(root, text='Leave ends on:',font=myFont).place(x=550,y=400)
          enddate = Calendar(root, width=12, background='darkblue', selectmode='day', cursor='hand1',year=2020)
          enddate.place(x=550,y=450)
          letter_button.place(x=900,y=650)
          root.mainloop()


def ALA():
     
     q=Queala()
     
     
def CLA():
     q=Quecla()

def HDLA():
     q=Quehdla()

def DIF():
     q=Quedif()
     
def IFM():
     q=Queifm()

def MLA():
     q=Quemla()
     
def ODLA():
     q=Queodla()
     
def PLA():
     q=Quepla()

def VLA():
     q=Quevla()


#LEAVE LETTER
menubutton1 = Menubutton(top, text = "LEAVE LETTER",bg='#000000',fg='#ffffff', relief = RAISED, font=myFont)  

menubutton1.place(x=100,y=100,height=100,width=250)
'''menubutton2 = Menubutton(top, text = "OTHER OPTIONS", relief = RAISED)  
  
menubutton2.grid()'''  
  
menubutton1.menu = Menu(menubutton1, font=myFont)
#Menu.place(x=100,y=100,height=100,width=250)
  
menubutton1["menu"]=menubutton1.menu  
  
menubutton1.menu.add_checkbutton(label = "Annual leave application",command=ALA)  
  
menubutton1.menu.add_checkbutton(label = "Casual leave application",command=CLA)

menubutton1.menu.add_checkbutton(label = "Half day leave application",command=HDLA)

menubutton1.menu.add_checkbutton(label = "Leave application due to death in the family",command=DIF)

menubutton1.menu.add_checkbutton(label = "Leave application due to the illness of a family member",command=IFM)

menubutton1.menu.add_checkbutton(label = "Maternity leave application",command=MLA)

menubutton1.menu.add_checkbutton(label = "One day leave application",command=ODLA)

menubutton1.menu.add_checkbutton(label = "Paternity leave application",command=PLA)

menubutton1.menu.add_checkbutton(label = "Vacation leave application",command=VLA)
#menubutton1.pack()  
  
top.mainloop()
