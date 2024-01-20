from tkinter import *
import random as rd
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    file = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file = pd.read_csv("data/data_file.csv")

word = file.to_dict(orient="records")
rand_word = {}


def right_key():
    global rand_word, flip_timer
    window.after_cancel(flip_timer)
    rand_word = rd.choice(word)
    english_word = rand_word["English"]
    canvas.itemconfig(text1, text="English", fill="black")
    canvas.itemconfig(text2, text=english_word, fill="black")
    canvas.itemconfig(card_image, image=image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(text1, text="Tamil", fill='white')
    canvas.itemconfig(card_image, image=img)
    canvas.itemconfig(text2, text=f'{rand_word["Tamil"]}', fill='white')


def is_known():
    word.remove(rand_word)
    data = pd.DataFrame(word)
    data.to_csv("data/words_to_learn.csv", index=False)
    right_key()


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
image = PhotoImage(file="images/card_front.png")
img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
text1 = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
text2 = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=right_key)
wrong_button.config(highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=is_known)
right_button.config(highlightthickness=0)
right_button.grid(row=1, column=1)

right_key()


window.mainloop()