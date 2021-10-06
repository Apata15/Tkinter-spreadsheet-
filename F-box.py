from tkinter import *
from tkinter.tix import *
#import pyvips
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
from tkinter import font
import ctypes
import win32con
from  multiprocessing import Process,freeze_support,pool
from multiprocessing.dummy import Pool as ThreadPool
import threading
from time import sleep
from os import path
import sys
import os.path
#from win32api import GetSystemMetrics
import sqlite3
import pickle
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.messagebox import showwarning
from tkinter.messagebox import askokcancel
from tkinter.messagebox import askyesno
from winsound import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from tkinter import colorchooser
ctypes.windll.shcore.SetProcessDpiAwareness(2)





root=Tk()


               
sys.setrecursionlimit(20000)
#f-analysis class frame
class Financial:
    def __init__(self,main):
        myframe=Frame()
        
        self.myframe=myframe
        self.photo=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\Untitled-1FRE-Temp0001.pn.png")
        self.photo=self.photo.resize((round(root.winfo_screenwidth()/2.4),round(root.winfo_screenheight()/5.4)))
        self.show=ImageTk.PhotoImage(self.photo)
        self.showit=Label(root,image=self.show,bd=0,borderwidth=0)
        #condition whereby  check buttons file for the themes is not created it creates one automatically
        if path.exists('check.pkl')==False:
            data=0
            with open('check.pkl', 'wb') as f1:
               self.data=pickle.dump(data,f1)
               f1.close()
            with open('check.pkl','rb') as f1:
                self.data=pickle.load(f1)
        #condition whereby  template file not created it creates one automatically
        if path.exists('loader.pk')==False:
            
            data2='Main'
            with open('loader.pk', 'wb') as f2:
               self.data3=pickle.dump(data2,f2)
               f2.close()
            with open('loader.pk','rb') as f2:
                self.data3=pickle.load(f2)
         # condition whereby the check button exists and it's size is greater than 0     
        if path.exists('check.pkl')==True and os.path.getsize('check.pkl')>0:
              with open('check.pkl','rb') as f1:
                  self.data=pickle.load(f1)
         # condition whereby the template exists and it's size is greater than 0 
        if path.exists('loader.pk')==True and os.path.getsize('loader.pk')>0:
              
              with open('loader.pk','rb') as f2:
                  self.data3=pickle.load(f2)
        if path.exists('data.db')==False:
            data=sqlite3.connect('data.db')
            connet=data.cursor()
            connet.execute("CREATE TABLE data(cells TEXT,row1 TEXT,row2 TEXT,row3 TEXT,row4 TEXT,row5 TEXT,row6 TEXT,row7 TEXT,row8 text)")
            
            data.commit()
            data.close()
        if path.exists('data.db')==True:
            if path.exists('loader.pk')==True and os.path.getsize('loader.pk')>0:
              
              with open('loader.pk','rb') as f2:
                  self.data3=pickle.load(f2)
                  print(self.data3)
                  data=sqlite3.connect('data.db')
                  connet=data.cursor()
                  self.names=connet.execute("SELECT cells FROM {}".format(self.data3)).fetchall()
            
                  self.play=connet.execute('SELECT rowid FROM {}'.format(self.data3)).fetchall()
            
                  data.commit()
                  data.close()
                  
           
        
                  
        
       
        


       
       # print(main.label.cget('text'))
        self.top=Toplevel(root)
        #self.top.geometry('{}x{}+0+0'.format(self.top.winfo_screenwidth(),self.top.winfo_screenheight()))
        
        self.top.withdraw()
        
    def get(self):
        self.top.deiconify()
        self.width=self.top.winfo_screenwidth()
        self.height=self.top.winfo_screenheight()
        root.withdraw()
        #self.top=self.top
        
        
        self.top.bind('<Alt-F4>',self.close)
        self.v=IntVar()
        self.v.set(round(0.00625*self.width))
        self.top.geometry('{}x{}+0+1'.format(self.width,self.height))
        
        #self.top.protocol('WM_DELETE_WINDOW',second.close)
        
        self.top.bind('<Configure>',self.master_update)
        my_menu=Menu(self.top,background='black',activebackground='black',foreground='white',bg='black',borderwidth=0,bd=0)
        self.g='200x200+0+0'
        #self.top.wm_attributes('-type','splash')
        self.top.overrideredirect(True)
        #self.top.state('zoomed')
        
        
        
       
        
        
        photos1=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\bar.png")
        photos1=ImageTk.PhotoImage(photos1)
        photos2=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\scatter.png")
        photos2=ImageTk.PhotoImage(photos2)
        photos3=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\basic.png")
        photos3=ImageTk.PhotoImage(photos3)
        
        
        photos4=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\rank.png")
        photos4=ImageTk.PhotoImage(photos4)
        photos5=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\max.png")
        photos5=ImageTk.PhotoImage(photos5)
      
       
        
        self.nam=['1']*50
        self.j2=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\suunday.png")
        self.j2=ImageTk.PhotoImage(self.j2)
        self.top.wm_title('Financial Analysis')
        self.top.config(bg='white')
        self.top.iconphoto(False,self.j2)
        
        #Main canvas that contains the spreadsheet widgets
        self.c = Canvas(self.top,borderwidth=0,width=self.width//1.1925465839,
                        height=self.height//1.2705882353,bg='#EBEBE6',highlightthickness=0)
        
        #canvas that contains columns names
        self.c3=Canvas(self.top,bg='black',width=self.width//1.1925465839,
                       height=self.height//36,bd=0,borderwidth=0,highlightthickness=0)
        #canvas that contains the cell row names label
        self.c4=Canvas(self.top,bg='black',width=self.width//6.7605633803,
                       height=self.width//36,bd=0,borderwidth=0,highlightthickness=0)
        #canvas that contains that contains the menu bar1
        self.toolbar=Canvas(self.top,width=self.width//1.1925465839,
                            height=0.05*self.height,bg='white',bd=0,borderwidth=0,highlightthickness=0)
        #canvas that contains the menubars 2
        self.toolbar2=Canvas(self.top,width=self.width//6.7605633803,
                             height=0.05*self.height,bg='white',bd=0,borderwidth=0,highlightthickness=0)
        self.c41=self.c4.create_text(round(self.width/13.24),round(self.height/72),text='Cells Names',font=('Helvatica',self.v.get(),'bold'),fill='red')
        #container frame for the main csnvas
        self.f2=Frame(self.c,bg='#EBEBE6')
        #canvas that contains the row names i.e cell row names
        self.c2=Canvas(self.top,bg='#EBEBE6',width=self.width//6.7605633803,
                       height=self.height//1.2705882353,borderwidth=0,highlightthickness=0,bd=0)
        self.top.bind('<Up>',self.up)
        self.top.bind('<Down>',self.down)
        self.top.bind('<Right>',self.right)
        self.top.bind('<Left>',self.left)
        #frame that contains the cell row names i.e cell row names
        self.f3=Frame(self.c2,bg='#EBEBE6')
        #canvas that contains the ent and bu widgets for auto-calculation
        self.testf=Canvas(self.top,borderwidth=0,width=self.width//1.1925465839,
                          height=self.height//7.397260274,bg='white',highlightthickness=0)
        
        #frame that contains the canvas that holds the ent and bu widgets
        self.test9=Frame(self.testf)
        #canvas that hold the configure button and back button
        self.testy=Canvas(self.top,borderwidth=0,width=round(self.width//6.7605633803),
                          height=round(self.height//7.397260274),bg='white',highlightthickness=0)
        #frames that contains the canvas which holds the config butt and back butt
        self.test10=Frame(self.testy,bg='white')
        print(root.winfo_screenwidth())
        
        self.barframe=Canvas(self.top,bg='white',width=round(self.width//6.1935483871),
                             height=round(self.height//7.397260274),bd=-2,highlightthickness=0,borderwidth=0)
       
        self.barframe2=Frame(self.barframe,bg='white')
        #barframe3=Canvas(barframe2,bg='blue',width=310,height=0.05*self.top.winfo_screenheight())
        self.sc1=Scrollbar(self.top,orient='vertical',command=self.scroll,bg='black')
        
        self.sc=Scrollbar(self.test10,orient='horizontal',command=self.scroll1)
        self.f4=Frame(self.c3,bg='#EBEBE6')
        self.f6=Frame(self.toolbar2,bg='white')
        self.f7=Frame(self.toolbar,bg='white')
        menu1=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\print.png")
        menu1=menu1.resize((int(self.width//42.666666667),int(self.height//27)))
        menu1=ImageTk.PhotoImage(menu1)
        menu2=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\pdf.png")
        menu2=menu2.resize((int(self.width//48),int(self.height//27)))
        menu2=ImageTk.PhotoImage(menu2)
        menu3=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\Excel.png")
        menu3=menu3.resize((int(self.width//38.4),int(self.height//25.11627907)))
        menu3=ImageTk.PhotoImage(menu3)
        
       

        
        self.one=Menubutton(self.f6,text='Create New Template',font=('Time',self.v.get()-1),bg='white',fg='black',activebackground='grey',activeforeground='white',
                            height=3,width=17,bd=-2,borderwidth=-2,highlightthickness=0)
        self.two=Menubutton(self.f7,text='Menu',font=('Time',self.v.get()-1),bg='white',fg='black',activebackground='grey',activeforeground='white',
                            height=3,bd=-2,borderwidth=-2,highlightthickness=0)
        self.three=Menubutton(self.f7,text='Edit',font=('Time',self.v.get()-1),bg='white',fg='black',activebackground='grey',activeforeground='white',
                            height=3,width=4,bd=-2,borderwidth=-2,highlightthickness=0)
        self.four=Menubutton(self.f7,text='Graph',font=('Time',self.v.get()-1),bg='white',fg='black',activebackground='grey',activeforeground='white',
                            height=3,width=4,bd=-2,borderwidth=-2,highlightthickness=0)
        self.five=Menubutton(self.f7,text='Functions',font=('Time',self.v.get()-1),bg='white',fg='black',activebackground='grey',activeforeground='white',
                            height=3,width=7,bd=-2,borderwidth=-2,highlightthickness=0)
       
        
        self.six=Button(self.f7,image=menu1,bg='black',activebackground='grey',bd=0,borderwidth=0)
       
        self.six.menu1=menu1
        self.seven=Button(self.f7,image=menu2,bg='black',activebackground='grey',bd=0,borderwidth=0)
        self.seven.menu2=menu2
        hov2=Hovertip(self.seven,'Convert To PDF Format',hover_delay=500)
        self.eight=Button(self.f7,image=menu3,bg='black',activebackground='grey',bd=0,borderwidth=0)
        self.eight.menu3=menu3
        hov2=Hovertip(self.eight,'Convert To Excel Format',hover_delay=500)
        self.template=Label(self.f7,text=self.data3)
        
        
        self.top.bind('<ButtonPress-1>',self.tryer1)
        self.ted=Menu(self.one,tearoff=0,activebackground='white',activeforeground='black',bg='black',fg='white',activeborderwidth=0,bd=-2,borderwidth=0)
        self.ted1=Menu(self.two,tearoff=0,activebackground='white',activeforeground='black',bg='black',fg='white',activeborderwidth=0)
        self.ted2=Menu(self.three,tearoff=0,activebackground='white',activeforeground='black',bg='black',fg='white',activeborderwidth=0)
        self.ted3=Menu(self.four,tearoff=0,activebackground='white',activeforeground='black',bg='black',fg='white',activeborderwidth=0)
        self.ted4=Menu(self.five,tearoff=0,activebackground='white',activeforeground='black',bg='black',fg='white',activeborderwidth=0,bd=0)
        self.one['menu']=self.ted
        self.two['menu']=self.ted1
        self.three['menu']=self.ted2
        self.four['menu']=self.ted3
        self.five['menu']=self.ted4
        self.two.grid(row=0,column=0,sticky='w',padx=8)
        self.one.grid(row=0,column=0,sticky='w',padx=8)
        self.three.grid(row=0,column=1,sticky='w')
        self.four.grid(row=0,column=2,sticky='w',padx=8)
        self.five.grid(row=0,column=3,sticky='w',padx=8)
        self.six.grid(row=0,column=4,sticky='w',padx=8)
        hov1=Hovertip(self.six,'Print File',hover_delay=500)
        self.seven.grid(row=0,column=5,sticky='w',padx=8)
        self.eight.grid(row=0,column=6,sticky='w',padx=8)
        self.template.grid(row=0,column=10,sticky='w',)
        self.ted.add_command(label='Create',command=self.create)
        self.ted.add_command(label='Load',command=self.load)
        self.ted.add_command(label='Edit')
        self.ted.add_command(label='Delete')
        self.ted1.add_command(label='Open')
        self.ted1.add_command(label='Open As')
        self.ted1.add_command(label='Save')
        self.ted1.add_command(label='Save As')
        self.ted1.add_command(label='Save As')
        self.ted1.add_command(label='Print')
        self.ted1.add_command(label='Open Recent')
        self.ted1.add_command(label='Options')
        self.ted1.add_command(label='Exit')
        self.ted3.add_command(label='Basic Graph',image=photos3,compound='left',command=self.graph)
        self.ted3.photos3=photos3
        self.ted3.add_command(label='Scatter Graph',image=photos2,compound='left',command=self.graph2)
        self.ted3.photos2=photos2
        self.ted3.add_command(label='Bar Graph',image=photos1,compound='left',command=self.graph3)
        self.ted3.photos1=photos1
        self.ted4.add_command(label='Sum',command=self.sum)
        self.ted4.add_command(label='Average',command=self.average)
        self.ted4.add_command(label='Rank',image=photos4,compound='left',command=self.rank)
        self.ted4.photos4=photos4
        self.ted4.add_command(label='Min',command=self.min)
        self.ted4.add_command(label='Max',image=photos5,compound='left',command=self.max)
        self.ted4.photos5=photos5
        
        
        #this are the entries for the function answers
        ent=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent.grid(row=0,column=1)
        sep=ttk.Separator(self.test9,orient='vertical')
        sep.grid(row=0,column=1,rowspan=2,columnspan=2,sticky='ns')
        h11.append(ent)
        ent2=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent2.grid(row=0,column=2)
        sep1=ttk.Separator(self.test9,orient='vertical')
        sep1.grid(row=0,column=2,rowspan=2,columnspan=2,sticky='ns')
        h11.append(ent2)
        ent3=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent3.grid(row=0,column=3)
        sep2=ttk.Separator(self.test9,orient='vertical')
        sep2.grid(row=0,column=3,rowspan=2,columnspan=2,sticky='ns')
        h11.append(ent3)
        ent4=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent4.grid(row=0,column=4)
        sep3=ttk.Separator(self.test9,orient='vertical')
        sep3.grid(row=0,column=4,rowspan=2,columnspan=2,sticky='ns')
        h11.append(ent4)
        ent5=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent5.grid(row=0,column=5)
        sep4=ttk.Separator(self.test9,orient='vertical')
        sep4.grid(row=0,column=5,rowspan=2,columnspan=2,sticky='ns')
        h11.append(ent5)
        ent6=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent6.grid(row=0,column=6)
        sep5=ttk.Separator(self.test9,orient='vertical')
        sep5.grid(row=0,column=6,rowspan=2,columnspan=2,sticky='ns')
        h11.append(ent6)
        ent7=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent7.grid(row=0,column=7)
        sep6=ttk.Separator(self.test9,orient='vertical')
        sep6.grid(row=0,column=7,rowspan=2,columnspan=2,sticky='ns')
        h11.append(ent7)
        ent8=Text(self.test9,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                   wrap='char',undo=True,cursor='arrow',highlightthickness=0,state='disabled')
        ent8.grid(row=0,column=8)
        h11.append(ent8)
        
        
        
        self.lf=round(0.0067708333*self.top.winfo_screenwidth())  #this is the font size variable for the p labels
        self.ls=16 #this is the width size of the p label
        #this the popupmenu for sum fuction
        self.men=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men.add_cascade(label='    Choose',state='disabled')
        self.men.add_separator()
        self.men.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,w=ent,x=1000:self.cal(l,d,w,x))
        self.men.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,w=ent2,x=500:self.cal(l,d,w,x))
        self.men.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,w=ent3,x=200:self.cal(l,d,w,x))
        self.men.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,w=ent4,x=100:self.cal(l,d,w,x))
        self.men.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,w=ent5,x=50:self.cal(l,d,w,x))
        self.men.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,w=ent6,x=20:self.cal(l,d,w,x))
        self.men.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,w=ent7,x=10:self.cal(l,d,w,x))
        self.men.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,w=ent8,x=5:self.cal(l,d,w,x))
        #This is the the popupmenu for average function
        self.men2=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men2.add_cascade(label='    Choose',state='disabled')
        self.men2.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,w=ent,x=1000:self.cal2(l,d,w,x))
        self.men2.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,w=ent2,x=500:self.cal2(l,d,w,x))
        self.men2.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,w=ent3,x=200:self.cal2(l,d,w,x))
        self.men2.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,w=ent4,x=100:self.cal2(l,d,w,x))
        self.men2.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,w=ent5,x=50:self.cal2(l,d,w,x))
        self.men2.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,w=ent6,x=20:self.cal2(l,d,w,x))
        self.men2.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,w=ent7,x=10:self.cal2(l,d,w,x))
        self.men2.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,w=ent8,x=5:self.cal2(l,d,w,x))
        #This is the popupmenu for rank function
        self.men3=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men3.add_cascade(label='    Choose',state='disabled')
        self.men3.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,x='1000 Row':self.cal3(l,d,x))
        self.men3.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,x='500 Row':self.cal3(l,d,x))
        self.men3.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,x='200 Row':self.cal3(l,d,x))
        self.men3.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,x='100 Row':self.cal3(l,d,x))
        self.men3.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,x='50 Row':self.cal3(l,d,x))
        self.men3.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,x='20 Row':self.cal3(l,d,x))
        self.men3.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,x='10 Row':self.cal3(l,d,x))
        self.men3.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,x='5 Row':self.cal3(l,d,x))
        #This is the popup menu for min function
        self.men4=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men4.add_cascade(label='    Choose',state='disabled')
        self.men4.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,w=ent:self.cal4(l,d,w))
        self.men4.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,w=ent2:self.cal4(l,d,w))
        self.men4.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,w=ent3:self.cal4(l,d,w))
        self.men4.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,w=ent4:self.cal4(l,d,w))
        self.men4.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,w=ent5:self.cal4(l,d,w))
        self.men4.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,w=ent6:self.cal4(l,d,w))
        self.men4.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,w=ent7:self.cal4(l,d,w))
        self.men4.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,w=ent8:self.cal4(l,d,w))
        #This the popup menu for max function
        self.men5=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men5.add_cascade(label='    Choose',state='disabled')
        self.men5.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,w=ent:self.cal5(l,d,w))
        self.men5.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,w=ent2:self.cal5(l,d,w))
        self.men5.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,w=ent3:self.cal5(l,d,w))
        self.men5.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,w=ent4:self.cal5(l,d,w))
        self.men5.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,w=ent5:self.cal5(l,d,w))
        self.men5.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,w=ent6:self.cal5(l,d,w))
        self.men5.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,w=ent7:self.cal5(l,d,w))
        self.men5.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,w=ent8:self.cal5(l,d,w))
        #This is popupmenu for basic graph plot
        self.men6=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men6.add_cascade(label='    Choose',state='disabled')
        self.men6.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,x='1000 Row':self.cal6(l,d,x))
        self.men6.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,x='500 Row':self.cal6(l,d,x))
        self.men6.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,x='200 Row':self.cal6(l,d,x))
        self.men6.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,x='100 Row':self.cal6(l,d,x))
        self.men6.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,x='50 Row':self.cal6(l,d,x))
        self.men6.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,x='20 Row':self.cal6(l,d,x))
        self.men6.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,x='10 Row':self.cal6(l,d,x))
        self.men6.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,x='5 Row':self.cal6(l,d,x))
        #This is the popup menu for scatter graph plot
        self.men7=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men7.add_cascade(label='    Choose',state='disabled')
        self.men7.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,x='1000 Row':self.cal7(l,d,x))
        self.men7.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,x='500 Row':self.cal7(l,d,x))
        self.men7.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,x='200 Row':self.cal7(l,d,x))
        self.men7.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,x='100 Row':self.cal7(l,d,x))
        self.men7.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,x='50 Row':self.cal7(l,d,x))
        self.men7.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,x='20 Row':self.cal7(l,d,x))
        self.men7.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,x='10 Row':self.cal7(l,d,x))
        self.men7.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,x='5 Row':self.cal7(l,d,x))
        #This is the popup menu for bar graph plot
        self.men8=Menu(self.top,tearoff=0,bg='black',activebackground='white',activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men8.add_cascade(label='    Choose',state='disabled')
        self.men8.add_command(label='1. 1000 Naira row',command=lambda l=kist,d=h,x='1000 Row':self.cal8(l,d,x))
        self.men8.add_command(label='2. 500 Naira row',command=lambda l=list2,d=h1,x='500 Row':self.cal8(l,d,x))
        self.men8.add_command(label='3. 200  Naira row',command=lambda l=list3,d=h2,x='200 Row':self.cal8(l,d,x))
        self.men8.add_command(label='4. 100 Naira row',command=lambda l=list4,d=h3,x='100 Row':self.cal8(l,d,x))
        self.men8.add_command(label='5. 50 Naira row',command=lambda l=list5,d=h4,x='50 Row':self.cal8(l,d,x))
        self.men8.add_command(label='6. 20 Naira row',command=lambda l=list6,d=h5,x='20 Row':self.cal8(l,d,x))
        self.men8.add_command(label='7. 10 Naira row',command=lambda l=list7,d=h6,x='10 Row':self.cal8(l,d,x))
        self.men8.add_command(label='8. 5 Naira row',command=lambda l=list8,d=h7,x='5 Row':self.cal8(l,d,x))
        self.f5=Frame(self.top)
        self.color='black'
        label=Button(self.f5,text='It worked').pack()
        self.p1=Label(self.f4,text='1000 Naira', font=('blue', self.lf, 'bold'),width=self.ls,bg=self.color,fg='white')
        self.p1.grid(row=0, column=0)
        h10.append(self.p1)
        #this are the  buttons resposible to trigger a function 
        

        self.bu1=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=kist,d=h,w=ent,x=1000:self.cal(l,d,w,x))
        self.bu1.grid(row=1,column=1,ipadx=round(self.width/960))
        self.bu2=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=list2,d=h1,w=ent2,x=500:self.cal(l,d,w,x))
        self.bu2.grid(row=1,column=2,ipadx=round(self.width/960))
        self.bu3=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=list3,d=h2,w=ent3,x=200:self.cal(l,d,w,x))
        self.bu3.grid(row=1,column=3,ipadx=round(self.width/960))
        self.bu4=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=list4,d=h3,w=ent4,x=100:self.cal(l,d,w,x))
        self.bu4.grid(row=1,column=4,ipadx=round(self.width/960))
        self.bu5=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=list5,d=h4,w=ent5,x=50:self.cal(l,d,w,x))
        self.bu5.grid(row=1,column=5,ipadx=round(self.width/960))
        self.bu6=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=list6,d=h5,w=ent6,x=20:self.cal(l,d,w,x))
        self.bu6.grid(row=1,column=6,ipadx=round(self.width/960))
        self.bu7=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=list7,d=h6,w=ent7,x=10:self.cal(l,d,w,x))
        self.bu7.grid(row=1,column=7,ipadx=round(self.width/960))
        self.bu8=Button(self.test9,text='Sum',font=('Time',self.v.get()-2,),
                   width=22,command=lambda l=list8,d=h7,w=ent8,x=5:self.cal(l,d,w,x))
        self.bu8.grid(row=1,column=8,ipadx=round(self.width/960))
        #self.readyfr=Frame(self.test9)
        #self.ready=Label(self.readyfr,text='Ready')
        #self.ready.grid(row=0,column=0)
        #self.readyfr.grid(row=2,column=1)
        
         #size of the entries 
        for i0 in range(len(self.nam)):
            la=Label(self.f3,text=str(i0+1),font=('blue',self.v.get(),'normal'),fg='black',bg='#EBEBE6')
            #sep=ttk.Separator(f3,orient='horizontal')
            #sep.grid(row=i0,column=0,rowspan=2,columnspan=1,sticky='ew')
            la.grid(row=i0,column=0,sticky='w')
            
        
        self.confi=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\configure.png")
        self.cong=ImageTk.PhotoImage(self.confi.resize((round(self.width/7.84),round(self.height/36))))
        self.config=Button(self.test10,image=self.cong,font=('helvectica',5,'bold'),borderwidth=0,bd=0,bg='black',
                           activebackground='#EBEBE6',command=self.bind)
        self.back=Button(self.test10,text='Back',font=('helvectica',self.v.get(),'bold'),bd=2,borderwidth=0,command=second.close)
        self.config.grid(row=1,column=0)
        self.back.grid(row=2,column=0)
       
        for ip in range(50):
            for jp in range(1):
                
                g0= Text(self.f3, font=('blue',self.v.get()+1),bd=1,width=18,height=0,wrap='char',undo=True,autoseparators=True,cursor='arrow',highlightthickness=0)
                g0.grid(row=ip, column=jp+2,sticky='nsew')
                
                Grid.rowconfigure(self.f3,ip,weight=1)
                Grid.columnconfigure(self.f3,jp+2,weight=1)
                #wep=ttk.Separator(self.f3,orient='vertical')
                #wep.grid(row=ip,column=jp+2,sticky='ns')
                list9.append(g0)
                
        """ the for loops are the entries that forms the rows and columns 
        of the cells it's made up of 50 rows and 8 columns"""
        if len(self.names)>0:
           for ir in range(len(self.names)):
              list9[ir].delete(1.0,END)
              
              
              list9[ir].insert(1.0,self.names[ir][0])
              list9[ir].config(state='disabled')
        if len(self.names)==0:
            for ir2 in range(len(list9)):
                list9[ir2].config(state='disabled')
              
       #3except TclError:
           #pass
        
        
        for i in range(50):
            for j in range(1):
                self.g = Text(self.f2, font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                       wrap='char',autoseparators=True,undo=True,cursor='plus',highlightthickness=0)
                self.g.grid(row=i+1, column=j+1)
                Grid.rowconfigure(self.f2,i+1,weight=1)
                Grid.columnconfigure(self.f2,j+1,weight=1)
                wep=ttk.Separator(self.f2,orient='vertical')
                wep.grid(row=i+1,column=j+1,rowspan=2,columnspan=2,sticky='ns')
                kist.append(self.g)
      
        p2=Label(self.f4,text='500 Naira', font=('blue', self.lf, 'bold'),width=self.ls,bg=self.color,fg='blue')
        p2.grid(row=0, column=1)
        h10.append(p2)
        for i2 in range(1, 51):
            g2 = Text(self.f2, font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                       wrap='char',undo=True,cursor='plus',highlightthickness=0)
            g2.grid(row=i2, column=2)
            wep=ttk.Separator(self.f2,orient='vertical')
            wep.grid(row=i2,column=2,rowspan=2,columnspan=2,sticky='ns')
            list2.append(g2)
        p3=Label(self.f4,text='200 Naira', font=('blue', self.lf,'bold'),width=self.ls,bg=self.color,fg='cyan')
        p3.grid(row=0, column=2)
        h10.append(p3)
        for i3 in range(1,51):
            g3=Text(self.f2, font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                    wrap='char',undo=True,cursor='plus',highlightthickness=0)
            g3.grid(row=i3, column=3)
            wep=ttk.Separator(self.f2,orient='vertical')
            wep.grid(row=i3,column=3,rowspan=2,columnspan=2,sticky='ns')
            list3.append(g3)
        p4=Label(self.f4,text='100 Naira', font=('blue', self.lf, 'bold'),width=self.ls,bg=self.color,fg='powder blue')
        p4.grid(row=0, column=3)
        h10.append(p4)
        for i4 in range(1,51):
            g4=Text(self.f2, font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                     wrap='char',undo=True,cursor='plus',highlightthickness=0)    
            g4.grid(row=i4, column=4)
            wep=ttk.Separator(self.f2,orient='vertical')
            wep.grid(row=i4,column=4,rowspan=2,columnspan=2,sticky='ns')
            list4.append(g4)
        p5=Label(self.f4,text='50 Naira', font=('blue', self.lf, 'bold'),width=self.ls,bg=self.color,fg='turquoise')
        p5.grid(row=0, column=4)
        h10.append(p5)
        for i5 in range(1,51):
            g5=Text(self.f2, font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                    wrap='char',undo=True,cursor='plus',highlightthickness=0)
            g5.grid(row=i5, column=5)
            wep=ttk.Separator(self.f2,orient='vertical')
            wep.grid(row=i5,column=5,rowspan=2,columnspan=2,sticky='ns')
            list5.append(g5)
        p6=Label(self.f4,text='20 Naira', font=('blue', self.lf, 'bold'),width=self.ls,bg=self.color,fg='light green')
        p6.grid(row=0, column=5)
        h10.append(p6)
        for i6 in range(1,51):
            g6=Text(self.f2, font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                    wrap='char',undo=True,cursor='plus',highlightthickness=0)
            g6.grid(row=i6, column=6)
            wep=ttk.Separator(self.f2,orient='vertical')
            wep.grid(row=i6,column=6,rowspan=2,columnspan=2,sticky='ns')
            list6.append(g6)
        p7=Label(self.f4,text='10 Naira', font=('blue',self.lf, 'bold'),width=self.ls,bg=self.color,fg='tan')
        p7.grid(row=0, column=6)
        h10.append(p7)
        for i7 in range(1,51):
            g7 = Text(self.f2,font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                                     wrap='char',undo=True,cursor='plus',highlightthickness=0)
            g7.grid(row=i7, column=7)
            wep=ttk.Separator(self.f2,orient='vertical')
            wep.grid(row=i7,column=7,rowspan=2,columnspan=2,sticky='ns')
            list7.append(g7)
        p8=Label(self.f4,text='5 Naira', font=('blue', self.lf, 'bold'),width=self.ls,bg=self.color,fg='pink')
        p8.grid(row=0, column=7)
        h10.append(p8)
       
        for i8 in range(1,51):
            g8 = Text(self.f2, font=('blue',self.v.get()+1),bd=1,width=18,height=0,
                      wrap='char',undo=True,cursor='plus',highlightthickness=0)
            g8.grid(row=i8, column=8)
            #wep=ttk.Separator(self.f2,orient='vertical')
            #wep.grid(row=18,column=8,rowspan=2,columnspan=2,sticky='ns')
            list8.append(g8)
        self.c3.update_idletasks()
        self.c.update_idletasks()
        self.toolbar2.update_idletasks()
        self.toolbar.update_idletasks()
        self.testf.update_idletasks()
        self.testy.update_idletasks()
       
        self.toolbar2.create_window(round(self.width/192),round(self.height/36),anchor='w',window=self.f6)
        self.toolbar.create_window(round(self.width/192),round(self.height/36),anchor='w',window=self.f7)
        self.testy.create_window(round(self.width/13.71),round(self.height/10.3),anchor='s',window=self.test10)
        
        self.testf.create_window(0,0,anchor='s',window=self.test9)
        
        self.toolbar.grid(row=0,column=3,sticky='nsew')
        self.toolbar.grid_propagate(False)
        self.testf.config(scrollregion=self.testf.bbox('all'),xscrollcommand=self.sc.set)
        self.testf.xview_moveto(0.0)
        self.toolbar2.grid(row=0,column=0,sticky='nsew')
        self.toolbar2.grid_propagate(False)
        self.c3.create_window(0,0,anchor='ne',window=self.f4)
        self.c3.config(scrollregion=self.c3.bbox('all'),xscrollcommand=self.sc.set)
        self.c3.xview_moveto(0.0)
        self.c.create_window(0,0,anchor='w',window=self.f2)
        self.c.configure(scrollregion=self.c.bbox('all'),yscrollcommand=self.sc1.set,xscrollcommand=self.sc.set)
        self.testy.grid(row=28,column=0)
        self.testy.grid_propagate(False)
        self.c.grid(row=4,column=3,sticky='nsew')
        self.c.yview_moveto(0.0)
        self.c.xview_moveto(0.0)
        self.c.grid_propagate(False)
        self.c3.grid(row=3,column=3,sticky='nsew')
        self.c3.grid_propagate(False)
        self.c4.grid(row=3,column=0,sticky='nsew')
        self.sc.grid(row=0,column=0,sticky='nsew')
        
        self.testf.grid(row=28,column=3,sticky='nsew')
        self.testf.grid_propagate(False)
        #self.barframe.grid(row=4,column=4,sticky='news')
        self.sc1.grid(row=4,column=4,sticky='nsew')
        
        self.c2.update_idletasks()
        self.c2.create_window(0,0,anchor='w',window=self.f3)
        self.c2.config(scrollregion=self.c2.bbox('all'),yscrollcommand=self.sc1.set)
        self.c2.yview_moveto(0.0)
        self.c2.xview_moveto(0.0)
        self.c2.grid(row=4,column=0,sticky='nsew')
        self.c2.grid_propagate(False)
        
        #Grid.columnconfigure(self.top,0,weight=1)
        Grid.columnconfigure(self.top,3,weight=10)
        
        Grid.rowconfigure(self.top,1,weight=10)
        Grid.rowconfigure(self.top,28,weight=10)
        Grid.rowconfigure(self.top,3,weight=10)
        Grid.rowconfigure(self.top,4,weight=10)
        self.config_themes5()
        
        
        
        
        self.top.after(100,self.forcer)
        self.top.after_idle(self.top.focus_force)
        
        #self.update('e')
        #self.top.update()
       #binding sc horizontal scrollbar to c2 and c
    def verify2(self,input):
        print(input)
    def scroll(self,*args):
        threading.Thread(target=self.c.yview(*args)).start()
        threading.Thread(target=self.c2.yview(*args)).start()
       
    #binding sc2 scrollbar to c and c3
    def scroll1(self,*args):
        threading.Thread(target=self.c.xview(*args)).start()
        threading.Thread(target=self.c3.xview(*args)).start()
        threading.Thread(target=self.testf.xview(*args)).start()
    #binding the up-arrow key to sc scrollbar
    def up(self,e):
        threading.Thread(target=self.c.yview_scroll(-1,'units')).start()
        threading.Thread(target=self.c2.yview_scroll(-1,'units')).start()
    #binding the down-arrow key to sc scrollbar
    def down(self,e):
        threading.Thread(target=self.c.yview_scroll(1,'units')).start()
        threading.Thread(target=self.c2.yview_scroll(1,'units')).start()
    #binding the right arrow key to sc2 scrollbar
    def right(self,e):
        threading.Thread(target=self.c.xview_scroll(1,'units')).start()
        threading.Thread(target=self.c3.xview_scroll(1,'units')).start()
        threading.Thread(target=self.testf.xview_scroll(1,'units')).start()
    #binding the left arrowkkey to sc2 scrollbar
    def left(self,e):
        threading.Thread(target=self.c.xview_scroll(-1,'units')).start()
        threading.Thread(target=self.c3.xview_scroll(-1,'units')).start()
        threading.Thread(target=self.testf.xview_scroll(-1,'units')).start()
    #summation function fuction call
    def cal(self,l,d,w,x):
       w.config(state='normal')
       global count1
       count1+=1
       count=0
       for c in l:
           
           if c.get(1.0,'end-1c').isdigit():
               d.append(int(c.get(1.0,'end-1c')))
       if count1>1:
           w.delete(1.0,'end')
           w.insert(1.0,'{:,} naira'.format(sum(d)*x))
           
       else:
           w.insert(1.0,'{:,} naira'.format(sum(d)*x))
           
       del d[:]
    #averagefunction function call
    def cal2(self,l,d,w,x):
        w.configure(state='normal')
        global count1
        count1+=1
        for c in l:
       
           if c.get(1.0,'end-1c').isdigit():
               d.append(int(c.get(1.0,'end-1c')))
        if count1>1:
           w.delete(1.0,'end')
           w.insert(1.0,'Avr {:,.2f} Naira'.format((sum(d)/len(d))*x))
           
        else:
           w.insert(1.0,'Avr {:,.2f} Naira'.format((sum(d)/len(d))*x))
           
        del d[:]
    #rankfunction function call
    def cal3(self,l,d,x):
        
        
        global count1
        count1+=1
        for c in l:
            test.append(c.get(1.0,'end-1c'))
            if c.get(1.0,'end-1c').isdigit():
                d.append(int(c.get(1.0,'end-1c')))
                
        d.sort()
        self.d=d[::1]
        self.display(x)
        del d[:]
        del test[:]
    #minfuntion function call
    def cal4(self,l,d,w):
        w.configure(state='normal')
        global count1
        count1+=1
        for c in l:
            test.append(c.get(1.0,'end-1c'))
            if c.get(1.0,'end1-1c').isdigit():
                d.append(int(c.get(1.0,'end-1c')))
        if count1>1:
                w.delete(1.0,'end')
                w.insert(1.0,'Min {}'.format(min(d)))
        else:
                w.insert(1.0,'Min {}'.format(min(d)))
        del d[:]
    #maxfunction function call
    def cal5(self,l,d,w):
        
        w.configure(state='normal')
        global count1
        count1+=1
        for c in l:
            test.append(c.get())
            if c.get(1.0,'end-1c').isdigit():
                d.append(int(c.get(1.0,'end-1c')))
        if count1>1:
                w.delete(1.0,'end')
                w.insert(1.0,'Max {}'.format(max(d)))
        else:
                w.insert(1.0,'Max {}'.format(max(d)))
        del d[:]
    def cal6(self,l,d,x):
        top6=Toplevel(self.top)
        top6.attributes('-toolwindow',True)
        top6.iconphoto(False,self.j2)
        top6.resizable(1,0)
        size=plt.figure(figsize=(7,8),dpi=100)
        for c in l:
            if c.get(1.0,'end-1c').isdigit():
                d.append(int(c.get(1.0,'end-1c')))
       
        plot1=size.add_subplot(111)     
        plot1.plot(d)
        graph_canvas=FigureCanvasTkAgg(size,top6)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().pack()
        tool=NavigationToolbar2Tk(graph_canvas,top6)
        tool.update()
        plt.xlabel('x-axis')
        plt.ylabel('{} ({})'.format('y-axis',x+' '+'entries'))
        plt.title(x)
        
        graph_canvas.get_tk_widget().pack()
        del d[:]
    def cal7(self,l,d,x):
        top6=Toplevel(self.top)
        top6.attributes('-toolwindow',True)
        top6.iconphoto(False,self.j2)
        top6.resizable(1,0)
        size=plt.figure(figsize=(7,8),dpi=100)
        for c in l:
            if c.get(1.0,'end-1c').isdigit():
                d.append(int(c.get(1.0,'end-1c')))
        for i in range(len(d)):
            graph.append(i)
        plot1=size.add_subplot(111)
        plot1.cla()
        plot1.scatter(graph,d)
        graph_canvas=FigureCanvasTkAgg(size,top6)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().pack()
        tool=NavigationToolbar2Tk(graph_canvas,top6)
        tool.update()
        plt.xlabel('x-axis')
        plt.ylabel('{} ({})'.format('y-axis',x+' '+'entries'))
        plt.title(x)
        
        graph_canvas.get_tk_widget().pack()
        del d[:]
        del graph[:]
    def cal8(self,l,d,x):
        top6=Toplevel(self.top)
        top6.attributes('-toolwindow',True)
        top6.iconphoto(False,self.j2)
        top6.resizable(1,0)
        size=plt.figure(figsize=(7,8),dpi=100)
        for c in l:
            if c.get(1.0,'end-1c').isdigit():
                d.append(int(c.get(1.0,'end-1c')))
        for i in range(len(d)):
            graph.append(i)
        plot1=size.add_subplot(111)
        plot1.cla()
        plot1.bar(graph,d,width=0.7)
        graph_canvas=FigureCanvasTkAgg(size,top6)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().pack()
        tool=NavigationToolbar2Tk(graph_canvas,top6)
        tool.update()
        plt.xlabel('x-axis')
        plt.ylabel('{} ({})'.format('y-axis',x+' '+'entries'))
        plt.title(x)
        
        graph_canvas.get_tk_widget().pack()
        del d[:]
        del graph[:]
    #display of the listbox containing the ranks
    def display(self,x):
        self.top2=Toplevel(self.top)
        self.top2.iconphoto(False,self.j2)
        self.top2.title('Financial Analysis')
        self.top2.resizable(0,0)
        self.top2.attributes('-toolwindow',True)
        
        self.box=Listbox(self.top2)
        self.scr2=Scrollbar(self.top2,orient='horizontal',command=self.box.xview)
        self.scro=Scrollbar(self.top2,orient='vertical',command=self.box.yview)
        lab=Label(self.top2,text=x,bg='black',fg='white',width=20).grid(row=0,column=0,sticky='n')
        self.se=IntVar()
        self.se.set(1)
        self.asc=Radiobutton(self.top2,text='Ascending',bd=0,borderwidth=0,var=self.se,value=1,command=self.display2)
        self.dec=Radiobutton(self.top2,text='Descending',bd=0,borderwidth=0,var=self.se,value=2,command=self.display2)
        for i in range(len(self.d)):
               self.box.insert(END,'{}'.format('(')+str(i+1)+'{}'.format(')')+' '+str(self.d[i]))
        self.asc.grid(row=2,sticky='s')
        self.dec.grid(row=3,stick='s')
        self.box.grid(row=0,column=0,sticky='n',pady=30)
        self.box.config(yscrollcommand=self.scro.set,xscrollcommand=self.scr2.set)
        self.scro.grid(row=0,column=2,sticky='ns',pady=30)
        self.scr2.grid(row=1,sticky='ew')
    #Radiobuutons command to change the sequence of the ranks i.e ascending or descending order
    def display2(self):
         if self.se.get()==1:
            self.box.delete(0,END)
            for i in range(len(self.d)):
               self.box.insert(END,'{}'.format('(')+str(i+1)+'{}'.format(')')+' '+str(self.d[i]))
    
         if self.se.get()==2:
             self.box.delete(0,END)
             for i in range(len(self.d)):
               self.box.insert(0,'{}'.format('(')+str(len(self.d)-(i))+'{}'.format(')')+' '+str(self.d[i]))
    #popmenu function for the sum fuction
    def sum(self):
        x=self.men.winfo_pointerx()
        y=self.men.winfo_pointery()
        try:
            self.men.tk_popup(x,y,0)
        finally:
            self.men.grab_release()
    #popupmenu function for the average function
    def average(self):
        x=self.men2.winfo_pointerx()
        y=self.men2.winfo_pointery()
        try:
            self.men2.tk_popup(x,y,0)
        finally:
            self.men2.grab_release()
    #popupmenu function for the rank funtion
    def rank(self):
         x=self.men3.winfo_pointerx()
         y=self.men3.winfo_pointery()
         try:
            self.men3.tk_popup(x,y,0)
         finally:
            self.men3.grab_release()
    #popupmenu for the min fuction
    def min(self):
         x=self.men4.winfo_pointerx()
         y=self.men4.winfo_pointery()
         try:
            self.men4.tk_popup(x,y,0)
         finally:
            self.men4.grab_release()
    #popupmenu function for the max function
    def max(self):
         x=self.men5.winfo_pointerx()
         y=self.men5.winfo_pointery()
         try:
            self.men5.tk_popup(x,y,0)
         finally:
            self.men5.grab_release()
    #poopup menu for the basic graph function
    def graph(self):
        x=self.men6.winfo_pointerx()
        y=self.men6.winfo_pointery()
        try:
           self.men6.tk_popup(x,y,0)
        finally:
            self.men6.grab_release()
    #popupmenu for the scatter graph plot function
    def graph2(self):
        x=self.men7.winfo_pointerx()
        y=self.men7.winfo_pointery()
        try:
           self.men7.tk_popup(x,y,0)
        finally:
            self.men7.grab_release()
    #popup menu for the bar graph menu function
    def graph3(self):
        x=self.men8.winfo_pointerx()
        y=self.men8.winfo_pointery()
        try:
           self.men8.tk_popup(x,y,0)
        finally:
            self.men8.grab_release()
    # Template creation function
    def create(self):
        self.c4.grid_remove()
        self.back.grid_remove()
        self.config.grid_remove()
        #Template name Entry
        self.entry=Entry(self.top,)
        self.entry.insert(0,'New_Template')
        self.terminate=Button(self.top,text='X')
        
        self.entry.select_range(0,'end')
        self.entry.focus_set()
        self.entry.grid(row=3,column=0)
        self.entry.bind('<Escape>',self.load3)
        for i in range(len(list9)):
            threading.Thread(target=list9[i].config(state='normal')).start()
            threading.Thread(target=list9[i].delete(1.0,'end')).start()
        self.xc1=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\clear.png")
        self.xc1=self.xc1.resize((round(self.width/7.68),round(self.height/29.19)))
        self.xc1=ImageTk.PhotoImage(self.xc1)
        self.yc1=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\savet.png")
        self.yc1=self.yc1.resize((round(self.width/7.68),round(self.height/29.19)))
        self.yc1=ImageTk.PhotoImage(self.yc1)
        
        try:
          #Clear all button to erase all names
          self.cle1=Button(self.test10,image=self.xc1,borderwidth=0,bd=0,bg='grey')
          self.sav1=Button(self.test10,image=self.yc1,borderwidth=0,bd=0,command=self.create2)
          self.cle1.grid(row=2,column=0,sticky='s')
          self.sav1.grid(row=3,column=0,sticky='s')
          self.ted.entryconfig('Create',state='disabled')
          self.ted.entryconfig('Edit',state='disabled')
          self.ted.entryconfig('Delete',state='disabled')
          self.ted.entryconfig('Load',state='disabled')
          
        finally:
            self.ted.entryconfig('Create',label='Please Save The Template')
        self.config_themes8()
    def load3(self,event):
          data=sqlite3.connect('data.db')
          connet=data.cursor()
          names=connet.execute("SELECT cells FROM {}".format(self.template.cget('text'))).fetchall()
          for i in range(len(names)):
            
                list9[i].config(state='normal')
                list9[i].delete(1.0,'end')
                list9[i].insert(1.0,names[i][0])
                list9[i].config(state='disabled')
          self.entry.grid_forget()
          self.cle1.grid_forget()
          self.sav1.grid_forget()
          self.c4.grid()
          self.config.grid()
          self.back.grid()
          self.ted.entryconfig('Please Save The Template',state='normal',label='Create')
          self.ted.entryconfig('Edit',state='normal')
          
          self.ted.entryconfig('Delete',state='normal')
          self.ted.entryconfig('Load',state='normal')  
    def tryer(self,event):
        self.frame.place(x=self.bi,y=self.bii)
        print(self.bi,self.bii,'gh')
        threading.Thread(target=self.frame.config(width=event.x,height=event.y)).start()
        self.top.bind('<ButtonPress-1>',self.do)
        print(self.frame.cget('width'),self.frame.cget('height'))
        #curx,cury=(event.x,event.y)
        #self.testy.coords(self.rect,self.widget_drag1,self.widget_drag2,curx,cury)
        #if self.resize:
        #    if self.resize and self.hori:
        #        self.frame.config(width=event.x)
        #    if self.resize and self.vert:
        #        self.frame.config(height=event.y)
        #else:
        #    cursor='size' if self.do2(event.x,event.y) else ''
        #    if cursor!=self.cursor:
        #        self.frame.config(cursor=cursor)
    #def tryer1(self,event):
    #     pass
    #def tryer(self,event):
    #    u=event.widget
    #    x=u.winfo_x()-self.widget_drag1+event.x
    #   y=u.winfo_y()-self.widget_drag2+event.y
    #    #u.place(x=x,y=y)
    #    u=event.widget.winfo_containing(event.x_root,event.y_root)
        
    #    if isinstance(u,Text):
            
    #        w,h=self.c.winfo_width(),self.c.winfo_height()
    #        print(w,h)
    #        print(event.y,'j')
    #        self.top.bind('<ButtonPress-1>',self.do)
    #        #self.top.bind('<keyP')
    #        if event.x>round(0.9*w):
    #            threading.Thread(target=self.c.xview_scroll(1,'units')).start()
    #            threading.Thread(target=self.c3.xview_scroll(1,'units')).start()
    #            threading.Thread(target=self.testf.xview_scroll(1,'units')).start()
    #            threading.Thread(target=u.config(bg='#EBA7A7')).start()
    #        elif event.x<round(0.9*w):
                
    #            threading.Thread(target=self.c.xview_scroll(-1,'units')).start()
    #            threading.Thread(target=self.c3.xview_scroll(-1,'units')).start()
    #            threading.Thread(target=self.testf.xview_scroll(-1,'units')).start()
    #            threading.Thread(target=u.config(bg='#EBA7A7')).start()
    #        if event.y>round(0.9*h):
    #            threading.Thread(target=self.c.yview_scroll(1,'units')).start()
    #            threading.Thread(target=self.c2.yview_scroll(1,'units')).start()
    #            threading.Thread(target=u.config(bg='#EBA7A7')).start()
    #        elif event.y<round(0.9*h):
    #            threading.Thread(target=self.c.yview_scroll(-1,'units')).start()
    #            threading.Thread(target=self.c2.yview_scroll(-1,'units')).start()
    #            threading.Thread(target=u.config(bg='#EBA7A7')).start()
    #        lgh.append(u)


    def do(self,event):
        self.frame.place_forget()
        self.top.bind('<ButtonPress-1>',self.tryer1)
           
    def do2(self,x,y):
        wid,hei=self.frame.cget('width'),self.frame.cget('height')
        mode=0
        if x>wid-10: mode|=self.hori
        if y>hei-10: mode|=self.vert
        return mode

    def tryer1(self,event):
        self.hori=1
        self.vert=2
        self.resize=0
        self.cursor=''
        widget=event.widget
        if isinstance(widget,Text):
             self.bi=event.x_root
             self.bii=event.y_root
             self.top.bind('<B1-Motion>',self.tryer)
        self.widget_drag1=event.x
        self.widget_drag2=event.y
       
        #self.rect=self.testy.create_rectangle(0,0,1,1, fill='brown')
        self.frame=Canvas(self.top,bd=0,relief='raised',bg='brown',width=100,height=100)
        #self.do2(self.widget_drag1,self.widget_drag2)
        

    #Template creation checker   
    def create2(self):
        checkers=[]
        print(len(self.entry.get()))
        #to check whether the template name is empty
        if len(self.entry.get())==0:
            self.error=showerror('Name Null','Template Name Null')
        # to check wheather the tempate name is purely numbers
        elif self.entry.get().isdigit():
            self.error2=showerror("Name Null","Template Name\nCan't be Number")
        #if it none of the above
        else:
        #opening of the data base
          try:
            data=sqlite3.connect('data.db')
            connet=data.cursor()
            res=connet.execute("SELECT name FROM sqlite_master WHERE type='table' ").fetchall()
          # if there are no raised errors like table name already exist
         
            connet.execute("""CREATE TABLE {}(cells TEXT,row1 TEXT,row2 TEXT,
            row3 TEXT,row4 TEXT,row5 TEXT,row6 TEXT,row7 TEXT,row8 text)""".format(self.entry.get()))
            for i in range(len(list9)):
                            connet.execute("INSERT INTO {}(cells) VALUES('{}')".format(self.entry.get(),list9[i].get(1.0,'end')))
                            list9[i].config(state='disabled')
            self.entry.grid_forget()
            self.cle1.grid_forget()
            self.sav1.grid_forget()
            self.c4.grid()
            self.config.grid()
            self.back.grid()
            self.ted.entryconfig('Please Save The Template',state='normal',label='Create')
            self.ted.entryconfig('Edit',state='normal')
          
            self.ted.entryconfig('Delete',state='normal')
            self.ted.entryconfig('Load',state='normal')
            with open('loader.pk', 'wb') as f2:
               self.data2=pickle.dump(self.entry.get(),f2)
            self.template.config(text=self.entry.get())
            data.commit()
            data.close()
          #if there is any error it raises a message box with confirmation wheather there should be overwritten of the table name
          except sqlite3.OperationalError:
             threading.Thread(target=PlaySound('SystemQuestion',SND_ASYNC)).start()
             
             self.top12=Toplevel(self.top)
             self.top12.resizable(0,0)
             self.top12.attributes('-toolwindow',True)
             self.top12.protocol('WM_DELETE_WINDOW',lambda:threading.Thread(target=PlaySound('SystemQuestion',SND_ASYNC)).start())
             self.topframe=Frame(self.top12)
             self.question=Label(self.topframe,text="Name '{}'  Already Exists.\nDo You  Want To Overwrite".format(self.entry.get()))
             self.question.grid(row=0,column=0)
             self.yes=Button(self.topframe,text='Yes',command=lambda answer='yes':self.message(answer))
             self.yes.grid(row=1,column=0)
             self.top12.bind('<Button-1>',self.flash)
             self.top12.bind('<ButtonPress-1>',self.flash)
             self.top12.bind('<Button-2>',self.flash)
             self.top12.bind('<ButtonPress-2>',self.flash)
             self.top12.bind('<Button-3>',self.flash)
             self.top12.bind('<Button-4>',self.flash)
             self.top12.bind('<Button-5>',self.flash)
             self.no=Button(self.topframe,text='No',command=lambda answer='no':self.message(answer))
             self.no.grid(row=1,column=1,padx=10)
             self.top12.grab_set()
             self.topframe.grid(row=0)
             self.top12.focus_force()
             
                
            
    #warning sound if try to shift focus away from the messagebox             
    def flash(self,event):
           try:
            if event.widget==self.top12:
               self.top12.bell()
           except AttributeError:
              if event.widget==self.top17:
               self.top17.bell()
            
    #messagebox function to achieve the overwritting       
    def message(self,answer):
        
        if answer=='yes':
          try:
            data=sqlite3.connect('data.db')
            connet=data.cursor()
            self.top12.grab_release()
            self.top12.destroy()
            connet.execute("DROP TABLE {}".format(self.entry.get()))
            connet.execute("""CREATE TABLE {}(cells TEXT,row1 TEXT,row2 TEXT,row3 TEXT,
                row4 TEXT,row5 TEXT,row6 TEXT,row7 TEXT,row8 text)""".format(self.entry.get()))
            
            for i in range(len(list9)):
                            connet.execute("INSERT INTO {}(cells) VALUES('{}')".format(self.entry.get(),list9[i].get(1.0,'end')))
                            list9[i].config(state='disabled')
            self.entry.grid_forget()
            self.c4.grid()
            self.cle1.grid_forget()
            self.sav1.grid_forget()
            self.back.grid()
            self.config.grid()
            self.ted.entryconfig('Please Save The Template',state='normal',label='Create')
            self.ted.entryconfig('Create',state='normal')
            self.ted.entryconfig('Delete',state='normal')
            self.ted.entryconfig('Load',state='normal')
            self.ted.entryconfig('Edit',state='normal')
            with open('loader.pk', 'wb') as f2:
               self.data2=pickle.dump(self.entry.get(),f2)
               f2.close()
            with open('loader.pk','rb') as f2:
                  data3=pickle.load(f2)
            self.template.config(text=data3)
            data.commit()
            data.close()
          except AttributeError:
            data=sqlite3.connect('data.db')
            connet=data.cursor()
            self.top17.grab_release()
            self.top17.destroy()
            connet.execute("DROP TABLE {}".format(self.entry2.get()))
           
            
            
            connet.execute("""CREATE TABLE {}(cells TEXT,row1 TEXT,row2 TEXT,row3 TEXT,
                row4 TEXT,row5 TEXT,row6 TEXT,row7 TEXT,row8 text)""".format(self.entry2.get()))
            
            for i in range(len(list9)):
                            connet.execute("INSERT INTO {}(cells) VALUES('{}')".format(self.entry2.get(),list9[i].get(1.0,'end')))
                            list9[i].config(state='disabled')
            
            self.cle2.grid_forget()
            self.sav2.grid_forget()
            self.entry2.grid_forget()
            self.c4.grid()
            self.back.grid()
            self.config.grid()
            self.ted.entryconfig('Please Save The Template',state='normal',label='Edit')
            self.ted.entryconfig('Create',state='normal')
            self.ted.entryconfig('Delete',state='normal')
            self.ted.entryconfig('Load',state='normal')
            with open('loader.pk', 'wb') as f2:
               self.data2=pickle.dump(self.entry2.get(),f2)
               f2.close()
            connet.execute("DROP TABLE {}".format(self.value[self.value.index('  ')+2:]))
            with open('loader.pk','rb') as f2:
                  data3=pickle.load(f2)
            self.template.config(text=data3)
            data.commit()
            data.close()

        if answer=='no':
           try:
            self.entry.focus_set()
            self.top12.grab_release()
            self.top12.destroy()
           except AttributeError:
               self.entry2.focus_set()
               self.top17.grab_release()
               self.top17.destroy()
    #load function to load already created templates
    def load(self):
        self.top13=Toplevel(self.top)
        self.top13.protocol('WM_DELETE_WINDOW',self.burst)
        mwidth=self.top13.winfo_screenwidth()
        mheight=self.top13.winfo_screenheight()
        xwidth1=round(mwidth/2.3)
        yheight1=round(mheight/2.3)
        self.top13.geometry('{}x{}+{}+{}'.format(xwidth1,yheight1,round((mwidth/2)-(xwidth1/2)),round((mheight/2)-(yheight1/2))))
        self.top13.resizable(0,0)
        
        self.top13.grab_set()
        self.top13.attributes('-toolwindow',True)
        data=sqlite3.connect('data.db')
        connet=data.cursor() 
        style=ttk.Style()
        style.configure('mystyle.Treeview',highlightthickness=0,bd=0,font=('Calibri',11),rowheight=35,)
        style.configure('mystyle.Treeview.Heading',font=('Calibri',13,'bold'))
        style.layout('mystyle.Treeview',[('mystyle.Treeview.treearea',{'sticky':'nswe'})],)
        style.configure('mystyle.Treeview',background='black')
        images=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\templ.png")
        images=images.resize((25,25))
        images=ImageTk.PhotoImage(images)
        self.loadframe=Frame(self.top13)
        #listbox that contains the template names
        self.loadlist=ttk.Treeview(self.loadframe,columns=('#0','#1','#2'),style='mystyle.Treeview')
        self.loadlist.heading('#0',text='Names',anchor='center')
        self.loadlist.heading('#1',text='Date Created',anchor='center')
        self.loadlist.heading('#2',text='Last Modified',anchor='center')
        self.loadlist.column('#0',minwidth=300,width=300)
        self.loadlist.column('#1',minwidth=190,width=190)
        self.loadlist.column('#2',minwidth=190,width=190)
        self.loadscroll=Scrollbar(self.loadframe,orient='horizontal')
        self.loadscroll1=Scrollbar(self.loadframe,orient='vertical')
        res=connet.execute("SELECT name FROM sqlite_master WHERE type='table' ").fetchall()
        for i in range(len(res)):
            self.loadlist.insert('',f'{i}',f'{i}',text=('{}'.format(res[i][0])),values=(0,10),image=images)
            self.loadlist.images=images
        self.loadlist.grid(row=0,column=0)
        self.loadscroll.config(command=self.loadlist.xview)
        self.loadscroll1.config(command=self.loadlist.yview)
        self.loadscroll.grid(row=1,column=0,sticky='ew')
        self.loadscroll1.grid(row=0,column=2,sticky='ns')
        self.loadlist.config(xscrollcommand=self.loadscroll.set,yscrollcommand=self.loadscroll1.set)
        self.loadlist.grid_propagate(False)
        
        
        self.loadlist.focus_set()
        self.top13.bind('<Button-1>',self.flash2)
        self.top13.bind('<ButtonPress-1>',self.flash2)
        self.top13.bind('<Button-2>',self.flash2)
        self.top13.bind('<ButtonPress-2>',self.flash2)
        self.top13.bind('<Button-3>',self.flash2)
        self.top13.bind('<Button-4>',self.flash2)
        self.top13.bind('<Button-5>',self.flash2)
        self.loadframe.grid(row=0,column=0)
        with open('loader.pk','rb') as f2:
                  data3=pickle.load(f2)
                  
        
        
        #indexer=list(self.loadlist.get(0,'end')).index('{}  {}'.format('::::',data3,))
        
        #self.loadlist.selection_set(indexer)
        #self.loadlist.see(indexer)
        #listbox selection binding
        self.loadlist.bind('<<TreeviewSelect>>',self.load2)
        self.loadlist.bind('<Button-3>',self.popup)
    #load listbox selection function
    def load2(self,event):
        try:
          self.top13.grab_set()
          sel=self.loadlist.selection()
          if sel:
              selc=self.loadlist.item(sel)
              self.value=selc['text']
              print(selc['text'])

        except AttributeError:
             sel=self.loadlist.selection()
             self.value=self.loadlist.get(sel[0])
        
        with open('loader.pk', 'wb') as f2:
               self.data2=pickle.dump(self.value,f2)
               f2.close()
        
        data=sqlite3.connect('data.db')
        connet=data.cursor()
        names=connet.execute("SELECT cells FROM {}".format(self.value)).fetchall()
        #if the length of the template is 0 it ask to edit the template 
        if len(names)==0:
             self.top13.grab_release()
             threading.Thread(target=self.top13.bell).start()
             self.top14=Toplevel(self.top)
             self.top14.resizable(0,0)
             self.top14.focus_force()
             self.top14.grab_set()
             self.top14.attributes('-toolwindow',True)
             self.top14.title('Name Null')
             self.top14.protocol('WM_DELETE_WINDOW',self.erexit)
             self.topframe2=Frame(self.top14)
             self.question1=Label(self.topframe2,text="Template ({}) is empty, Do You Wish to Edit? ".format(self.value))
             self.question1.grid(row=0,column=0)
             self.yes1=Button(self.topframe2,text='Yes',command=lambda answer='yes',answer2='null':self.message2(answer,answer2))
             self.yes1.grid(row=1,column=0)
             self.top14.bind('<Button-1>',self.flash3)
             self.top14.bind('<ButtonPress-1>',self.flash3)
             self.top14.bind('<Button-2>',self.flash3)
             self.top14.bind('<ButtonPress-2>',self.flash3)
             self.top14.bind('<Button-3>',self.flash3)
             self.top14.bind('<Button-4>',self.flash3)
             self.top14.bind('<Button-5>',self.flash3)
             self.no1=Button(self.topframe2,text='No',command=lambda answer='no',answer2='null':self.message2(answer,answer2))
             self.no1.grid(row=1,column=1,padx=3)
             
             self.topframe2.grid(row=0)
             
            
        else:
          self.top13.grab_set()
          for i in range(len(names)):
            
            list9[i].config(state='normal')
            list9[i].delete(1.0,'end')
            list9[i].insert(1.0,names[i][0])
            list9[i].config(state='disabled')
    ##exiting the confirmation messagebox
    def burst(self):
        with open('loader.pk','rb') as f2:
                  data3=pickle.load(f2)
        self.template.config(text=data3)
        self.top.focus_force()
        self.top13.grab_release()
        self.top13.destroy()
    def erexit(self):
        self.top14.destroy()
        self.top13.grab_set()
    #warning sound if tried to shift focus away from the messagebox
    def flash2(self,event):
            if self.top13.winfo_containing(event.x_root,event.y_root)!=self.top13 and event.widget!=self.loadscroll1 and event.widget!=self.loadscroll and event.widget!=self.loadlist:
               self.top13.bell() 
   #warning sound if tried to shift focus away from the messagebox
    def flash3(self,event):
         try:
           if event.widget==self.top14:
               self.top14.bell()
         except:
             if event.widget==self.top18:
               self.top18.bell()
    #fuction to achieve the answers to edit or not
    def message2(self,answer,answer2):
      if answer=='no':
         self.top14.grab_release()
         self.top14.destroy()
         self.top13.grab_set()
         self.top13.focus_force()
      if answer=='yes':
        try:
          self.top.focus_force()
          self.top14.grab_release()
          self.top14.destroy()
          self.top13.destroy()
        except AttributeError:
          self.top.focus_force()
          
          
          self.top13.destroy()
        data=sqlite3.connect('data.db')
        connet=data.cursor()
        names=connet.execute("SELECT cells FROM {}".format(self.value)).fetchall()
        self.c4.grid_remove()
        self.back.grid_remove()
        self.config.grid_remove()
        self.entry2=Entry(self.top,)
        self.entry2.insert(0,self.value)
        self.entry2.select_range(0,'end')
        self.entry2.focus_set()
        self.entry2.grid(row=3,column=0)
        
        for ik in range(len(names)):
            
            list9[ik].config(state='normal')
            list9[ik].delete(1.0,'end')
            list9[ik].insert(1.0,names[ik][0])
            list9[ik].config(state='disabled')
        for i in range(len(list9)):
            threading.Thread(target=list9[i].config(state='normal')).start()
            
        self.xc2=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\clear.png")
        self.xc2=self.xc2.resize((round(self.width/7.68),round(self.height/29.19)))
        self.xc2=ImageTk.PhotoImage(self.xc2)
        self.yc2=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\savet.png")
        self.yc2=self.yc2.resize((round(self.width/7.68),round(self.height/29.19)))
        self.yc2=ImageTk.PhotoImage(self.yc2)
        
        try:
          
          self.cle2=Button(self.test10,image=self.xc2,borderwidth=0,bd=0,bg='grey')
          self.sav2=Button(self.test10,image=self.yc2,borderwidth=0,bd=0,command=self.edit2)
          self.cle2.grid(row=2,column=0,sticky='s')
          self.sav2.grid(row=3,column=0,sticky='s')
          self.ted.entryconfig('Edit',state='disabled')
          self.ted.entryconfig('Create',state='disabled')
          self.ted.entryconfig('Delete',state='disabled')
          self.ted.entryconfig('Load',state='disabled')
          
        finally:
            self.ted.entryconfig('Edit',label='Please Save The Template')
        

    #saving the template which was edited
    def edit2(self):
      data=sqlite3.connect('data.db')
      connet=data.cursor()
      confirm=connet.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(self.entry2.get())).fetchone()
      #testing wheather if there are errors
      try:
        #testing wheather the name is empty
        if len(self.entry2.get())==0:
            self.error6=showerror('Name Null','Template Name Null')
        #Testing wheter the name is number
        elif self.entry2.get().isdigit():
            self.error7=showerror("Name Null","Template Name\nCan't be Number")
        #testing wheather there the template highlighted match with the one inside the database if any changes is done to the previous name
        #Also if the name edited match with any table name on the database it raises an error to overwrite the table or not
        elif confirm[0]!=self.value[self.value.index('  ')+2:] and len(confirm)>0:
             self.top17=Toplevel(self.top)
             self.top17.resizable(0,0)
             self.top17.attributes('-toolwindow',True)
             self.top17.protocol('WM_DELETE_WINDOW',lambda:threading.Thread(target=PlaySound('SystemQuestion',SND_ASYNC)).start())
             self.topframe2=Frame(self.top17)
             self.question3=Label(self.topframe2,text="Name '[{}]'  Already Exists.\nClick [Yes] To overwrite, Click [No] To Cancel".format(self.entry2.get()))
             self.question3.grid(row=0,column=0)
             self.yes3=Button(self.topframe2,text='Yes',command=lambda answer='yes':self.message(answer))
             self.yes3.grid(row=1,column=0)
             self.top17.bind('<Button-1>',self.flash)
             self.top17.bind('<ButtonPress-1>',self.flash)
             self.top17.bind('<Button-2>',self.flash)
             self.top17.bind('<ButtonPress-2>',self.flash)
             self.top17.bind('<Button-3>',self.flash)
             self.top17.bind('<Button-4>',self.flash)
             self.top17.bind('<Button-5>',self.flash)
             self.no3=Button(self.topframe2,text='No',command=lambda answer='no':self.message(answer))
             self.no3.grid(row=1,column=1,padx=10)
             self.top17.grab_set()
             self.topframe2.grid(row=0)
             self.top17.focus_force()
        #if the table does exists like no changes made to the name of the template   
        else:
          
          
          
          
            connet.execute("DELETE FROM {}".format(self.entry2.get()))
            for i in range(len(list9)):
                            connet.execute("INSERT INTO {}(cells) VALUES('{}')".format(self.entry2.get(),list9[i].get(1.0,'end')))
                            list9[i].config(state='disabled')
            self.entry2.grid_forget()
            self.cle2.grid_forget()
            self.sav2.grid_forget()
            self.c4.grid()
            self.config.grid()
            self.back.grid()
            self.ted.entryconfig('Please Save The Template',state='normal',label='Edit')
            self.ted.entryconfig('Edit',state='normal')
            self.ted.entryconfig('Create',state='normal')
            self.ted.entryconfig('Delete',state='normal')
            self.ted.entryconfig('Load',state='normal')
            with open('loader.pk','rb') as f2:
                  data3=pickle.load(f2)
            self.template.config(text=data3)
            data.commit()
            data.close()
          
          
      #deleting the previous table if the name has been changed to a new one that 
      #is not on the database before in the database automatically     
      except TypeError:
             
            data=sqlite3.connect('data.db')
            connet=data.cursor()
            #deleting the table which once formally selcted to be deleted while the name has been changed to a new one
            connet.execute("DROP TABLE {}".format(self.value[self.value.index('  ')+2:]))
            connet.execute("""CREATE TABLE {}(cells TEXT,row1 TEXT,row2 TEXT,row3 TEXT,
                row4 TEXT,row5 TEXT,row6 TEXT,row7 TEXT,row8 text)""".format(self.entry2.get()))
            
            for i in range(len(list9)):
                            connet.execute("INSERT INTO {}(cells) VALUES('{}')".format(self.entry2.get(),list9[i].get(1.0,'end')))
                            list9[i].config(state='disabled')
            self.entry2.grid_forget()
            self.c4.grid()
            self.cle2.grid_forget()
            self.sav2.grid_forget()
            self.back.grid()
            self.config.grid()
            self.ted.entryconfig('Please Save The Template',state='normal',label='Edit')
            self.ted.entryconfig('Create',state='normal')
            self.ted.entryconfig('Delete',state='normal')
            self.ted.entryconfig('Load',state='normal')
            with open('loader.pk', 'wb') as f2:
               self.data2=pickle.dump(self.entry2.get(),f2)
            
            self.template.config(text=self.entry2.get())
            data.commit()
            data.close()
    def flash4(self,event):
            if event.widget==self.top16:
               self.top16.bell()
    #confirming the message box answers of deletion of templates
    def message3(self,answer):
        #if the answer is yes it droped the table from the database and remove the listbox and activate the upper table(Template)
        if answer=='yes':
            
            data=sqlite3.connect('data.db')
            connet=data.cursor()
            self.top18.grab_release()
            self.top18.destroy()
            connet.execute("DROP TABLE {}".format(self.value[self.value.index('  ')+2:]))
            indexer=list(self.loadlist.get(0,'end')).index('{}  {}'.format('::::',self.value[self.value.index('  ')+2:],))
            self.loadlist.delete(indexer)
            
            try:
              indexe=self.loadlist.get(indexer-1)
         
               
          
              #pickling the upper template for loading references
              with open('loader.pk', 'wb') as f2:
                   self.data2=pickle.dump(self.value[indexe.index('  ')+2:],f2)
                   f2.close()
             
              self.loadlist.selection_clear(0,'end')
              self.loadlist.selection_set(indexer-1)
              self.loadlist.see(indexer-1)
              self.loadlist.activate(indexer-1)
              self.loadlist.selection_anchor(indexer-1)
              #calling the load2 fuction to activate the upper template
              self.load2('l')
              
              data.commit()
              data.close()
              self.top13.grab_set()
            except ValueError:
              indexe=self.loadlist.get(0)
         
              
          
              #pickling the upper template for loading references
              with open('loader.pk', 'wb') as f2:
                   self.data2=pickle.dump(self.value[indexe.index('  ')+2:],f2)
                   f2.close()
            
              self.loadlist.selection_clear(0,'end')
              self.loadlist.selection_set(0)
              self.loadlist.see(0)
              self.loadlist.activate(0)
              self.loadlist.selection_anchor(0)
              #calling the load2 fuction to activate the upper template
              self.load2('l')
              data.commit()
              data.close()
              self.top13.grab_set()
            
        if answer=='no':
            
            self.top18.grab_release()
            self.top18.destroy()
            self.top13.grab_set()
    #deletion fuction when clicked
    def delete(self):
        
             self.top18=Toplevel(self.top)
             self.top18.bell()
             self.top18.resizable(0,0)
             self.top18.attributes('-toolwindow',True)
             self.top18.protocol('WM_DELETE_WINDOW',lambda:threading.Thread(target=PlaySound('SystemQuestion',SND_ASYNC)).start())
             self.topframe3=Frame(self.top18)
             self.question4=Label(self.topframe3,
                                  text="Do You Want To Proceed To Delete The Template ({}).\nClick [Yes] To overwrite, Click [No] To Cancel".format(self.value[self.value.index('  ')+2:]))
             self.question4.grid(row=0,column=0)
             self.yes4=Button(self.topframe3,text='Yes',command=lambda answer='yes':self.message3(answer))
             self.yes4.grid(row=1,column=0)
             self.top18.bind('<Button-1>',self.flash3)
             self.top18.bind('<ButtonPress-1>',self.flash3)
             self.top18.bind('<Button-2>',self.flash3)
             self.top18.bind('<ButtonPress-2>',self.flash3)
             self.top18.bind('<Button-3>',self.flash3)
             self.top18.bind('<Button-4>',self.flash3)
             self.top18.bind('<Button-5>',self.flash3)
             self.no4=Button(self.topframe3,text='No',command=lambda answer='no':self.message3(answer))
             self.no4.grid(row=1,column=1)
             self.top18.grab_set()
             self.topframe3.grid(row=0)
             self.top18.focus_force()

    #popop while right clicking the listbox item to achieve some internal fuctions   
    def popup(self,event):
        
        self.loadlist.selection_set(self.loadlist.identify_row(event.y))
        #self.loadlist.activate(self.loadlist.nearest(event.y))
        sel=self.loadlist.selection()
        
        selc=self.loadlist.item(sel)
        self.value=selc['text']
              
        
        with open('loader.pk', 'wb') as f2:
               self.data2=pickle.dump(self.value,f2)
        self.men10=Menu(self.top13,tearoff=0,bg='black',activebackground='white',
                        activeforeground='black',font=('Time',10),fg='white',activeborderwidth=0,bd=0,relief=FLAT)
        self.men10.add_cascade(label='Template: {}'.format(self.value))
        self.men10.add_separator()
        self.men10.add_command(label='Edit ({})'.format(self.value),
                               command=lambda answer='yes',answer2='null':self.message2(answer,answer2))
        self.men10.add_separator()
        self.men10.add_command(label='Delete ({})'.format(self.value),command=self.delete)
        self.men10.add_separator()
        self.men10.add_command(label='Properties')
        
        self.popup1(event.x_root,event.y_root)
    def popup1(self,x,y):
       
        try:
           self.men10.tk_popup(x,y)
        finally:
            self.men10.grab_release()

    def change(self):
        self.xc=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\clear.png")
        self.xc=self.xc.resize((round(self.width/7.68),round(self.height/29.19)))
        self.xc=ImageTk.PhotoImage(self.xc)
        self.yc=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\save.png")
        self.yc=self.yc.resize((round(self.width/7.68),round(self.height/29.19)))
        self.yc=ImageTk.PhotoImage(self.yc)
        self.back.grid_forget()
        self.config.grid_forget()
        try:
          for i in range(len(list9)):
                       list9[i].config(state='normal')
          self.cle=Button(self.test10,image=self.xc,borderwidth=0,bd=0,bg='grey',command=self.change2)
          self.sav=Button(self.test10,image=self.yc,borderwidth=0,bd=0,command=self.change1)
          self.cle.grid(row=2,column=0,sticky='s')
          self.sav.grid(row=3,column=0,sticky='s')
          self.ted.entryconfig('Edit',state='disabled')
          
        finally:
            self.ted.entryconfig('Edit',label='Please Save The Template')
        self.config_themes7()
        
    #function to save the cell rows name in the data base (data.db)
    def change1(self):
         data=sqlite3.connect('data.db')
         connet=data.cursor()
         self.names=connet.execute("SELECT cells FROM data").fetchall()
         self.ted.entryconfig('Please Save The Template',state='normal',label='Create')
         self.config.grid(row=1,column=0)
         self.back.grid(row=2,column=0)
         self.sav.grid_forget()
         self.cle.grid_forget()
         #condition whereby the cell row names are still void
         if len(self.names)==0:
           
           for i in range(len(list9)):
               connet.execute("INSERT INTO data(cells) VALUES('{}')".format(list9[i].get(1.0,'end')))
               list9[i].config(state='disabled')
              
           data.commit()   
           data.close()
         #condition whreby the cell row names are updated   
         else:
              connet.execute("DELETE FROM data")
              for i in range(len(list9)):
                            connet.execute("INSERT INTO data(cells) VALUES('{}')".format(list9[i].get(1.0,'end')))
                            list9[i].config(state='disabled')
              data.commit()
              data.close()
              
    def change2(self):
       for i in range(len(list9)):
           list9[i].delete(1.0,'end')
        

    #settings menu function 
    def bind(self):
      
       self.top5=Toplevel()
       self.top5.config(bg='white')
       self.top5.resizable(0,0)
       self.top5.grab_set()
       self.top5.focus_set()
       self.xwidth=self.top5.winfo_screenwidth()
       self.yheight=self.top5.winfo_screenheight()
       self.gwidth=round(self.top5.winfo_screenwidth()/2.09)
       self.gheight=round(self.top5.winfo_screenheight()/1.32)
       self.top5.geometry('{}x{}+{}+{}'.format(self.gwidth,self.gheight,round((self.xwidth/2)-(self.gwidth/2)),
                                               round((self.yheight/2)-(self.gheight/2))))
       self.top5.attributes('-toolwindow',True)
       list_frame=Frame(self.top5)
       self.frame=Frame(self.top5)
       self.frame2=Frame(self.top5)
       self.frame3=Frame(self.top5,bd=0,borderwidth=0,bg='white')
       self.hc=Canvas(self.top5,width=round(self.xwidth/2.18))
       self.frame4=Frame(self.hc,width=round(self.xwidth/2.26))
       self.hsc=Scrollbar(self.top5,orient='vertical')
       self.hsc1=Scrollbar(self.top5,orient='horizontal')
       string=StringVar()
       string.set('Row')
       self.option=Listbox(list_frame,width=round(self.xwidth/24),height=round(self.yheight/154.29),
                           font=('Helvectica',10))
       self.b=['Security','Themes','Configure Functions','How it Works','About','Support And Donation',
               'Restore App To Factory State']
       for c in self.b:
           self.option.insert('end',c)
       self.option.grid(row=1,column=0,sticky='ns')
       list_frame.grid(row=1,column=0,sticky='w')
       self.option.bind('<<ListboxSelect>>',self.pri)
       self.option.selection_set(0)
       self.option.see(0)
       self.security()
       self.config_themes2()
    
    def pri(self,event):
        wid=event.widget
        sel=wid.curselection()
        value=wid.get(sel[0])
        
       #conditon if any of the settings menu is selected it returns back the actual menu
        if value=='Themes':
            self.themes()
        if value=='Security':
            self.security()
        if value=='Configure Functions':
            self.cf()
        if value=='How it Works':
            self.hiw()
        if value=='About':
            self.about()
        if value=='Support And Donation':
            self.sad()
        if value=='Restore App To Factory State':
            self.ras()
    def themes(self):
            self.hsc.grid_forget()
            self.hsc1.grid_forget()
            self.hc.grid_forget()
            self.frame3.grid_forget()
            self.frame.grid(row=4,column=0,sticky='w')
            
            white=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\white.png")
            white=white.resize((round(self.xwidth/4.8),round(self.yheight/10.8)))
            
            white=ImageTk.PhotoImage(white)
            ash=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\ashes.png")
            
            ash=ash.resize((round(self.xwidth/4.8),round(self.yheight/10.8)))
            ash=ImageTk.PhotoImage(ash)
            blue=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\dark blue.png")
            
            blues=blue.resize((round(self.xwidth/4.8),round(self.yheight/10.8)))
            blue=ImageTk.PhotoImage(blues)
            black=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\Black.png")
            
            black=black.resize((round(self.xwidth/4.8),round(self.yheight/10.8)))
            black=ImageTk.PhotoImage(black)
            
            self.cha=Label(self.frame,text='Choose your desire your Theme',font=('Time',round(self.xwidth/160),'bold'),borderwidth=0,bd=0,
                           fg='black')
            self.cha.grid(row=2,column=0,sticky='w')
            #changing of theme and backgrounds including text colors etc
            first_color=Label(self.frame,image=ash,font=('helvectica',13,'bold'),bg='grey').grid(row=3,column=0,sticky='w')
            second_color=Label(self.frame,image=black,font=('helvectica',13,'bold'),bg='black').grid(row=4,column=0,sticky='w')
            third_color=Label(self.frame,image=blue,font=('helvectica',13,'bold'),bg='#151930').grid(row=5,column=0,sticky='w')
            forth_color=Label(self.frame,image=white,font=('helvectica',13,'bold'),bg='white').grid(row=6,column=0,sticky='w')
            self.va1=IntVar()
           
            
            with open('check.pkl','rb') as f1:
                 data=pickle.load(f1)
                 self.va1.set(data)

            var1=Checkbutton(self.frame,text='',var=self.va1,onvalue=1,bd=1,borderwidth=0,command=self.config_themes).grid(row=3,column=2,sticky='w')
            var2=Checkbutton(self.frame,text='',var=self.va1,onvalue=2,bd=1,borderwidth=0,command=self.config_themes).grid(row=4,column=2,sticky='w')
            var3=Checkbutton(self.frame,text='',var=self.va1,onvalue=3,bd=1,borderwidth=0,command=self.config_themes).grid(row=5,column=2,sticky='w')
            var4=Checkbutton(self.frame,text='',var=self.va1,onvalue=4,bd=1,borderwidth=0,command=self.config_themes).grid(row=6,column=2,sticky='w')
            
     #security fuction for settings menu     
    def security(self):
            self.hsc.grid_forget()
            self.hsc1.grid_forget()
            self.hc.grid_forget()
            self.frame.grid_forget()
            
            account=Button(self.frame3,text='Account',font=('helvectica',13),bd=2,borderwidth=0,fg='red',bg='white')
            account.grid(row=0,column=0)
            namesl=Label(self.frame3,text='Users',font=('helveectica',13,'bold'),bd=0,borderwidth=0,bg='white',fg='black')
            namesl.grid(row=1,column=0,pady=15)
            acct_list=ttk.Treeview(self.frame3,column=('A'))
            acct_list.heading('#0',text='Users',anchor='center')
            acct_list.column('A',anchor='center',width=100)

            account=sqlite3.connect('account.db')
            connet=account.cursor()
            user_name=connet.execute("SELECT name FROM account").fetchall()
            pass_word=connet.execute("SELECT password FROM account").fetchall()
            account.commit()
            account.close()
           
            for c in user_name:
                            acct_list.insert('','end',text=c[0])
            acct_list.grid(row=3)
            self.frame3.grid(row=4,column=0,sticky='nwes')

     # configure functions fuction for security menu       
    def cf(self):
            self.hsc.grid_forget()
            self.hsc1.grid_forget()
            self.hc.grid_forget()
            self.frame4.grid_forget()
            self.frame3.grid_forget()
            self.frame.grid_forget()
            
    # How it works Fuction for the security menu       
    def hiw(self):
            self.hsc.grid_forget()
            self.hsc1.grid_forget()
            self.hc.grid_forget()
            self.frame4.grid_forget()
            self.frame3.grid_forget()
            self.frame.grid_forget()
            
            hl=Label(self.frame4,text='''  The F-Box is a miniature office suite it comprises (spreadsheets,word processor,fileviewer),this would be coagulated 
together to form a single piece of software namely F-Box. Use of the F-Box is very simple and straight foward there are 
no needs for prior experiences of using a word processor or spreadsheets i.e anyone can use it.
How to use the F-Box:
1 )The spreadsheets menus(Financials,Monthly) are limited compared to other ones out there but it can solve some basic things 
and it also  have inbuit functions to perfom mathematical and staistical analysis.
2) The spreadsheets menus are only built with 26,rows and 8 columns, the 26 rows and 8 columns can be used interchangeably without 
errors, to do that you set that in the settings
3) The spreadsheets and the memo menus are both built to print out saved docs by your defaults printers. Also the printing can aslo
be done through the saved files menu.
4) Both the spreadsheets and the memo has edit functions i.e you can edit already saved files...Note(only the one done on F-Box not 
any other software.
5) The memo is like a text editor which is more advanced i.e you can input images for better editing of your memos.
6) The products isn't perfect but it can be used to perform basic analysis and not large analysis.
7) The app and your saved docs are protected and no need for fear of loss of datas and it being governed by your acoount created when 
you first open the F-Box.''',justify='left')
            hl.grid(row=1,sticky='w')
            self.hc.update_idletasks()
            self.hc.create_window(0,0,anchor='w',window=self.frame4)
            self.hc.config(scrollregion=self.hc.bbox('all'),yscrollcommand=self.hsc.set,xscrollcommand=self.hsc1.set)
            self.hsc.config(command=self.hc.yview)
            self.hsc1.config(command=self.hc.xview)
            self.hsc1.grid(row=5,column=0,sticky='ew')
            self.hsc.grid(row=4,column=1,sticky='ns')
            #self.frame4.grid(row=4)
            self.hc.grid(row=4,column=0,sticky='w')
   # About function for the about menu         
    def about(self):
            self.hsc.grid_forget()
            self.hsc1.grid_forget()
            self.hc.grid_forget()
            self.frame4.grid_forget()
            self.frame3.grid_forget()
            self.frame.grid_forget()
            self.frame2.grid_forget()
   # Support and Donation function for security and donaton menu         
    def sad(self):
            self.hsc.grid_forget()
            self.hsc1.grid_forget()
            self.hc.grid_forget()
            self.frame4.grid_forget()
            self.frame3.grid_forget()
            self.frame.grid_forget()
            self.frame2.grid_forget()
    # restore App to factory setting function menu        
    def ras(self):
             self.hsc.grid_forget()
             self.hsc1.grid_forget()
             self.hc.grid_forget()
             self.frame4.grid_forget()
             self.frame3.grid_forget()
             self.frame.grid_forget()
             self.frame2.grid_forget()
             print('ye4')
