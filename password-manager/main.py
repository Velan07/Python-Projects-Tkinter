import json
from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_list = [choice(letters) for _ in range(randint(8, 10))]

    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    pass_word = ''.join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, f"{pass_word}")
    pyperclip.copy(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site_name = input_website_name.get()
    name = input_user_name.get()
    pw = input_password.get()

    new_data = {
        site_name: {
            "email": name,
            "password": pw
        }
    }

    if len(site_name) == 0 or len(name) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("new_file.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("new_file.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("new_file.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            input_website_name.delete(0, END)
            input_password.delete(0, END)
            input_user_name.delete(0, END)


# ---------------------------- PASSWORD SEARCH ------------------------------- #


def find_password():
    site_name = input_website_name.get()
    try:
        with open("new_file.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if site_name in data:
            messagebox.showinfo(title="Details", message=f"E-mail: {data[site_name]['email']}\n"
                                                         f"Password: {data[site_name]['password']}")
        else:
            messagebox.showerror(title="Error", message="No details from the website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
user_name = Label(text="E-mail/Username:")
user_name.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

input_website_name = Entry(width=32)
input_website_name.grid(row=1, column=1)
input_website_name.focus()
input_user_name = Entry(width=50)
input_user_name.grid(row=2, column=1, columnspan=2)
input_password = Entry(width=32)
input_password.grid(row=3, column=1)

pw_generate_button = Button(text="Generate Password", command=generate_password)
pw_generate_button.grid(row=3, column=2)
add_to_database = Button(text="Add", width=20, command=save)
add_to_database.grid(row=4, column=1)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()