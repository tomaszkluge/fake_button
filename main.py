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
            buttons.append(Button(t, text="click me", command="win"))
        else:
            buttons.append(Button(t, text="click me", command="loose"))