#funtion that changes live i.e it changes the thmeme of individual menus while the programm is still running if the Picke is o the the the theme
 #remains unchanged and if higer than 0 it changes through (grey,black,blue,white)
    def config_themes(self):
        self.var_butt=self.va1.get()
        with open('check.pkl','wb') as f1:
            pickle.dump(self.var_butt,f1)
        with open('check.pkl','rb') as f1:
            self.data=pickle.load(f1)
        
        if self.data==0:
          try:
            self.c4.config(bg='white')
            self.testy.config(bg='white')
            self.config.config(bg='white')
            self.test10.config(bg='white')
            self.test9.config(bg='white')
            self.c3.config(bg='white')
            self.testf.config(bg='white')
            self.toolbar.config(bg='white')
            self.toolbar2.config(bg='white')
            self.f6.config(bg='white')
            self.f7.config(bg='white')
            self.top.config(bg='white')
            self.top5.config(bg='white')
            self.one.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.two.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.three.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.four.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.five.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.six.config(bg='white')
            self.seven.config(bg='white')
            self.eight.config(bg='white')
            self.option.config(bg='white',fg='black')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(fg='black',bg='white',insertbackground='black')
                c1.configure(fg='black',bg='white',insertbackground='black')
                c2.configure(fg='black',bg='white',insertbackground='black')
                c3.configure(fg='black',bg='white',insertbackground='black')
                c4.configure(fg='black',bg='white',insertbackground='black')
                c5.configure(fg='black',bg='white',insertbackground='black')
                c6.configure(fg='black',bg='white',insertbackground='black')
                c7.configure(fg='black',bg='white',insertbackground='black')
                c8.configure(fg='black',bg='white',insertbackground='black')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='white')
               c10.configure(bg='white')
            self.p1.configure(fg='black')
          except AttributeError:
            self.option.config(bg='white',fg='black')
            self.top5.config(bg='white')
        
        if self.data==1:
          try:
            self.c4.config(bg='grey')
            self.testy.config(bg='grey')
            self.config.config(bg='grey')
            self.c3.config(bg='grey')
            self.testf.config(bg='grey')
            self.test10.config(bg='grey')
            self.test9.config(bg='grey')
            self.testy.config(bg='grey')
            self.toolbar.config(bg='grey')
            self.toolbar2.config(bg='grey')
            self.f6.config(bg='grey')
            self.f7.config(bg='grey')
            self.one.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.two.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.three.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.four.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.five.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.six.config(bg='grey')
            self.seven.config(bg='grey')
            self.eight.config(bg='grey')
            self.top.config(bg='grey')
            self.top5.configure(bg='grey')
            self.option.config(bg='grey',fg='white')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='grey',fg='white',insertbackground='white')
                c1.configure(bg='grey',fg='white',insertbackground='white')
                c2.configure(bg='grey',fg='white',insertbackground='white')
                c3.configure(bg='grey',fg='white',insertbackground='white')
                c4.configure(bg='grey',fg='white',insertbackground='white')
                c5.configure(bg='grey',fg='white',insertbackground='white')
                c6.configure(bg='grey',fg='white',insertbackground='white')
                c7.configure(bg='grey',fg='white',insertbackground='white')
                c8.configure(bg='grey',fg='white',insertbackground='white')
                
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='grey')
               c10.configure(bg='grey',fg='white')
            self.p1.configure(fg='white')
          except AttributeError:
            self.option.config(bg='grey',fg='white')
            self.top5.config(bg='grey')
    
        if self.data==2:
          try:
            self.c4.config(bg='black')
            self.testy.config(bg='black')
            self.c3.config(bg='black')
            self.testf.config(bg='black')
            self.config.config(bg='black')
            self.test10.config(bg='black')
            self.test9.config(bg='black')
            self.testy.config(bg='black')
            self.toolbar.config(bg='black')
            self.toolbar2.config(bg='black')
            self.f6.config(bg='black')
            self.f7.config(bg='black')
            self.one.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.two.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.three.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.four.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.five.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.six.config(bg='black')
            self.seven.config(bg='black')
            self.eight.config(bg='black')
            self.top.config(bg='black')
            self.top5.config(bg='black')
            self.option.config(bg='black',fg='white')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='black',fg='white',insertbackground='white')
                c1.configure(bg='black',fg='white',insertbackground='white')
                c2.configure(bg='black',fg='white',insertbackground='white')
                c3.configure(bg='black',fg='white',insertbackground='white')
                c4.configure(bg='black',fg='white',insertbackground='white')
                c5.configure(bg='black',fg='white',insertbackground='white')
                c6.configure(bg='black',fg='white',insertbackground='white')
                c7.configure(bg='black',fg='white',insertbackground='white')
                c8.configure(bg='black',fg='white',insertbackground='white')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='black')
               c10.configure(bg='black',fg='white')
            self.p1.configure(fg='white')
          except AttributeError:
            self.option.config(bg='black',fg='white')
            self.top5.config(bg='black')
            
        if self.data==3:
          try:
            self.c4.config(bg='#151930')
            self.testy.config(bg='#151930')
            self.c3.config(bg='#151930')
            self.testf.config(bg='#151930')
            self.config.config(bg='#151930')
            self.test10.config(bg='#151930')
            self.test9.config(bg='#151930')
            self.testy.config(bg='#151930')
            self.toolbar.config(bg='#151930')
            self.toolbar2.config(bg='#151930')
            self.f6.config(bg='#151930')
            self.f7.config(bg='#151930')
            self.one.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.two.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.three.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.four.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.five.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.six.config(bg='#151930')
            self.seven.config(bg='#151930')
            self.eight.config(bg='#151930')
            self.top.config(bg='#151930')
            self.top5.config(bg='#151930')
            self.option.config(bg='#151930',fg='white')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='#151930',fg='white',insertbackground='white')
                c1.configure(bg='#151930',fg='white',insertbackground='white')
                c2.configure(bg='#151930',fg='white',insertbackground='white')
                c3.configure(bg='#151930',fg='white',insertbackground='white')
                c4.configure(bg='#151930',fg='white',insertbackground='white')
                c5.configure(bg='#151930',fg='white',insertbackground='white')
                c6.configure(bg='#151930',fg='white',insertbackground='white')
                c7.configure(bg='#151930',fg='white',insertbackground='white')
                c8.configure(bg='#151930',fg='white',insertbackground='white')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='#151930')
               c10.configure(bg='#151930',fg='white')
            self.p1.configure(fg='white')
          except AttributeError:
            self.option.config(bg='#151930',fg='white')
            self.top5.config(bg='#151930')
            
        if self.data==4:
          try:
            self.c4.config(bg='white')
            self.testy.config(bg='white')
            self.c3.config(bg='white')
            self.testf.config(bg='white')
            self.config.config(bg='white')
            self.test10.config(bg='white')
            self.test9.config(bg='white')
            self.testy.config(bg='white')
            self.toolbar.config(bg='white')
            self.toolbar2.config(bg='white')
            self.f6.config(bg='white')
            self.f7.config(bg='white')
            self.one.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.two.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.three.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.four.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.five.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.six.config(bg='white')
            self.seven.config(bg='white')
            self.eight.config(bg='white')
            self.top.config(bg='white')
            self.top5.config(bg='white')
            self.option.config(bg='white',fg='black')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='white',fg='black',insertbackground='black')
                c1.configure(bg='white',fg='black',insertbackground='black')
                c2.configure(bg='white',fg='black',insertbackground='black')
                c3.configure(bg='white',fg='black',insertbackground='black')
                c4.configure(bg='white',fg='black',insertbackground='black')
                c5.configure(bg='white',fg='black',insertbackground='black')
                c6.configure(bg='white',fg='black',insertbackground='black')
                c7.configure(bg='white',fg='black',insertbackground='black')
                c8.configure(bg='white',fg='black',insertbackground='black')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='white')
               c10.configure(bg='white',fg='black')
            self.p1.configure(fg='black')
          except AttributeError:
            self.option.config(bg='white',fg='black')
            self.top5.config(bg='white')
    #fuction tp change the setttings menu thmeme        
    def config_themes2(self):
        if self.data==0:
            self.top5.config(bg='white')
            self.option.config(bg='white',fg='black')
        if self.data==1:
            self.top5.configure(bg='grey')
            self.option.config(bg='grey',fg='white')
        if self.data==2:
            self.top5.config(bg='black')
            self.option.config(bg='black',fg='white')
        if self.data==3:
            self.top5.config(bg='#151930')
            self.option.config(bg='#151930',fg='white')
        if self.data==4:
            self.top5.config(bg='white')
            self.option.config(bg='white',fg='black')
    
    
    #function to change the F-analysis theme
    def config_themes5(self):
        try:
         if self.data==0:
            self.c4.config(bg='white')
            self.testy.config(bg='white')
            self.c3.config(bg='white')
            self.testf.config(bg='white')
            self.config.config(bg='white')
            self.test10.config(bg='white')
            self.toolbar.config(bg='white')
            self.toolbar2.config(bg='white')
            self.f6.config(bg='white')
            self.f7.config(bg='white')
            self.top.config(bg='white')
            self.test9.config(bg='white')
            self.one.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.two.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.three.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.four.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.five.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.six.config(bg='white')
            self.seven.config(bg='white')
            self.eight.config(bg='white')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(fg='black',bg='white')
                c1.configure(fg='black',bg='white')
                c2.configure(fg='black',bg='white')
                c3.configure(fg='black',bg='white')
                c4.configure(fg='black',bg='white')
                c5.configure(fg='black',bg='white')
                c6.configure(fg='black',bg='white')
                c7.configure(fg='black',bg='white')
                c8.configure(fg='black',bg='white')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='white')
               c10.configure(bg='white')
            self.p1.configure(fg='black')
            
         if self.data==1:
            self.c4.config(bg='grey')
            self.c3.config(bg='grey')
            self.testf.config(bg='grey')
            self.testy.config(bg='grey')
            self.config.config(bg='grey')
            self.test10.config(bg='grey')
            self.toolbar.config(bg='grey')
            self.toolbar2.config(bg='grey')
            self.test9.config(bg='grey')
            self.f6.config(bg='grey')
            self.f7.config(bg='grey')
            self.one.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.two.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.three.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.four.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.five.config(bg='grey',fg='white',activebackground='black',activeforeground='white')
            self.six.config(bg='grey')
            self.seven.config(bg='grey')
            self.eight.config(bg='grey')
            self.top.config(bg='grey')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='grey',fg='white')
                c1.configure(bg='grey',fg='white')
                c2.configure(bg='grey',fg='white')
                c3.configure(bg='grey',fg='white')
                c4.configure(bg='grey',fg='white')
                c5.configure(bg='grey',fg='white')
                c6.configure(bg='grey',fg='white')
                c7.configure(bg='grey',fg='white')
                c8.configure(bg='grey',fg='white')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='grey')
               c10.configure(bg='grey',fg='white')
            self.p1.configure(fg='white')
    
            
           
         if self.data==2:
            self.c4.config(bg='black')
            self.c3.config(bg='black')
            self.testf.config(bg='black')
            self.testy.config(bg='black')
            self.config.config(bg='black')
            self.test10.config(bg='black')
            self.toolbar.config(bg='black')
            self.toolbar2.config(bg='black')
            self.test9.config(bg='black')
            self.f6.config(bg='black')
            self.f7.config(bg='black')
            self.one.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.two.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.three.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.four.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.five.config(bg='black',fg='white',activebackground='grey',activeforeground='white')
            self.six.config(bg='black')
            self.seven.config(bg='black')
            self.eight.config(bg='black')
            self.top.config(bg='black')
            
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='black',fg='white',insertbackground='white')
                c1.configure(bg='black',fg='white',insertbackground='white')
                c2.configure(bg='black',fg='white',insertbackground='white')
                c3.configure(bg='black',fg='white',insertbackground='white')
                c4.configure(bg='black',fg='white',insertbackground='white')
                c5.configure(bg='black',fg='white',insertbackground='white')
                c6.configure(bg='black',fg='white',insertbackground='white')
                c7.configure(bg='black',fg='white',insertbackground='white')
                c8.configure(bg='black',fg='white',insertbackground='white')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='black')
               c10.configure(bg='black',fg='white')
            self.p1.configure(fg='white')
            
         if self.data==3:
            self.c4.config(bg='#151930')
            self.c3.config(bg='#151930')
            self.testy.config(bg='#151930')
            self.testf.config(bg='#151930')
            self.config.config(bg='#151930')
            self.test10.config(bg='#151930')
            self.toolbar.config(bg='#151930')
            self.toolbar2.config(bg='#151930')
            self.test9.config(bg='#151930')
            self.f6.config(bg='#151930')
            self.f7.config(bg='#151930')
            self.one.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.two.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.three.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.four.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.five.config(bg='#151930',fg='white',activebackground='grey',activeforeground='white')
            self.six.config(bg='#151930')
            self.seven.config(bg='#151930')
            self.eight.config(bg='#151930')
            self.top.config(bg='#151930')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='#151930',fg='white',insertbackground='white')
                c1.configure(bg='#151930',fg='white',insertbackground='white')
                c2.configure(bg='#151930',fg='white',insertbackground='white')
                c3.configure(bg='#151930',fg='white',insertbackground='white')
                c4.configure(bg='#151930',fg='white',insertbackground='white')
                c5.configure(bg='#151930',fg='white',insertbackground='white')
                c6.configure(bg='#151930',fg='white',insertbackground='white')
                c7.configure(bg='#151930',fg='white',insertbackground='white')
                c8.configure(bg='#151930',fg='white',insertbackground='white')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='#151930')
               c10.configure(bg='#151930',fg='white')
            self.p1.configure(fg='white')
            
         if self.data==4:
            self.c4.config(bg='white')
            self.c3.config(bg='white')
            self.testf.config(bg='white')
            self.testy.config(bg='white')
            self.config.config(bg='white')
            self.test10.config(bg='white')
            self.toolbar.config(bg='white')
            self.toolbar2.config(bg='white')
            self.test9.config(bg='white')
            self.f6.config(bg='white')
            self.f7.config(bg='white')
            self.one.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.two.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.three.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.four.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.five.config(bg='white',fg='black',activebackground='grey',activeforeground='white')
            self.six.config(bg='white')
            self.seven.config(bg='white')
            self.eight.config(bg='white')
            self.top.config(bg='white')
            for c,c1,c2,c3,c4,c5,c6,c7,c8 in zip(kist,list2,list3,list4,list5,list6,list7,list8,list9):
                c.configure(bg='white',fg='black')
                c1.configure(bg='white',fg='black')
                c2.configure(bg='white',fg='black')
                c3.configure(bg='white',fg='black')
                c4.configure(bg='white',fg='black')
                c5.configure(bg='white',fg='black')
                c6.configure(bg='white',fg='black')
                c7.configure(bg='white',fg='black')
                c8.configure(fg='black',bg='white')
            for c9,c10 in zip(h10,h11):
               c9.configure(bg='white')
               c10.configure(bg='white',fg='black')
            self.p1.configure(fg='black')
        except TclError:
              pass
    def config_themes6(self):
        if self.data==0:
            self.rec1.config(bg='white',fg='black')
            self.rec3.config(bg='white',fg='black')
            self.rec6.config(bg='white',fg='black')
        if self.data==1:
            self.rec1.config(bg='grey',fg='white')
            self.rec3.config(bg='grey',fg='white')
            self.rec6.config(bg='grey',fg='white')
        if self.data==2:
            self.rec1.config(bg='black',fg='white')
            self.rec3.config(bg='black',fg='white')
            self.rec6.config(bg='black',fg='white')
        if self.data==3:
            self.rec1.config(bg='#151930',fg='white')
            self.rec3.config(bg='#151930',fg='white')
            self.rec6.config(bg='#151930',fg='white')
        if self.data==4:
            self.rec1.config(bg='white',fg='black')
            self.rec3.config(bg='white',fg='black')
            self.rec6.config(bg='white',fg='black')
    def config_themes7(self):
        if self.data==0:
            self.cle.config(bg='white',activebackground='#8193F7')
            self.sav.config(bg='white',activebackground='#8193F7')
        if self.data==1:
            self.cle.config(bg='grey',activebackground='#F0F4FF')
            self.sav.config(bg='grey',activebackground='#F0F4FF')
        if self.data==2:
            self.cle.config(bg='black',activebackground='#969AA8')
            self.sav.config(bg='black',activebackground='#969AA8')
        if self.data==3:
            self.cle.config(bg='#151930',activebackground='#1D2761')
            self.sav.config(bg='#151930',activebackground='#1D2761')
        if self.data==4:
            self.cle.config(bg='white',activebackground='#8193F7')
            self.sav.config(bg='white',activebackground='#8193F7')
    def config_themes8(self):
        if self.data==0:
            self.cle1.config(bg='white',activebackground='#8193F7')
            self.sav1.config(bg='white',activebackground='#8193F7')
        if self.data==1:
            self.cle1.config(bg='grey',activebackground='#F0F4FF')
            self.sav1.config(bg='grey',activebackground='#F0F4FF')
        if self.data==2:
            self.cle1.config(bg='black',activebackground='#969AA8')
            self.sav1.config(bg='black',activebackground='#969AA8')
        if self.data==3:
            self.cle1.config(bg='#151930',activebackground='#1D2761')
            self.sav1.config(bg='#151930',activebackground='#1D2761')
        if self.data==4:
            self.cle1.config(bg='white',activebackground='#8193F7')
            self.sav1.config(bg='white',activebackground='#8193F7')


            
            
    def close(self,event):
       self.top.destroy()
       root.destroy()
    def master_update(self,event):
        #self.top.update()
        
        t2=threading.Thread(target=self.update).start()
        t1=threading.Thread(target=self.update2).start()
               
        #threading.Thread(target=lambda:sleep(1)).start()
        #t2=threading.Thread(target=self.update2)
        #t2.start()
        #t2.join()
        #self.update2()
        
    def update(self):
        self.width=self.top.winfo_width()-1
        self.height=self.top.winfo_height()-1
        self.v.set(round(0.00625*self.width))
        
        #self.top.update()
        
        self.cong=ImageTk.PhotoImage(self.confi.resize((round(self.width/7.84),round(self.height/36))))
        self.config.configure(image=self.cong)
        self.back.config(font=('helvectica',self.v.get(),'bold'))
        
        
        
        
       
    def update2(self):
       
        
        self.top.update()
    def forcer(self):
      j=ctypes.windll.user32.GetParent(self.top.winfo_id())
      style=ctypes.windll.user32.GetWindowLongPtrW(j,GWL_EXSTYLE)
      style=style & -WS_EX_TOOLWINDOW
      style=style | WS_EX_APPWINDOW
      res=ctypes.windll.user32.SetWindowLongPtrW(j,GWL_EXSTYLE,style)
      self.top.withdraw()
      self.top.after(10,lambda:self.top.deiconify())
      
      kist[0].focus_set()
     
      
