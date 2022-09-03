from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_lowercase)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave field empty!")
    else:
        user_input=messagebox.askokcancel(title=website,message=f"These are details entered: \nEmail:{email}"
                                                 f"\nPassword:{password}\nIs it ok to save?")

        if user_input:
            f = open("data.txt", 'a')
            f.write(f"{website} |{email} |{password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,112,image=img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:",font=("Arial",10))
website_label.grid(column=0,row=1)


website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_label=Label(text="Email/Username:",font=("Arial",10))
email_label.grid(column=0,row=2)

email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)

password_label=Label(text="Password:",font=("Arial",10))
password_label.grid(column=0,row=3)

password_entry=Entry(width=17)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",width=14,command=generate_password)
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=30,command=save,)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()
