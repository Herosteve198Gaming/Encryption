from tkinter import *
from tkinter.ttk import *
from tkinter import Radiobutton
import random
import pyperclip


win = Tk()
win.title("Password Generator")
win.geometry('450x75')

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
strength = StringVar()
strength.set("Low")
characters = lower

def Copy(string):
    pyperclip.copy(str(string))
    print(str(string))

def generate(string):
    global entpassword, comlength, password
    password = ""
    a = comlength.get()
    length = int(a)
    for i in range(0, length, 1):
        a = random.choice(string)
        password = password+a
    entpassword.delete(0, END)
    entpassword.insert(0, password)

def createpass(*args):
    global characters
    generate(characters)

def encrypt():
    global characters, encryption, entpassword
    Key = 13
    encryption = ""
    password = entpassword.get()
    for i in range(0, len(password)):
        char = password[i]
        for i2 in range(0, len(characters)):
            if char == characters[i2]:
                if i > 0:
                    for i3 in range(0, len(characters)):
                        if password[i-1] == characters[i3]:
                            index2 = i3
                else:
                    index2 = 0
                index = ((i2 + Key)+index2) % len(characters)
                encryption = encryption+characters[index]
    entencrypt.delete(0, END)
    entencrypt.insert(0, encryption)

def decrypt():
    global characters, entencrypt, entpassword
    Key = 13
    password = ""
    encryption = entencrypt.get()
    for i in range(0, len(encryption)):
        char = encryption[i]
        for i2 in range(0, len(characters)):
            if char == characters[i2]:
                if i > 0:
                    for i3 in range(0, len(characters)):
                        if password[i-1] == characters[i3]:
                            index2 = i3
                else:
                    index2 = 0
                index = ((i2 - Key)-index2) % len(characters)
                password = password+characters[index]
    entpassword.delete(0, END)
    entpassword.insert(0, password)

def setup(f):
    global lblpassword, lbllength, entpassword, comlength, btnpasscopy, btngenerate, radlow, radmedium, radstrong, lblencrypt, entencrypt, btnencrcopy, btnencrypt, btndecrypt
    if f == 0:
        lblpassword = Label(win, text="Password:")
        lbllength = Label(win, text="Length:")
        lblencrypt = Label(win, text="Encrypt:")
        entpassword = Entry(win, width=20)
        entencrypt = Entry(win, width=20)
        comlength = Combobox(win, width=17)
        comlength['values'] = (6,7 ,8 ,9 ,10)
        comlength.current(2)
        btnpasscopy = Button(win, text="Copy", command= lambda: Copy(entpassword.get()))
        btnencrcopy = Button(win, text="Copy", command= lambda: Copy(entencrypt.get()))
        btngenerate = Button(win, text="Generate", command= createpass)
        btnencrypt = Button(win, text="Encrypt", command= encrypt)
        btndecrypt = Button(win, text="Decrypt", command= decrypt)
        radlow = Radiobutton(win, text= "Low", value="Low", variable=strength)
        radmedium = Radiobutton(win, text= "Medium", value="Medium", variable=strength)
        radstrong = Radiobutton(win, text= "Strong", value="Strong", variable=strength)
    elif f == 1:
        lblpassword.grid(column=0, row=0)
        lbllength.grid(column=0, row=1)
        entpassword.grid(column=1, row=0)
        comlength.grid(column=1, row=1)
        btnpasscopy.grid(column=2, row=0)
        btngenerate.grid(column=3, row=0)
        btnencrcopy.grid(column=2, row=2)
        btnencrypt.grid(column=3, row=2)
        btndecrypt.grid(column=4, row=2)
        radlow.grid(column=2, row=1)
        radmedium.grid(column=3, row=1)
        radstrong.grid(column=4, row=1)
        lblencrypt.grid(column=0, row=2)
        entencrypt.grid(column=1, row=2)

setup(0)
setup(1)

def radpress(*args):
    global strength, radlow, radmedium, radstrong, lower, upper, digits, characters
    s = strength.get()
    if s == "Low":
        radlow.config(fg="red")
        radmedium.config(fg="black")
        radstrong.config(fg="black")
        characters = lower
    elif s == "Medium":
        radlow.config(fg="black")
        radmedium.config(fg="red")
        radstrong.config(fg="black")
        characters = upper
    elif s == "Strong":
        radlow.config(fg="black")
        radmedium.config(fg="black")
        radstrong.config(fg="red")
        characters = digits

strength.trace("w", radpress)
win.mainloop()