#login screen which splashes before the core ussage of the app
    
class Login(Financial):
   def __init__(self,object):
       self.show=object.showit
       self.data=object.data
       self.myframe=object.myframe
   def splash(self):
        
        
        
      
        self.z=0
        self.track2=1
        self.splash_frame=Frame(root,bg='white')
        screen1=root.winfo_screenwidth()
        screen2=root.winfo_screenheight()
        splash_width=round(root.winfo_screenwidth()/1.92)
        splash_height=round(root.winfo_screenheight()/1.54)
        p = Image.open("D:\FES2.png")
        p = p.resize((50, 50))
        self.toolwindow1=Canvas(root,width=splash_width,height=40,bg='black',highlightthickness=0)
        self.toolwindow=Frame(self.toolwindow1,bg='black')
        
        self.toolwindow1.grid(row=0,column=0,sticky='n')
        self.destr=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\term.png")
        self.mini=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\term2.png")
        self.destr=ImageTk.PhotoImage(self.destr)
        self.mini=ImageTk.PhotoImage(self.mini)
        self.cancel=Button(self.toolwindow,image=self.destr,bd=0,borderwidth=0,command=lambda:root.destroy())
        self.cancel.grid(row=0,column=9,sticky='e')
        
        self.minimize=Button(self.toolwindow,image=self.mini,bd=0,borderwidth=0,command=self.resize)
        
        self.minimize.grid(row=0,column=4,sticky='we',padx=round(root.winfo_screenwidth()/73.84))
        self.cancel.bind('<Enter>',self.hover2)
        self.cancel.bind('<Leave>',self.hover3)
        self.minimize.bind('<Enter>',self.hover2)
        self.minimize.bind('<Leave>',self.hover3)
        
       
        p = ImageTk.PhotoImage(p)
        root.iconphoto(False, p)
        
        root.geometry("{}x{}+{}+{}".format(splash_width,splash_height,round((root.winfo_screenwidth()/2)-(splash_width/2)),
                                           round((root.winfo_screenheight()/2)-(splash_height/2))))
        root.title('F-BOX')
        root.config(bg='white')
        
        self.showb=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\show.png")
        self.showb=ImageTk.PhotoImage(self.showb)
        self.showc=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\show2.png")
        self.showc=ImageTk.PhotoImage(self.showc)
        self.logic=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\log.png")
        self.logic=ImageTk.PhotoImage(self.logic)
        self.creatic=Image.open(r"C:\Users\PASCAL\Desktop\FES Project\project 1\create.png")
        self.creatic=ImageTk.PhotoImage(self.creatic)
        
        #Fess logo initiation and placement which was referenced in the initialization function
        self.show.config(bg='white')
        self.show.grid(row=1,column=0,sticky='n',pady=round(root.winfo_screenheight()/36),padx=round(root.winfo_screenwidth()/24))
        root.resizable(0,0)
        self.string=StringVar()
        
        root.overrideredirect(True)
        self.username = Entry(self.splash_frame, font=('helvectica', round(screen1*0.00678)), width=10)
        self.l = Label(self.splash_frame, text='Enter Username', bg='white', fg='black')
        
        self.l.grid(row=1, column=8, sticky='ns')
        self.l2 = Label(self.splash_frame, text='Enter Password', bg='white', fg='black')
        self.l2.grid(row=2, column=8, sticky='ns')
        self.username.grid(row=1, column=9, sticky='ns', pady=5)
        self.password = Entry(self.splash_frame,textvariable=self.string,font=('helvectica', round(screen1*0.00678)), width=10, show='*')
        self.password.grid(row=2, column=9, sticky='ns', pady=5)
        self.phone=Entry(self.splash_frame,font=('Helvectica', round(screen1*0.00678)),width=12)
        self.l3=Label(self.splash_frame,text='Enter Phone Number',bg='white',fg='black')
        self.hubby=Entry(self.splash_frame,font=('Helvectica', round(screen1*0.00678)),width=12)
        self.l4=Label(self.splash_frame,text='Your Hubby',bg='white',fg='black')
        self.l5=Label(self.splash_frame,text='* ALL FIELDS ARE REQUIRED',bg='white',fg='black')
        self.visible=Button(self.splash_frame,image=self.showc,font=('Helvectica',5),command=self.visibility,borderwidth=0,bd=0)
        self.sp2=Frame(self.splash_frame,bg='white')
        self.loginb=Button(self.splash_frame,image=self.logic,bd=0,borderwidth=0,command=lambda e='i':self.logined(e))
        self.logb=Button(self.sp2,image=self.creatic,bd=0,borderwidth=0,command=lambda event='e':self.create(event))
        
        self.reg=Label(self.splash_frame,text='Sign Up',font=('helvectical',15,'bold'),bg='white',fg='blue')
        self.login=Label(self.splash_frame,text='Login',font=('helvectical',20,'bold'),bg='white',fg='green')
        #conditon whereby when theere is no account logged-in ten it askes one
        
        #when there is an acoount logged in
        if path.exists('account.db')==False:
            account=sqlite3.connect('account.db')
            connet=account.cursor()
            connet.execute("CREATE TABLE account(name TEXT,password TEXT,phone TEXT,hubby TEXT)")
            account.commit()
            account.close()
        if path.exists('account.db')==True:
            account=sqlite3.connect('account.db')
            connet=account.cursor()
            cred1=connet.execute("SELECT name FROM account").fetchall()
            account.commit()
            account.close()
        
       
           
        if len(cred1)>0:
                self.regi=self.password.register(self.verify)
                self.username.insert(0,cred1[0])
                self.password.config(validate='key',validatecommand=(self.regi,'%V'))
                
                self.login.grid(row=0,column=8,sticky='ns')
                self.loginb.grid(row=4,column=8,sticky='ns')
                self.visible.grid(row=2,column=10,sticky='ns')
                self.password.focus_set()
                self.id1=self.password.bind('<Return>',self.logined,'+')
                print(self.password.index('insert'))
            #conditon whereby when theere is no account logged-in ten it askes one
        if len(cred1)==0:
               self.l5.grid(row=0,column= 9,sticky='w')
               self.username.config(validate='all',validatecommand=self.reg)
              
               self.reg.grid(row=0,column=8,sticky='ns')
               self.logb.grid(row=4,column=8,sticky='ns')
               self.sp2.grid(row=5,column=8,sticky='ns')
               self.phone.grid(row=3,column=9,sticky='ns',pady=5,padx=9)
               self.l3.grid(row=3,column=8,sticky='ns',pady=5,padx=9)
               self.l4.grid(row=4,column=8,sticky='ns',pady=5)
               self.hubby.grid(row=4,column=9,sticky='ns',pady=5)
               self.visible.grid(row=2,column=10,sticky='ns')
               self.username.focus_set()
               self.id2=root.bind('<Return>',self.create,'+')
            #general Entry of password and username for both creation and logging in

        self.toolwindow1.update_idletasks()
        
        self.toolwindow1.create_window(round(screen1/2.07),round(screen2/120),anchor='n',window=self.toolwindow)
        
        self.splash_frame.grid(row=2,sticky='ns')
        self.config_themes3()
        self.id4=self.toolwindow1.bind('<B1-Motion>',self.move2)
        self.id5=self.toolwindow1.bind('<ButtonPress-1>',self.move)
        self.id6=root.bind('<Map>',self.framed)
        root.update()
        root.after_idle(root.focus_force)
    #Login fuction when login function is triggered
   def logined(self,e):
        screen1=root.winfo_screenwidth()
        screen2=root.winfo_screenheight()
        p = Image.open("D:\FES2.png")
        p = p.resize((50, 50))
        p = ImageTk.PhotoImage(p)
        root.iconphoto(False, p)
        cred2=self.password.get()
        account=sqlite3.connect('account.db')
        connet=account.cursor()
        mes=[c for c in connet.execute("SELECT name,password FROM account").fetchmany(2)]
        
        
        
        self.sp=Frame(self.myframe,bg='white')
        self.forgotten=Button(self.sp,text='Forgot Credentials',font=('helvectica',10,'bold'),
                          activebackground='green',borderwidth=0,bd=0,bg='white',fg='green',command=self.forgot)
    #condition when the password entered doesen't match with the one which was logged in before
        if self.password.get()!=mes[0][1] or self.username.get()!=mes[0][0]:
            
            error=showerror('Error','Username Or Pasword Wrong')
            self.password.delete(0,'end')
            self.password.config(width=10)
            self.username.config(width=10)
            try:
             self.password.unbind('<Key>',self.id7)
             self.track2=1
            except:
                  pass
            self.forgotten.grid(row=5,column=0,sticky='ns')
            self.sp.grid(row=5,column=0,sticky='ns',ipadx=37)
            self.myframe.grid()
    #when the password is corect and corresponds with the one which was logged in
        else:
          self.splash_frame.grid_forget()
          self.myframe.grid_forget()
          self.sp2.grid_forget()
          self.toolwindow.grid_forget()
          self.toolwindow1.grid_forget()
          first.display()
          self.password.unbind('<Return>',self.id1)
        self.config_themes4()
   #when the 'create' button is triggered its perforrms the account creation 
   def create(self,event):
        if len(self.username.get())>2 and len(self.password.get())>4 and len(self.phone.get())==11 and len(self.hubby.get())>3:
          account=sqlite3.connect('account.db')
          connet=account.cursor()
          connet.execute("INSERT INTO account VALUES('{}','{}','{}','{}')".format(self.username.get(),self.password.get(),self.phone.get(),self.hubby.get()))
          account.commit()
          account.close()
          
          self.splash_frame.grid_forget()
          self.myframe.grid_forget()
          root.unbind('<Return>',self.id2)
          first.display()
    #warning shown when there is no password nor username entres before the creation of the account
        else:
            warning=showwarning('Too short',"""Username or Password(must be greater than 4) Too Short
or phone number too short(must be accurate)""")
   def forgot(self):
        self.loginb.grid_forget()
        self.login.grid_forget()
        self.l.grid_forget()
        self.l2.grid_forget()
        self.username.grid_forget()
        self.password.grid_forget()
        self.forgotten.grid_forget()
        self.visible.grid_forget()
        self.rec1=Label(self.splash_frame,text='Your Phone Number')
        self.rec1.grid(row=1,column=8,sticky='ns')
        self.rec2=Entry(self.splash_frame,font=('Time',12),width=12)
        self.rec2.grid(row=1,column=9,sticky='ns',padx=4)
        self.rec3=Label(self.splash_frame,text='Your Hubby')
        self.rec3.grid(row=2,column=8,sticky='ns',pady=5)
        self.rec4=Entry(self.splash_frame,font=('Time',13),width=10)
        self.rec4.grid(row=2,column=9,sticky='ns',pady=5)
        self.rec5=Button(self.splash_frame,text='Recover',font=('Helvectica',10,'bold'),bd=9,borderwidth=1,command=lambda event='e':self.recover(event))
        self.rec5.grid(row=3,column=8,sticky='ns')
        self.rec6=Label(self.splash_frame,text='Confirm New Password')
        self.rec7=Entry(self.splash_frame,font=('Time',13),width=13,show='*')
        self.rec8=Button(self.splash_frame,text='Back',font=('Time',12),bd=9,borderwidth=2,command=self.home)
        self.rec8.grid(row=3,column=9)
        self.config_themes6()
        self.password.unbind('<Return>',self.id1)
        self.id3=root.bind('<Return>',self.recover,'+')
   def home(self):
        self.rec1.grid_forget()
        self.rec2.grid_forget()
        self.rec3.grid_forget()
        self.rec4.grid_forget()
        self.rec5.grid_forget()
        self.rec6.grid_forget()
        self.rec7.grid_forget()
        self.rec8.grid_forget()
        root.unbind('<Return>',self.id3)
        root.after(10,lambda:set(root))
        master.splash()
        self.password.focus_set()

   def recover(self,event):
        account=sqlite3.connect('account.db')
        connet=account.cursor()
        recov=connet.execute("SELECT phone,hubby FROM account").fetchmany(2)
        print(recov)
        for c in recov:
            self.recov1=c[0]
            recov2=c[1]
        
        if self.rec2.get()!=self.recov1 and self.rec4.get()!=recov2:
            self.rec2.delete(0,'end')
            self.rec4.delete(0,'end')
            warning=showwarning('Wrong','Both Wrong')
        else:
            self.rec3.grid_forget()
            self.rec4.grid_forget()
            self.rec1.configure(text='Enter New Password')
            self.rec2.delete(0,'end')
            self.rec2.configure(width=13,show='*')
            self.rec6.grid(row=2,column=8,sticky='ns',pady=5)
            self.rec7.grid(row=2,column=9,sticky='ns',pady=5)
            self.rec5.configure(text='Save',command=self.success)


   def success(self):  
         
         if self.rec7.get()==self.rec2.get():
            account=sqlite3.connect('account.db')
            connet=account.cursor()
            connet.execute("UPDATE account SET password=? WHERE phone=?",(self.rec2.get(),self.recov1))
            account.commit()
            account.close()
            self.rec1.grid_forget()
            self.rec2.grid_forget()
            self.rec6.grid_forget()
            self.rec7.grid_forget()
            self.rec5.grid_forget()
            self.rec8.grid_forget()
            root.after(10,lambda:set(root))
            master.splash()

         else:
             self.rec7.delete(0,'end')
             warning=showerror('Error',"Password Did Not Match!")
   def visibility(self):
        global counter
        counter+=1
        
        if self.visible:
            
            if counter==1:
                self.password.config(show='')
                self.visible.config(image=self.showb)
                
            if counter>1:
                
                self.password.config(show='*')
                self.visible.config(image=self.showc)
                counter=0
   def verify(self,input):
        
        
        
        
        if len(self.password.get())+1>12 and self.track2==1:
            self.password.config(width=self.password.cget('width')+self.track2+1)
            self.username.config(width=self.password.cget('width'))
            self.id9=self.password.bind('<BackSpace>',self.function2)
            
            
            
            if len(self.password.get())==20:
                self.track=0
                self.track2=0
                self.id7=self.password.bind('<Key>',lambda e: 'break')
                
                self.id8=self.password.bind('<BackSpace>',self.backspace2)
                #print(3)
                
        return True
    
   def backspace2(self,event):
        try:
          self.password.unbind('<Key>',self.id7)
        except tkinter.TclError:
            pass
        self.id11=self.password.bind('<Key>',self.function4)
        if self.password.cget('width')>10:
            threading.Thread(target=self.username.config(width=self.password.cget('width')-2)).start()
            threading.Thread(target=self.password.config(width=self.password.cget('width')-2)).start()
        
        
        if self.password.cget('width')==10:

            self.username.config(width=10)
            self.password.config(width=10)
          
           
   def function2(self,event):
        self.track2=0
        self.id10=self.password.bind('<Key>',self.function3)
        if self.password.cget('width')>10:
            threading.Thread(target=self.username.config(width=self.password.cget('width')-1)).start()
            threading.Thread(target=self.password.config(width=self.password.cget('width')-1)).start()
        
        
        if self.password.cget('width')==10:

            self.username.config(width=10)
            self.password.config(width=10)
        
   def function3(self,event):
        if event.char.isdigit() or event.char.isalpha():
            self.track2=1
            try:
              self.password.unbind('<BackSpace>',self.id9)
              
            except tkinter.TclError:
                pass
            
            

            
           
        else:
           self.track2=1
           try:
            self.password.unbind('<BackSpace>',self.id9)
            self.password.unbind('<BackSpace>',self.id8)
           except tkinter.TclError:
               pass
           
   def function4(self,event):

        if event.char.isdigit() or event.char.isalpha():
            self.track2=1
            
            try:
              self.password.unbind('<BackSpace>',self.id8)
            except tkinter.TclError:
                pass
            

            
           
        else:
           self.track2=1
           
           try:
              self.password.unbind('<BackSpace>',self.id8)
           except tkinter.TclError:
                pass
           
           
          

        
   def move(self,event):
        self.xp=event.x
        self.yp=event.y
   def move2(self,event):
        deltax=event.x-self.xp
        deltay=event.y-self.yp
        splash_width=round(root.winfo_screenwidth()/1.92)
        splash_height=round(root.winfo_screenheight()/1.54)
        screen1=root.winfo_x()+deltax
        screen2=root.winfo_y()+deltay
        root.geometry(newGeometry='{}x{}+{}+{}'.format(splash_width,splash_height,screen1,screen2))
   def resize(self):
        self.z=1
        root.withdraw()
        root.overrideredirect(False)
        
        
        root.iconify()
   def framed(self,event=NONE):
        
        root.overrideredirect(True)
        if self.z==1:
          
          root.after(10,lambda:set(root))
          root.update()
          self.z=0
   
   def hover2(self,button):
        
        button.widget.config(bg='#8193F7')
   def hover3(self,button):
        button.widget.config(bg=self.show.cget('bg'))       
        
   #function to change the login function of the splash 
   def config_themes3(self):
        if self.data==0:
           root.config(bg='white')
           self.show.config(bg='white')
           self.splash_frame.config(bg='white')
           self.reg.config(bg='white')
           self.toolwindow.config(bg='white')
           self.toolwindow1.config(bg='white')
           self.cancel.config(bg='white')
           self.minimize.config(bg='white')
           self.visible.config(bg='white',activebackground='white')
           self.login.config(bg='white')
           self.logb.config(bg='white')
           self.loginb.config(bg='white',activebackground='white')
           self.l.config(bg='white',fg='black')
           self.l2.config(bg='white',fg='black')
           self.l3.config(bg='white',fg='black')
           self.l4.config(bg='white',fg='black')
           self.l5.config(bg='white',fg='black')
        if self.data==1:
            root.config(bg='grey')
            self.show.config(bg='grey')
            self.splash_frame.config(bg='grey')
            self.toolwindow.config(bg='grey')
            self.toolwindow1.config(bg='grey')
            self.cancel.config(bg='grey')
            self.minimize.config(bg='grey')
            self.visible.config(bg='grey',activebackground='grey')
            self.reg.config(bg='grey')
            self.logb.config(bg='grey')
            self.loginb.config(bg='grey',activebackground='grey')
            self.login.config(bg='grey')
            self.l.config(bg='grey',fg='white')
            self.l2.config(bg='grey',fg='white')
            self.l3.config(bg='grey',fg='white')
            self.l4.config(bg='grey',fg='white')
            self.l5.config(bg='grey',fg='white')
        if self.data==2:
            root.config(bg='black')
            self.show.config(bg='black')
            self.toolwindow.config(bg='black')
            self.toolwindow1.config(bg='black')
            self.cancel.config(bg='black')
            self.minimize.config(bg='black')
            self.splash_frame.config(bg='black')
            self.reg.config(bg='black')
            self.logb.config(bg='black')
            self.loginb.config(bg='black')
            self.visible.config(bg='black',activebackground='black')
            self.login.config(bg='black')
            self.l.config(bg='black',fg='white')
            self.l2.config(bg='black',fg='white')
            self.l3.config(bg='black',fg='white')
            self.l4.config(bg='black',fg='white')
            self.l5.config(bg='black',fg='white')
        if self.data==3:
            root.config(bg='#151930')
            self.show.config(bg='#151930')
            self.splash_frame.config(bg='#151930')
            self.reg.config(bg='#151930')
            self.logb.config(bg='#151930')
            self.toolwindow.config(bg='#151930')
            self.toolwindow1.config(bg='#151930')
            self.cancel.config(bg='#151930')
            self.minimize.config(bg='#151930')
            self.visible.config(bg='#151930',activebackground='#151930')
            self.login.config(bg='#151930')
            self.loginb.config(bg='#151930',activebackground='#151930')
            self.l.config(bg='#151930',fg='white')
            self.l2.config(bg='#151930',fg='white')
            self.l3.config(bg='#151930',fg='white')
            self.l4.config(bg='#151930',fg='white')
            self.l5.config(bg='#151930',fg='white')
        if self.data==4:
            root.config(bg='white')
            self.show.config(bg='white')
            self.splash_frame.config(bg='white')
            self.reg.config(bg='white')
            self.logb.config(bg='white')
            self.toolwindow.config(bg='white')
            self.toolwindow1.config(bg='white')
            self.cancel.config(bg='white')
            self.minimize.config(bg='white')
            self.login.config(bg='white')
            self.visible.config(bg='white',activebackground='white')
            self.loginb.config(bg='white',activebackground='white')
            self.l.config(bg='white',fg='black')
            self.l2.config(bg='white',fg='black')
            self.l3.config(bg='white',fg='black') 
            self.l4.config(bg='white',fg='black')
            self.l4.config(bg='white',fg='black')
    #function to change the theme fogotton credentials functions
   def config_themes4(self):
        if self.data==0:
            self.sp.config(bg='white')
            self.forgotten.config(bg='white')
        if self.data==1:
            self.sp.config(bg='grey')
            self.forgotten.config(bg='grey')
        if self.data==2:
            self.sp.config(bg='black')
            self.forgotten.config(bg='black')
        if self.data==3:
            self.sp.config(bg='#151930')
            self.forgotten.config(bg='#151930')
        if self.data==4:
            self.sp.config(bg='white')
            self.forgotten.config(bg='white')
       

   
       

            
            
    
 #memo class frame      
