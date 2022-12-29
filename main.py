from tkinter import *
from tkinter import messagebox
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_list = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    global letters
    global symbols
    global numbers

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(r"password_manager.json", mode="r") as pw_manager:
                data = json.load(pw_manager)
                data.update(new_data)

            with open(r"password_manager.json", mode="w") as pw_manager:
                json.dump(data, pw_manager, indent=4)

        except FileNotFoundError:
            with open(r"password_manager.json", mode="w") as pw_manager:
                json.dump(new_data, pw_manager, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_data():
    website = website_entry.get()

    try:
        with open(r"password_manager.json", mode="r") as pw_manager:
            data = json.load(pw_manager)
            email = data[website]["email"]
            password = data[website]["password"]
    except:
        messagebox.showinfo(title="Error", message="No data found.")
    else:
        messagebox.showinfo(title="Password Manager", message=f"Website: {website}\nEmail: {email}\nPassword: "
                                                              f"{password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "vpoole21@icloud.com")
password_entry = Entry(width=45)
password_entry.grid(row=3, column=1, columnspan=2)

# buttons
gener_password_button = Button(text="Generate Password",  command=password_generator)
gener_password_button.grid(row=3, column=3)
add = Button(text="Add", width=40, command=save)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", command=search_data, width=15)
search.grid(row=1, column=3)

window.mainloop()