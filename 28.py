import tkinter as tk

mainwindow=tk.Tk()
mainwindow.title('CALCULATOR')
label=tk.Label(mainwindow,text='Enter first number')
label.pack()
first=tk.Entry(mainwindow)
first.pack()

label1=tk.Label(mainwindow,text='Enter second number')
label1.pack()
second=tk.Entry(mainwindow)
second.pack()


def addition():
    num1=float(first.get())
    num2=float(second.get())
    result=float((num1+num2))
    result_label.config(text='operation result is' + str(result))
def substraction():
    num1=float(first.get())
    num2=float(second.get())
    result=float((num1-num2))
    result_label.config(text='operation result is' + str(result))

def multiplication():
    num1=float(first.get())
    num2=float(second.get())
    result=float((num1*num2))
    result_label.config(text='operation result is'+str(result))

def division():
    num1=float(first.get())
    num2=float(second.get())
    if (num2==0):
        result_label.config(text='invalid input "cannot divide" second number is 0 ')
    else:
        result = float((num1 / num2))
        result_label.config(text='operation result is' + str(result))

label2=tk.Label(mainwindow,text='operations')
label2.pack()
button=tk.Button(mainwindow,text='+',command=lambda: addition())
button.pack()
button1=tk.Button(mainwindow,text='-',command=lambda: substraction())
button1.pack()
button2=tk.Button(mainwindow,text='*',command=lambda: multiplication())
button2.pack()
button3=tk.Button(mainwindow,text='/',command=lambda: division())
button3.pack()

result_label=tk.Label(mainwindow, text="Operations result is:")
result_label.pack()

mainwindow.mainloop()