class Memo(Financial):
    def __init__(self,master):
        self.master=master
    def mem(self):
        m = Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\bmb.png")
        m = m.resize((450,400))#resized
        m = ImageTk.PhotoImage(m)
        self.top3=Toplevel()
        self.top3.attributes('-fullscreen',True)
        self.top3.wm_title('Memo')
        self.top3.iconphoto(False,m)
        self.top3.wm_geometry('600x400')
        men=Menu(self.top3)
        self.top3.config(menu=men)
        f_menu=Menu(men,tearoff=0)
        e_menu=Menu(men,tearoff=0)
        men.add_cascade(label='File',menu=f_menu)
        men.add_cascade(label='Edit',menu=e_menu)
        p_menu=Menu(men,tearoff=0)
        pa_menu=Menu(men,tearoff=0)
        men.add_cascade(label='Paragraph',menu=pa_menu)
        men.add_cascade(label='Print',menu=p_menu)
        p_menu.add_command(label='Print')
        e_menu.add_command(label='Copy')
        e_menu.add_command(label='Paste',command=self.insert_pic)
        e_menu.add_command(label='Cut')
        e_menu.add_command(label='Undo')
        e_menu.add_command(label='Redo')
        f_menu.add_command(label='Save')
        f_menu.add_command(label='SaveAs')
        f_menu.add_command(label='Delete')
        f_menu.add_command(label='Open',command=self.open)
        pa_menu.add_command(label='Indented')
        pa_menu.add_command(label='Block')
        pa_menu.add_command(label='Centre')
        pa_menu.add_command(label='Left')
        pa_menu.add_command(label='Right')
        l1=Label(self.top3,text='Ready',font=('Helvetica',12))
        l1.grid(sticky='es')
        sc3=Scrollbar(self.top3,orient='vertical')
        self.textbox=Text(self.top3,font=('Helvetica',13),width=100,height=32,selectbackground='powder blue',
                     undo=True,selectforeground='black',yscrollcommand=sc3.set)
        self.textbox.grid(row=0,column=0)
        sc3.config(command=self.textbox.yview)
        sc3.grid(row=0,column=1,sticky='ns')
    def open(self):
        self.file=askopenfilename(parent=self.top3,title='Open File',filetypes=(['Text Files','.txt'],['PDF','.pdf'],['Microsoft Doc','.docx'],['Retrieve Text From Any File','*']))
        if self.file:
            print(self.file)
            the_file=open(self.file)
            self.textbox.insert(1.0,the_file.read())
    def insert_pic(self):
        self.file2=askopenfilename(parent=self.top3,title='insert image',filetypes=(['PNG','.png'],['JPEG','.jpg'],['Bitmap','.bmp']))
        if self.file2:
            in_image=Image.open(self.file2)
            in_image=ImageTk.PhotoImage(in_image)
            self.textbox.image_create(1.1,image=in_image)
            self.textbox.in_image=in_image
            

    
