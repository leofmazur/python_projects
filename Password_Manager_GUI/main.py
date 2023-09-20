from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# from pathlib import Path

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Message", message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it OK to save it?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# def save():
#
#     my_file = Path("C:/Users/mazur/OneDrive/Documents/Python/Password_Manager_GUI/data.txt")
#
#     if my_file.is_file():
#         input_website = website_entry.get()
#         with open("data.txt", "a") as data:
#             data.write(input_website + " | ")
#         website_entry.delete(0, 'end')
#
#         input_email = email_entry.get()
#         with open("data.txt", "a") as data:
#             data.write(input_email + " | ")
#
#         input_password = password_entry.get()
#         with open("data.txt", "a") as data:
#             data.write(input_password + "\n")
#         password_entry.delete(0, 'end')
#     else:
#         input_website = website_entry.get()
#         file_name = str("data" ".txt")
#         text_file = open(file_name, "w")
#         text_file.write(input_website + " | ")
#         website_entry.delete(0, 'end')
#
#         input_email = email_entry.get()
#         file_name = str("data" ".txt")
#         text_file = open(file_name, "a")
#         text_file.write(input_email + " | ")
#
#         input_password = password_entry.get()
#         file_name = str("data" ".txt")
#         text_file = open(file_name, "a")
#         text_file.write(input_password + "\n")
#         text_file.close()
#         password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ENTRIES
website_input = StringVar()
website_entry = Entry(window, textvariable=website_input, width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_input = StringVar()
email_entry = Entry(window, textvariable=email_input, width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mazur.leonardo@outlook.com")

password_entry = StringVar()
password_entry = Entry(window, textvariable=password_entry, width=35, show="*")
password_entry.grid(column=1, row=3)

# BUTTONS
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=6)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=7, columnspan=2)

window.mainloop()
