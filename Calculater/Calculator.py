from tkinter import *

cal = Tk()
cal.geometry('320x580')
cal.title("Calculator")
cal.config(bg="black")

Label(cal, text="Calculator", bg='lightblue', fg='black', width='40', font=('calibri', '12', 'bold')).grid(row='1', column='1', columnspan='4')

Button(cal, text='CE', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='4', column='1')
Button(cal, text='C', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='4', column='2')
Button(cal, text='DEL', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='4', column='3')
Button(cal, text='/', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='4', column='4')

Button(cal, text='7', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='5', column='1')
Button(cal, text='8', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='5', column='2')
Button(cal, text='9', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='5', column='3')
Button(cal, text='x', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='5', column='4')

Button(cal, text='4', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='6', column='1')
Button(cal, text='5', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='6', column='2')
Button(cal, text='6', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='6', column='3')
Button(cal, text='-', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='6', column='4')

Button(cal, text='1', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='7', column='1')
Button(cal, text='2', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='7', column='2')
Button(cal, text='3', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='7', column='3')
Button(cal, text='+', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='7', column='4')

Button(cal, text='%', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='8', column='1')
Button(cal, text='0', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='8', column='2')
Button(cal, text='.', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='8', column='3')
Button(cal, text='=', bg='white', width='9', font=('calibri', '12', 'bold'), height='4').grid(row='8', column='4')

canvas_1 = Canvas(cal, height='100', width='320').grid(row='2', column='1', columnspan='4')

cal.mainloop()