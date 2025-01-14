from tkinter import *
import random, string
import pyperclip
from tkinter import messagebox

root = Tk()
root.geometry("500x450")
root.title("Random Password Generator")

title = StringVar()
labelframe = Label(root, textvar=title).pack()
title.set("Password Strength")

def select():
    select = choice.get()

choice = IntVar()
r1 = Radiobutton(root, text="Weak", var=choice, value=1, command=select).pack(anchor=CENTER)
r2 = Radiobutton(root, text="Good", var=choice, value=2, command=select).pack(anchor=CENTER)
r3 = Radiobutton(root, text="Strong", var=choice, value=3, command=select).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

lenlabel = StringVar()
lenlabel.set("Password Length")
lentitle = Label(root, textvar=lenlabel).pack()
val = IntVar()
spinlength = Spinbox(root, from_=6, to_=14, textvar=val, width=15).pack()

customlabel = Label(root, text="Customize Password Generation")
customlabel.pack()

exclude_uppercase = IntVar()
exclude_uppercase_checkbox = Checkbutton(root, text="Exclude Uppercase Letters", variable=exclude_uppercase)
exclude_uppercase_checkbox.pack()

exclude_lowercase = IntVar()
exclude_lowercase_checkbox = Checkbutton(root, text="Exclude Lowercase Letters", variable=exclude_lowercase)
exclude_lowercase_checkbox.pack()

exclude_digits = IntVar()
exclude_digits_checkbox = Checkbutton(root, text="Exclude Digits", variable=exclude_digits)
exclude_digits_checkbox.pack()

exclude_symbols = IntVar()
exclude_symbols_checkbox = Checkbutton(root, text="Exclude Symbols", variable=exclude_symbols)
exclude_symbols_checkbox.pack()

def callback():
    Isum.config(text=passgen())

def copy_to_clipboard():
    password = Isum.cget("text")
    if password!="":
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard")
    else:
        messagebox.showerror("Error", "No password generated")

passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=4)
passgenButton.pack()
Isum = Label(root, text="")
Isum.pack(side=BOTTOM)

copyButton = Button(root, text="Copy to Clipboard", command=copy_to_clipboard, pady=4)
copyButton.pack()

weak = string.ascii_uppercase + string.ascii_lowercase
good = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """~!@#$%&()*_- +{}[]?/"""
strong = weak + good + symbols

def passgen():
    characters = ""
    if exclude_uppercase.get() == 0:
        characters += string.ascii_uppercase
    if exclude_lowercase.get() == 0:
        characters += string.ascii_lowercase
    if exclude_digits.get() == 0:
        characters += string.digits
    if exclude_symbols.get() == 0:
        characters += symbols

    if choice.get() == 1:
        if len(characters) < 6:
            return "Error: Password length should be at least 6 characters."
        return "".join(random.sample(characters, val.get()))
    elif choice.get() == 2:
        if len(characters) < 10:
            return "Error: Password length should be at least 10 characters."
        if not (any(c.isupper() for c in characters) and any(c.islower() for c in characters) and any(c.isdigit() for c in characters)):
            return "Error: Password should contain at least one uppercase letter, one lowercase letter, and one digit."
        return "".join(random.sample(characters, val.get()))
    elif choice.get() == 3:
        if len(characters) < 14:
            return "Error: Password length should be at least 14 characters."
        if not (any(c.isupper() for c in characters) and any(c.islower() for c in characters) and any(c.isdigit() for c in characters) and any(c in symbols for c in characters)):
            return "Error: Password should contain at least one uppercase letter, one lowercase letter, one digit, and one symbol."
        return "".join(random.sample(characters, val.get()))

root.mainloop()

