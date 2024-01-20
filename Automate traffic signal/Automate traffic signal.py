from tkinter import *
from time import sleep


def red():
    canvas1.create_oval(120, 120, 40, 30, outline="white", fill="red", width=4)
    canvas2.create_oval(120, 120, 40, 30, outline="white", fill="white", width=4)
    canvas3.create_oval(120, 120, 40, 30, outline="white", fill="white", width=4)


def orange():
    canvas1.create_oval(120, 120, 40, 30, outline="white", fill="white", width=4)
    canvas2.create_oval(120, 120, 40, 30, outline="white", fill="orange", width=4)
    canvas3.create_oval(120, 120, 40, 30, outline="white", fill="white", width=4)


def green():
    canvas1.create_oval(120, 120, 40, 30, outline="white", fill="white", width=4)
    canvas2.create_oval(120, 120, 40, 30, outline="white", fill="white", width=4)
    canvas3.create_oval(120, 120, 40, 30, outline="white", fill="green", width=4)


count = 60
def start():
    counter(count)


def new(c):
    if c >= 40:
        red()
        interval.config(text=c)
        play.update()
        sleep(1)
        counter(c)

    elif 40 > c >= 20:
        orange()
        interval.config(text=c)
        play.update()
        sleep(1)
        counter(c)

    elif 20 > c > 0:
        green()
        if c < 10:
            interval.config(text=f'0{c}')
        else:
            interval.config(text=c)
        play.update()
        sleep(1)
        counter(c)
    else:
        red()
        count = 60
        interval.config(text=c)
        play.update()
        sleep(1)
        counter(count)


def counter(timer):
    if timer > 0:
        timer = timer - 1
        new(timer)


play = Tk()
play.geometry('340x500')
play.title("Traffic Lights - Automatic Control")
play.configure(bg='lightblue')


# adding buttons
Button(play, text='Start', font=('calibri', 13), command=start, bg='gray', width='12', height='2').place(x=10, y=70)
head = Label(play, text='Automate Traffic Signal', font=('calibri', 25, 'bold'), bg='black', fg='white')
head.place(x=10, y=10)
interval = Label(play, text='', font=('calibri', 25, 'bold'), bg='black', fg='red', width='5')
interval.place(x=10, y=270)


# adding canvas -> container:
canvas1 = Canvas(play, height=140, width=160, bg='black')
canvas1.place(x=150, y=65)

canvas2 = Canvas(play, height=140, width=160, bg='black')
canvas2.place(x=150, y=207)

canvas3 = Canvas(play, height=140, width=160, bg='black')
canvas3.place(x=150, y=350)


play.mainloop()