#The app Main menu 
class Main(Financial):
    def __init__(self,object):
        
        #self.to=object.top
        self.f=object.showit
        self.main=main
        self.nam=object.data
        self.screen1=round(root.winfo_screenheight()/27)
        self.screen2=round(root.winfo_screenheight()-self.screen1)
            
        self.icon1=Canvas(root,highlightthickness=0,width=root.winfo_screenwidth(),height=self.screen2+10)
        self.fra1=Frame(self.icon1,highlightthickness=0)
        
      
       
        self.maxi=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\maximize.png")
        self.t =Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\suunday.png")
        self.z=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\settings.png")
        self.m = Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\bmb.png")
        self.y=Image.open(rb"C:\Users\PASCAL\Desktop\FES Project\project 1\Monthly.png")
        self.label = Button(self.fra1, text='Financial Analysis', font=('blue', 13, 'bold'),borderwidth=0,bd=0,command=master.get)
        self.b = Button(self.fra1, borderwidth=0,command=master.get)
        memory=sqlite3.connect(':memory:')
        mem=memory.cursor()
        mem.execute("CREATE TABLE icon(image TEXT)")
        #mem.execute("INSERT INTO icon(image) VALUES(?)",[sqlite3.Binary(t)])
        memory.commit()

    def display(self):
            self.maxi=ImageTk.PhotoImage(self.maxi)
            
            self.toolwindow1=Canvas(root,width=root.winfo_screenwidth(),height=self.screen1,bg='black',highlightthickness=0)
            self.toolwindow=Frame(self.toolwindow1,bg='black')
            self.maximize=Button(self.toolwindow,image=self.maxi,bd=0,borderwidth=0,bg='black')
            self.maximize.grid(row=0,sticky='e')
            
            
           
            root.wm_title('F-BOX')
            
            root.geometry('{}x{}+-0+1'.format(root.winfo_screenwidth(),root.winfo_screenheight()-1))
            root.after(10,lambda:set(root))
            my4=Hovertip(self.b,'Daily\nFinancial Analysis')
            self.v=StringVar()
            self.v.set('grey')
            self.f.grid_forget()
            root.resizable(1,1)
            #F-analysis icon image
            self.b.grid(row=0,column=0,sticky='nsew')
            self.label.grid(row=1,column=0,sticky='nsew')
            #memo icon image
            
            
            #memo button trigger
            self.b2 = Button(self.fra1, borderwidth=0,command=main.mem)
            #self.b2.self.m=self.m
            self.b2.grid(row=0,column=1,padx=round(root.winfo_screenheight()/18),sticky='nsew')
            my1=Hovertip(self.b2,'Text Editor',hover_delay=500)
            
            # memo button trigger 2
            self.label2 = Button(self.fra1, text='Memo', font=('blue', 12, 'bold'),borderwidth=0,bd=0,command=main.mem)
            self.label2.grid(row=1, column=1,padx=round(root.winfo_screenheight()/18),sticky='nsew')
            #f-analysis button trigger 2
            
            
            #f-analysis button trigger 
           
            #monthly analysis button image icon
            
            
            self.b3=Button(self.fra1,borderwidth=0,bd=0)
            
            self.b3.grid(row=0,column=2,padx=round(root.winfo_screenheight()/18),sticky='nsew')
            my2=Hovertip(self.b3,'Monthly Report',hover_delay=500)
            self.label3=Button(self.fra1,text='Monthly Analysis',font=('Time',13,'bold'),borderwidth=0,bd=0)
            self.label3.grid(row=1,column=2,padx=round(root.winfo_screenheight()/18),sticky='nsew')
            
            
            #settings buttin image icon
           
            
            self.se=Button(self.fra1,borderwidth=0,padx=round(root.winfo_screenheight()/18),command=master.bind)
            
            self.label4=Button(self.fra1,text='Settings',font=('Time',13,'bold'),borderwidth=0,bd=0,command=master.bind)
            self.se.grid(row=0,column=3,padx=round(root.winfo_screenheight()/18),sticky='nsew')
            my3=Hovertip(self.se,'Setings And Configuration',hover_delay=500)
            self.label4.grid(row=1,column=3,sticky='nsew')
            #App icon image
            p = Image.open("D:\FES2.png")
            p = p.resize((50, 50))
            p = ImageTk.PhotoImage(p)
            root.iconphoto(False, p)
            root.config(bg=self.v.get())
            
            
            
            
            #self.fra1.grid(row=1,column=0,sticky='nsew')
            #self.fra2.grid(row=1,column=1,sticky='nsew')
            #self.fra3.grid(row=1,column=2,sticky='nsew')
            #self.fra4.grid(row=1,column=3,sticky='nsew')
            
            Grid.columnconfigure(self.fra1 ,0,weight=1)
            Grid.columnconfigure(self.fra1,2,weight=1)
            Grid.rowconfigure(self.fra1,0,weight=1)
            Grid.rowconfigure(self.fra1,1,weight=1)
            Grid.columnconfigure(self.fra1,1,weight=1)
            Grid.columnconfigure(self.fra1,3,weight=1)
            
            threading.Thread(target=root.update).start()
            
            
            self.geo=root.winfo_width()
            self.geo2=root.winfo_height()
            #self.print2('e')
            
            self.theme_change()
            
            self.toolwindow1.update_idletasks()
            self.icon1.update_idletasks()
            
            self.icon1.grid_propagate(False)
            self.toolwindow1.grid_propagate(False)
            self.toolwindow1.create_window(1800,round(self.geo2/120),anchor='n',window=self.toolwindow)
            self.icon1.create_window(0,round(root.winfo_screenheight()/4.7),anchor='w',window=self.fra1)
            self.toolwindow1.grid(row=0,column=0,sticky='n')
            self.icon1.grid(row=1,column=0,sticky='nsew')
            root.bind('<Configure>',self.print2)
            root.after_idle(root.focus_force)
            
            #root.state('zoomed')
    def theme_change(self):
        if self.nam==0:
            root.config(bg='grey')
            self.b2.config(bg='grey',activebackground='grey')
            self.label2.config(bg='grey',activebackground='grey',fg='white')
            self.label.config(bg='grey',activebackground='grey',fg='white')
            self.b.config(bg='grey',activebackground='grey')
            self.b3.config(bg='grey',activebackground='grey')
            self.label3.config(bg='grey',activebackground='grey',fg='white')
            self.se.config(bg='grey',activebackground='grey')
            self.label4.config(bg='grey',activebackground='grey',fg='white')
            self.fra1.config(bg='grey')
            self.icon1.config(bg='grey')
           
       
        if self.nam==1:
            root.config(bg='grey')
            self.b2.config(bg='grey',activebackground='grey')
            self.label2.config(bg='grey',activebackground='grey',fg='white')
            self.label.config(bg='grey',activebackground='grey',fg='white')
            self.b.config(bg='grey',activebackground='grey')
            self.b3.config(bg='grey',activebackground='grey')
            self.label3.config(bg='grey',activebackground='grey',fg='white')
            self.se.config(bg='grey',activebackground='grey')
            self.label4.config(bg='grey',activebackground='grey',fg='white')
            self.fra1.config(bg='grey')
            self.icon1.config(bg='grey')
            
       
        if self.nam==2:
            root.config(bg='black')
            self.b2.config(bg='black',activebackground='black')
            self.label2.config(bg='black',activebackground='black',fg='white')
            self.label.config(bg='black',activebackground='black',fg='white')
            self.b.config(bg='black',activebackground='black')
            self.b3.config(bg='black',activebackground='black')
            
            self.label3.config(bg='black',activebackground='black',fg='white')
            self.se.config(bg='black',activebackground='black')
            self.label4.config(bg='black',activebackground='black',fg='white')
            self.fra1.config(bg='black')
            self.icon1.config(bg='black')
            
       
        if self.nam==3:
            root.config(bg='#151930')
            self.b2.config(bg='#151930',activebackground='#151930')
            self.label2.config(bg='#151930',activebackground='#151930',fg='white')
            self.label.config(bg='#151930',activebackground='#151930',fg='white')
            self.b.config(bg='#151930',activebackground='#151930')
            self.b3.config(bg='#151930',activebackground='#151930')
            self.label3.config(bg='#151930',activebackground='#151930',fg='white')
            self.se.config(bg='#151930',activebackground='#151930')
            self.label4.config(bg='#151930',activebackground='#151930',fg='white')
            self.fra1.config(bg='#151930')
            self.icon1.config(bg='#151930')

            
       
        if self.nam==4:
            root.config(bg='white')
            self.b2.config(bg='white',activebackground='white')
            self.label2.config(bg='white',activebackground='white',fg='black')
            self.label.config(bg='white',activebackground='white',fg='black')
            self.b.config(bg='white',activebackground='white')
            self.b3.config(bg='white',activebackground='white')
            self.label3.config(bg='white',activebackground='white',fg='black')
            self.se.config(bg='white',activebackground='white')
            self.label4.config(bg='white',activebackground='white',fg='black')
            self.fra1.config(bg='white')
            self.icon1.config(bg='white')
            
    def print2(self,event):
        
        #p=threading.Thread(target=self.print)
        #p1=threading.Thread(target=self.print3)  
        #p2=threading.Thread(target=self.print4)
        #p3=threading.Thread(target=self.print5)
        #p.start()
        #p1.start()
        #p2.start()
        #p3.start()
        #self.print4()
        
        self.print()
        self.print3()
        self.print4()
        self.print5()
        
        
        #Process(target=self.print4).run()
    def resize1(self):
       pass
    def print(self):
           if self.m:
               iw,ih=self.m.width,self.m.height
               mw,mh=root.winfo_width(),root.winfo_height()
              
               
               
           if self.geo==mw:
                   iw=self.geo//5
                   ih=self.geo//5
                   self.ic1 =ImageTk.PhotoImage(self.t.resize((iw, ih)),Image.NEAREST)
                   self.b.configure(image=self.ic1)
                   self.label.config(font=('Helvectica',12,'bold'))
                   
                   
           else:
             iw=mw//5
             ih=mw//5
        
             self.ic1 = ImageTk.PhotoImage(self.t.resize((iw, ih)),Image.NEAREST)
             self.b.configure(image=self.ic1)
             self.label.config(font=('Helvectica',round((mw*0.00625)+3),'bold'))
           
    

    def print3(self):
      
      if self.m:
            iw,ih=self.m.width,self.m.height
            mw,mh=root.winfo_width(),root.winfo_height()


      if self.geo==mw:
             iw=self.geo//5
             ih=self.geo//5
             self.ic2 = ImageTk.PhotoImage(self.m.resize((iw,ih)),Image.NEAREST)
             self.b2.config(image=self.ic2)
             self.label2.config(font=('Helvectica',12,'bold'))
      else:
        iw=mw//5
        ih=mw//5
               
        self.ic2= ImageTk.PhotoImage(self.m.resize((iw,ih)),Image.NEAREST)
        self.b2.config(image=self.ic2)
        self.label2.config(font=('Helvectica',round((mw*0.00625)+3),'bold'))
      

    def print4(self):
        if self.m:
            iw,ih=self.m.width,self.m.height
            mw,mh=root.winfo_width(),root.winfo_height()

        if self.geo==mw:
             iw=self.geo//5
             ih=self.geo//5
             self.ic3=ImageTk.PhotoImage(self.y.resize((iw,ih)),Image.NEAREST)
             self.b3.config(image=self.ic3)
             self.label3.config(font=('Helvectica',12,'bold'))


        else:
           iw=mw//5
           ih=mw//5
           self.ic3=ImageTk.PhotoImage(self.y.resize((iw,ih)),Image.NEAREST)
           self.b3.config(image=self.ic3)
           self.label3.config(font=('Helvectica',round((mw*0.00625)+3),'bold'))
        
    def print5(self):
        if self.m:
            iw,ih=self.m.width,self.m.height
            mw,mh=root.winfo_width(),root.winfo_height()

        if self.geo==mw:
             iw=self.geo//5
             ih=self.geo//5

             self.ic4=ImageTk.PhotoImage(self.z.resize((iw,ih)),Image.NEAREST)
             self.se.config(image=self.ic4)
             self.label4.config(font=('Helvectica',13,'bold'))

        else:
           iw=mw//5
           ih=mw//5
            
           self.ic4=ImageTk.PhotoImage(self.z.resize((iw,ih)),Image.NEAREST)
           self.se.config(image=self.ic4)
           self.label4.config(font=('Helvectica',round((mw*0.00625)+3),'bold')) 


       
        
