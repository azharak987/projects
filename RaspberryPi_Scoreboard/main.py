from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import RPi.GPIO as GPIO
window = Tk()
startFlag = IntVar()
startFlag.set(0)
score = IntVar()
score.set(0)
time = IntVar()
time.set(1000)

#First Frame for the initial Screen
firstFrame = tk.Frame(window)
firstFrame.pack()

#Score board frame
scoreFrame = Frame(window)
scoreFrame.pack_forget()

w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
#Variables for Score and Timer

scoreStr = StringVar()
scoreStr = str(score.get())
timeStr = StringVar()
timeStr = time.get()

def startFtn():
    firstFrame.pack_forget()
    scoreFrame.pack()
    time.set(120)
    score.set(0)
    scoreChangeLbl.config(text = str(score.get()))
    timeChangeLbl.config(text = str(time.get()))
    window.update()
    if startFlag.get() > 0:
        timer()
    startFlag.set(1)

def updateScore(score_):
    newScore = score.get()
    newScore += 10
    score.set(newScore)
    scoreChangeLbl.config(text=str(newScore))
    window.update()

def timer():
    if time.get() != 0:
        time1 = time.get() - 1
        time.set(time1)
        timeSStr =  str(time1)
        timeChangeLbl.config(text = timeSStr)
        window.after(1000, timer) # run itself again after 1000 ms
    elif time.get() == 0:
        if startFlag.get() > 0:
            messagebox.showinfo("Time Up","Your Score is " + str(score.get()))
            scoreFrame.pack_forget()
            firstFrame.pack()
            startFlag.set(startFlag.get()+1)
            time.set(9999)

def tester():
    #print("I am tester")
    window.after(5000, tester)
background = PhotoImage(file = "ssLogo.png")
label = Label(window, image = background)
label.place(relx=0.35, rely=0.2, anchor=CENTER)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.add_event_detect(7, GPIO.RISING, callback = updateScore)

startLbl = Label(firstFrame, text = "Push Button to Start", font = ("Arial", 50))
startLbl.grid(row = 1, column = 1, padx = 100, pady = (400, 10))
startBtn = ttk.Button(firstFrame, text = "Start", command = startFtn)
startBtn.grid(row = 2, column = 1, padx = 100, pady = (10, 10))

timeLbl = Label(scoreFrame, text = "Time", font = ("Times", 80))
timeLbl.grid(row = 1, column = 0, padx = 50, pady = (400, 10))


scoreLbl = Label(scoreFrame, text = "Score", font = ("Times", 80))
scoreLbl.grid(row = 1, column = 3, padx = (300, 50) , pady = (400, 10))

scoreChangeLbl = Label(scoreFrame, text= scoreStr, font = ("Times", 80))
scoreChangeLbl.grid(row = 2, column = 3, padx = (300, 50) , pady = (10, 10))

timeChangeLbl = Label(scoreFrame, text = timeStr, font = ("Times", 80))
timeChangeLbl.grid(row = 2, column = 0, padx = 50, pady = (10, 10))

#testButton = ttk.Button(scoreFrame, text = "Update Score", command = updateScore)
#testButton.grid(row = 3, column = 2)
timer()
tester()
window.mainloop()
