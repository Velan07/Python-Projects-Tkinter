from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


def calc():
    miles = entry_1.get()
    km = int(miles)*1.609344
    label_3.config(text=str(km))


entry_1 = Entry(width=20, text=0)
entry_1.grid(row=0, column=1, padx=10, pady=10)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2, padx=10, pady=10)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0, padx=10, pady=10)

label_3 = Label(text="0")
label_3.grid(row=1, column=1, padx=10, pady=10)

label_4 = Label(text="Km")
label_4.grid(row=1, column=2, padx=10, pady=10)

button = Button(text="Calculate", command=calc)
button.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()