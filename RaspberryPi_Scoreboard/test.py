from tkinter import *
from tkinter import ttk
import datetime

root = Tk()

lab = Label(root)
lab.pack()

score = IntVar()
score.set(0)
lab.config(text = str(score))
def update():
    newScore = score.get()
    newScore += 10
    score.set(newScore)
    lab.config(text = str(newScore))
    root.update()
btn = ttk.Button(root, text = "Update Score", command = update)
btn.pack()
# run first time

root.mainloop()