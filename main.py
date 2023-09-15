import random
from tkinter import *
import random

t = Tk()
t.title("Choose button")
t.geometry("300x350")


def insert_buttons():
    quantity = 8
    global buttons
    buttons = []
    correct = random.randint(0, quantity-1)
    for i in range(quantity):
        if i == correct:
            buttons.append(Button(t, text="click me", command=win))
        else:
            buttons.append(Button(t, text="click me", command=loose))
    for i in buttons:
        i.pack(fill=BOTH, expand=YES)

    insert_buttons()


def win():
    for i in buttons:
        i.destroy()
    global label
    label = Label(t, text="Correct button")
    label.pack(fill=BOTH, expand=YES)
    t.after(5000, restart)


def restart():
    label.destroy()
    insert_buttons()


def crate():
    for i in buttons:
        i.destroy()
        global label
        label = Label(t, text="Wrong button")
        label.pack(fill=BOTH, expand=YES)
        t.after(5000, restart)


