from tkinter import *
def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)
def btnclearDisplay():
    global operator
    operator=" "
    text_input.set(" ")
def btnequalsinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

cal=Tk()

cal.title("My Calculator")
operator=""
text_input=StringVar()
txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=30,
                 insertwidth=3,bg='powder blue',justify='right').grid(columnspan=4)
btn7=Button(cal,text='7',command=lambda:btnclick(7) ,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=1,column=0)
btn8=Button(cal,text='8',command=lambda:btnclick(8),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=1,column=1)
btn9=Button(cal,text='9',command=lambda:btnclick(9),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=1,column=2)
Addition=Button(cal,text='+',command=lambda:btnclick('+'),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
                bg='powder blue').grid(row=1,column=3)
#_____________________________________________________
btn4=Button(cal,text='4',command=lambda:btnclick(4),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=2,column=0)
btn5=Button(cal,text='5',command=lambda:btnclick(5),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=2,column=1)
btn6=Button(cal,text='6',command=lambda:btnclick(6),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=2,column=2)
substraction=Button(cal,text='-',command=lambda:btnclick('-'),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
                    bg='powder blue').grid(row=2,column=3)
#__________________________________________________________________
btn1=Button(cal,text='1',command=lambda:btnclick(1),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=3,column=0)
btn2=Button(cal,text='2',command=lambda:btnclick(2),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=3,column=1)
btn3=Button(cal,text='3',command=lambda:btnclick(3),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=3,column=2)
Multiplication=Button(cal,text='*',command=lambda:btnclick('*'),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
                      bg='powder blue').grid(row=3,column=3)
#-------------------------------------------------------------------
btn0=Button(cal,text='0',command=lambda:btnclick(0),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            bg='powder blue').grid(row=4,column=0)
clear=Button(cal,text='c',command=btnclearDisplay,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
             bg='powder blue').grid(row=4,column=1)
equalto=Button(cal,text='=',command=btnequalsinput,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               bg='powder blue').grid(row=4,column=2)
Division=Button(cal,text='/',command=lambda:btnclick('/'),padx=16,bd=8,fg='black',font=('arial',20,'bold'),
                bg='powder blue').grid(row=4,column=3)
cal.mainloop()

