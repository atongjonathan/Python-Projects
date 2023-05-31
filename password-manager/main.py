from random import choice, shuffle, randint
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letter

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode='r') as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo("Error", message="No data file found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


def save():
    is_ok = False
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:
        {
            "email": email,
            "password": password
        }
    }
    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"These are the details entered :\nEmail: {email},\nPassword:{password}\n"
                                               f"Is it Ok to save?")
    if is_ok:
        try:
            with open("data.json", mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", mode='w') as file:
                data.update(new_data)
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=lock_img)
canvas.grid(column=2, row=1)
# Labels
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

email_label = Label(text="Email/User  name:")
email_label.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# Entries
website_entry = Entry(width=17)
website_entry.grid(column=2, row=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "atongjonathan@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=2, row=4)

# Buttons
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=2, row=5, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=3, row=2)
window.mainloop()
