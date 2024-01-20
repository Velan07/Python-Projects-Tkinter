from tkinter import *


def red():
    canvas1.create_oval(120, 120, 30, 30, outline="white", fill="red", width=4)
    canvas2.create_oval(120, 120, 30, 30, outline="white", fill="white", width=4)
    canvas3.create_oval(120, 120, 30, 30, outline="white", fill="white", width=4)


def orange():
    canvas1.create_oval(120, 120, 30, 30, outline="white", fill="white", width=4)
    canvas2.create_oval(120, 120, 30, 30, outline="white", fill="orange", width=4)
    canvas3.create_oval(120, 120, 30, 30, outline="white", fill="white", width=4)


def green():
    canvas1.create_oval(120, 120, 30, 30, outline="white", fill="white", width=4)
    canvas2.create_oval(120, 120, 30, 30, outline="white", fill="white", width=4)
    canvas3.create_oval(120, 120, 30, 30, outline="white", fill="green", width=4)


play = Tk()
play.geometry('340x500')
play.title("Traffic Lights - Manual Control")
play.configure(bg='lightblue')


# adding buttons
Button(play, font=('calibri', 13), command=red, bg='red', width='12', height='2').place(x=10, y=30)
Button(play, font=('calibri', 13), command=orange, bg='orange', width='12', height='2').place(x=10, y=180)
Button(play, font=('calibri', 13), command=green, bg='green', width='12', height='2').place(x=10, y=330)


# adding canvas -> container:
canvas1 = Canvas(play, height=140, width=160, bg='black')
canvas1.place(x=150, y=30)

canvas2 = Canvas(play, height=140, width=160, bg='black')
canvas2.place(x=150, y=180)

canvas3 = Canvas(play, height=140, width=160, bg='black')
canvas3.place(x=150, y=330)


play.mainloop()