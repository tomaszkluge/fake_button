from tkinter import *
import random

t = Tk()
t.title("Choose button")
t.geometry("300x350")

buttons = []
label = None


def win():
    for i in buttons:
        i.destroy()
    global label
    label = Label(t, text="Correct button")
    label.pack(fill=BOTH, expand=YES)
    t.after(5000, restart)


def loose():
    for i in buttons:
        i.destroy()
    global label
    label = Label(t, text="Wrong button")
    label.pack(fill=BOTH, expand=YES)
    t.after(1000, restart)


def insert_buttons():
    quantity = 5
    global buttons
    correct = random.randint(0, quantity-1)
    for i in range(quantity):
        if i == correct:
            buttons.append(Button(t, text="click me", command=win))
        else:
            buttons.append(Button(t, text="click me", command=loose))
    for i in buttons:
        i.pack(fill=BOTH, expand=YES)


insert_buttons()


def restart():
    label.destroy()
    buttons.clear()
    insert_buttons()


t.mainloop()
