from tkinter import *

 win=Tk()
 win.geometry('450x400')
 win.title('CALCULATOR')

 def myfun():
    a=int(enum1.get())
    b=int(enum2.get())
     lres.config(text=str(a+b), bg='sky blue')

 def myfun1():
     a = int(enum1.get())
     b = int(enum2.get())
     lres.config(text=str(a-b), bg='sky blue')

 def myfun2():
     a = int(enum1.get())
    b = int(enum2.get())
     lres.config(text=str(a*b), bg='sky blue')

 def myfun3():
     a = int(enum1.get())
     b = int(enum2.get())
     lres.config(text=str(a/b), bg='sky blue')

 def myfun4():
     a = int(enum1.get())
     b = int(enum2.get())
     lres.config(text=str(a//b), bg='sky blue')

 def myfun5():
   a = int(enum1.get())
     b = 0
     lres.config(text=str(a**2), bg='sky blue')

def myfun6():
     a = 0
    b = int(enum2.get())
   lres.config(text=str(b**2), bg='sky blue')

 num1=Label(win, text='Enter First Number', font='20')
 num1.place(x=20,y=20)

 enum1=Entry(win, bg='yellow',font='20')
 enum1.place(x=190,y=20)

 num1=Label(win, text='Enter Second Number', font='20')
  num1.place(x=20,y=80)

 enum2=Entry(win, bg='yellow',font='20')
 enum2.place(x=190,y=80)

 btn=Button(win,text='Addition',command=myfun, font='20')
 btn.place(x=50, y=140)

 btn=Button(win,text='Subtraction',command=myfun1, font='20')
 btn.place(x=150, y=140)

 btn=Button(win,text='Multiplication',command=myfun2, font='20')
 btn.place(x=280, y=140)

 btn=Button(win,text='Division',command=myfun3, font='20')
 btn.place(x=40, y=200)

 btn=Button(win,text='Floor Division',command=myfun4, font='20')
 btn.place(x=140, y=200)

 btn=Button(win,text='Square of First No.',command=myfun5, font='20')
 btn.place(x=275, y=200)

 btn=Button(win,text='Square of Second No.',command=myfun6, font='20')
 btn.place(x=130, y=260)

 r=Label(win, text='ANSWER', font='20')
 r.place(x=20, y=320)

 lres=Label(win,text="     ", bg='yellow',font='20')
 lres.place(x=100, y=320)


 win.mainloop()