class Task(Main,Financial):
     def __init__(self,object1,object2):
         self.n=object2.top
         self.x=object1.b
         self.bc=object1.label
         
         
     def close(self):
         root.deiconify()
         self.x.config(command=lambda:self.n.deiconify())
         try:
           self.n.iconify()
         except tkinter.TclError:
             pass
class FLASHWINFO(ctypes.Structure):
     _fields_=[('cbSize',ctypes.c_uint),
               ('hwnd',ctypes.c_uint),
               ('dwFlags',ctypes.c_uint),
               ('dwTimeout',ctypes.c_uint)]

GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080

def close2(event):
    root.destroy()
def set(window):
    j=ctypes.windll.user32.GetParent(window.winfo_id())
    style=ctypes.windll.user32.GetWindowLongPtrW(j,GWL_EXSTYLE)
    style=style & -WS_EX_TOOLWINDOW
    style=style | WS_EX_APPWINDOW
    res=ctypes.windll.user32.SetWindowLongPtrW(j,GWL_EXSTYLE,style)
    window.withdraw()
    window.after(10,lambda:window.deiconify())
    #window.grab_set()
    #window.attributes('-topmost',True)
    
    
        
count1=0
counter=0
master=Financial(root)
main=Memo(root)
first=Main(master)
second=Task(first,master)
third=Login(master)


lgh=[]
h=[]       
h1=[]
h2=[]
h3=[]
h4=[]
h5=[]
h6=[]
h7=[]
h8=[]
h10=[]
h11=[]
test=[]
test2=[]
kist = []
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]
graph=[]

root.bind('<Alt-F4>',close2)
root.update()

#root.bind('<Enter>',master.logined)
if __name__=='__main__':
      freeze_support()
      root.after(10,lambda:set(root))
      third.splash()

      mainloop()
