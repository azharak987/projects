from tkinter import *
from tkinter.ttk import *

from gpiozero import Button
from signal import pause
from random import choice
import glob2
import subprocess
import keyboard
import re

window = Tk()
frame= Frame(window)
frame.pack()
video_frame = Frame(window)
video_frame.pack_forget()
images_frame = Frame(window)
images_frame.pack_forget()
window.geometry("1280x720")
videos_names = []
images_names = []

def loadVideos():
    videos = []
    for file in glob2.glob("/home/pi/Videos/*.mp4"):
        videos.append(file)
    for items in videos:
        x = re.split("\/", items, 4)
        videos_names.append(x[4])
    videos_names.append(videos_names[0])
    print(videos_names)
def loadImages():
    images = []
    for file in glob2.glob("/home/pi/Pictures/*.jpg"):
        images.append(file)
    for items in images:
        x = re.split("\/", items, 4)
        images_names.append(x[4])
    images_names.append(images_names[0])
    print(images_names)
def stop_video():
    keyoard.press_and_release('q')
    
def pause_video():
    keyboard.press_and_release('space')


play = Button(2)
stop = Button(3)
pause = Button(4)
loadVideos()
loadImages()

'''try:
    play.when_pressed = play_video
    stop.when_pressed = stop_video
    pause.when_pressed = pause_video
except KeyboardInterrupt:
    print("\nEXIT")'''
#Function to get the Radio Buttons Values
def btnVal(radVal):
    if radVal == 1:
        print("Images")
        frame.pack_forget()
        images_frame.pack()
    elif radVal == 2:
        print("Videos")
        frame.pack_forget()
        video_frame.pack()
    else:
        print("Incorrect Value")
        print(radVal.get())

radVal = IntVar()
vidVar = StringVar(window)
vidVar.set(videos_names[0])
imgVar = StringVar(window)
imgVar.set(images_names[0])
def play():
    toPlay = vidVar.get()
    print(toPlay)
    name_vid = "/home/pi/Videos/"+toPlay
    subprocess.Popen(['omxplayer',(name_vid)])
    
def show():
    to_show = imgVar.get()
    print(to_show)
    name_img = "/home/pi/Pictures/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
        
def back(val):
    if val == 'i':
        images_frame.pack_forget()
        frame.pack()
    elif val == 'v':
        video_frame.pack_forget()
        frame.pack()
ChooseOptionIV = Label(frame, text = "What do you want to play?", font=("Arial", 25))
ChooseOptionIV.grid(row = 0, column = 0, padx = 50, pady = (400,10))

imagesBtn = ttk.Button(frame, text = "Images", command = lambda: btnVal(1))
imagesBtn.grid(row = 1, column = 0, padx = 100, pady = 10)

videosBtn = ttk.Button(frame, text = "Videos", command = lambda: btnVal(2))
videosBtn.grid(row = 2, column = 0, padx = 100, pady = 10)

videoLabel = Label(video_frame, text = "Choose Video: ", font = ("Arial", 15))
videoLabel.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

videosMenu = OptionMenu(video_frame, vidVar, *videos_names)
videosMenu.grid(row = 1, column = 3, padx = 10, pady = (10,10))

videoMenuPlay = ttk.Button(video_frame, text = "Play", command = play)
videoMenuPlay.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

vid_back = ttk.Button(video_frame, text = "Back", command = lambda: back('v'))
vid_back.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

imgLabel = Label(images_frame, text = "Choose Image: ", font = ("Arial", 15))
imgLabel.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

imgMenu = OptionMenu(images_frame, imgVar, *images_names)
imgMenu.grid(row = 1, column = 3, padx = 10, pady = (10,10))

imgMenuPlay = ttk.Button(images_frame, text = "Show", command = show)
imgMenuPlay.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

img_back = ttk.Button(images_frame, text = "Back", command = lambda: back('i'))
img_back.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
window.mainloop()