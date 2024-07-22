#!/usr/bin/env python3
import keyboard
import glob2
import subprocess
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from gpiozero import Button
#Making GUI guiWindow
guiWindow = Tk()
#Making three Frames
#.pack() show the myFrame, .pack_forget() hides the myFrame.
mainFrame = Frame(guiWindow)
mainFrame.pack()

frame_presentation = Frame(guiWindow)
frame_presentation.pack_forget()

frame_info = Frame(guiWindow)
frame_info.pack_forget()



frame_fitness = Frame(guiWindow)
frame_fitness.pack_forget()


frame_events = Frame(guiWindow)
frame_events.pack_forget()



frame_religious = Frame(guiWindow)
frame_religious.pack_forget()



frame_dining = Frame(guiWindow)
frame_dining.pack_forget()

frame_archive = Frame(guiWindow)
frame_archive.pack_forget()

frame_posters = Frame(guiWindow)
frame_posters.pack_forget()


#Setting the guiWindow geometry
w, h = guiWindow.winfo_screenwidth(), guiWindow.winfo_screenheight()
guiWindow.geometry("%dx%d+0+0" % (w, h))
bg =Image.open('/home/pi/Desktop/university.jpg')
background = ImageTk.PhotoImage(bg)
label = Label(guiWindow, image = background)
label.place(relx=0.5, rely=0.12, anchor=CENTER)
#Lists to store videos and images names
media_presentation = []
imagesList_presentation = []

media_info = []
imagesList_info = []

media_fitness = []
imagesList_fitness = []

media_events = []
imagesList_events = []

media_religious = []
imagesList_religious = []

imagesList_dining = []

media_archive = []
imagesList_archive = []

media_posters = []
imagesList_posters = []

#Function to load videos from the storage and store their names in the list
#Place your videos in /home/pi/Videos
def getPresentationVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Presentation/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        media_presentation.append(x[4])
    try:
        media_presentation.append(media_presentation[0])
    except:
        print("Error", "No video in Presentation Folder")
    print(media_presentation)
def getPresentationImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Presentation/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_presentation.append(x[4])
    '''try:
        imagesList_info.append(imagesList_presentation[0])
    except:
        messagebox.showerror("Error", "No image in Presentation Folder")'''
    print(imagesList_presentation)
def getInfoVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Info/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        media_info.append(x[4])
    try:
        media_info.append(media_info[0])
    except:
        print("Error", "No video in Info Folder")
    print(media_info)
def getInfoImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Info/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_info.append(x[4])
    '''try:
        imagesList_info.append(imagesList_info[0])
    except:
        messagebox.showerror("Error", "No images in Info Folder")'''
    print(imagesList_info)


def getFitnessVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Fitness/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        media_fitness.append(x[4])
    try:
        media_fitness.append(media_fitness[0])
    except:
        print("Error", "No Video in Fitness Folder")
    print(media_fitness)
def getFitnessImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Fitness/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_fitness.append(x[4])
    '''try:
        imagesList_fitness.append(imagesList_fitness[0])
    except:
        messagebox.showerror("Error", "No Images in Fitness Folder")'''
    print(imagesList_fitness)


def getEventsVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Events/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        media_events.append(x[4])
    try:
        media_events.append(media_events[0])
    except:
        print("Error", "No Video in Events Folder")
    print(media_events)
def getEventsImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Events/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_events.append(x[4])
    '''try:
        imagesList_events.append(imagesList_events[0])
    except:
        messagebox.showerror("Error", "No Image in Events Folder")'''
    print(imagesList_events)


def getReligiousVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Religious/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        media_religious.append(x[4])
    try:
        media_religious.append(media_religious[0])
    except:
        print("Error", "No Video in Religious Folder")
    print(media_religious)
def getReligiousImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Religious/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_religious.append(x[4])
    '''try:
        imagesList_religious.append(imagesList_religious[0])
    except:
        messagebox.showerror("Error", "No Image in Religious Folder")'''
    print(imagesList_religious)
    
    
def getDiningImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Dining/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_dining.append(x[4])
    try:
        imagesList_dining.append(imagesList_dining[0])
    except:
        print("Error", "No Image in Dining Folder")
    print(imagesList_dining)


def getArchiveVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Archive/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        media_archive.append(x[4])
    try:
        media_archive.append(media_archive[0])
    except:
        print("Error", "No Video in Archive Folder")
    print(media_archive)
def getArchiveImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Archive/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_archive.append(x[4])
    '''try:
        imagesList_archive.append(imagesList_archive[0])
    except:
        messagebox.showerror("Error", "No Image in Archive Folder")'''
    print(imagesList_archive)
    
def getPostersVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Posters_Under_the_Dome/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        media_posters.append(x[4])
    try:
        media_posters.append(media_posters[0])
    except:
        print("Error", "No video in Info Folder")
    print(media_posters)
def getPostersImages():
    myImages = []
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Posters_Under_the_Dome/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList_posters.append(x[4])
    '''try:
        imagesList_info.append(imagesList_posters[0])
    except:
        messagebox.showerror("Error", "No image in Posters Under the Dome Folder")'''
    print(imagesList_posters)
    
def mainFrameFtn(option):
    if option == "presentation":
        mainFrame.pack_forget()
        frame_presentation.pack()
    elif option == "info":
        mainFrame.pack_forget()
        frame_info.pack()
        
    elif option == "fitness":
        mainFrame.pack_forget()
        frame_fitness.pack()
        
    elif option == "events":
        mainFrame.pack_forget()
        frame_events.pack()
        
    elif option == "religious":
        mainFrame.pack_forget()
        frame_religious.pack()
        
    elif option == "dining":
        mainFrame.pack_forget()
        frame_dining.pack()
        
    elif option == "archive":
        mainFrame.pack_forget()
        frame_archive.pack()
    elif option == "posters":
        mainFrame.pack_forget()
        frame_posters.pack()
#Load videos and images
getPresentationVideos()
getPresentationImages()

getInfoVideos()
getInfoImages()

getFitnessVideos()
getFitnessImages()

getEventsVideos()
getEventsImages()

getReligiousVideos()
getReligiousImages()

getDiningImages()

getArchiveVideos()
getArchiveImages()

getPostersVideos()
getPostersImages()

for i in range(0, len(imagesList_presentation)):
    media_presentation.append(imagesList_presentation[i])
    
for i in range(0, len(imagesList_info)):
    media_info.append(imagesList_info[i])

for i in range(0, len(imagesList_fitness)):
    media_fitness.append(imagesList_fitness[i])

for i in range(0, len(imagesList_events)):
    media_events.append(imagesList_events[i])

for i in range(0, len(imagesList_religious)):
    media_religious.append(imagesList_religious[i])

media_dining = imagesList_dining
for i in range(0, len(imagesList_archive)):
    media_archive.append(imagesList_archive[i])

for i in range(0, len(imagesList_posters)):
    media_posters.append(imagesList_posters[i])
    
#Variables to store the option from option menu
ValueRAD = IntVar()
mediaOptionVal_presentation = StringVar(guiWindow)
try:
    mediaOptionVal_presentation.set(media_presentation[0])
except:
    messagebox.showerror("Error", "No Media in Presentation Folder")
    
mediaOptionVal_info = StringVar(guiWindow)
try:
    mediaOptionVal_info.set(media_info[0])
except:
    messagebox.showerror("Error", "No Media in Info Folder")
mediaOptionVal_fitness = StringVar(guiWindow)
try:
    mediaOptionVal_fitness.set(media_fitness[0])
except:
    messagebox.showerror("Error", "No Media in Fitness Folder")
mediaOptionVal_events = StringVar(guiWindow)
try:
    mediaOptionVal_events.set(media_events[0])
except:
    messagebox.showerror("Error", "No Media in Fitness Folder")
    
mediaOptionVal_religious = StringVar(guiWindow)
try:
    mediaOptionVal_religious.set(media_religious[0])
except:
    messagebox.showerror("Error", "No Media in Religious Folder")
    
mediaOptionVal_dining = StringVar(guiWindow)
try:
    mediaOptionVal_dining.set(media_dining[0])
except:
    messagebox.showerror("Error", "No Media in Dining Folder")
mediaOptionVal_archive = StringVar(guiWindow)
try:
    mediaOptionVal_archive.set(media_archive[0])
except:
    messagebox.showerror("Error", "No Media in Archive Folder")
mediaOptionVal_posters = StringVar(guiWindow)
try:
    mediaOptionVal_posters.set(media_posters[0])
except:
    messagebox.showerror("Error", "No Media in Posters Under the Dome Folder")

#Buttons, the arguments to the button function shows to which GPIO pin the button is connected
Btn_tab = Button(2)
Btn_arrowUP = Button(3)
Btn_pause = Button(4)
Btn_space = Button(17)
Btn_arrowDOWN = Button(27)
Btn_Q_Stop = Button(22)

    
def enableButton():
    PLAY_vid_menu_info["state"] = NORMAL
    PLAY_vid_menu_fitness["state"] = NORMAL
    PLAY_vid_menu_events["state"] = NORMAL
    PLAY_vid_menu_religious["state"] = NORMAL
    PLAY_vid_menu_archive["state"] = NORMAL

#Functions for the buttons
def tabBTN_ftn():
    keyboard.press_and_release('tab')
    enableButton()
def arrowUPBTN_ftn():
    keyboard.press_and_release('up')
    
def pauseBTN_ftn():
    keyboard.press_and_release('space')
    print("In Pause ftn")
    objPlayer.pause_video()
    return
def spaceBTN_ftn():
    keyboard.press_and_release('space')    
    
def arrowDOWNBTN_ftn():
    keyboard.press_and_release('down')

def stopBTN_ftn():
    keyboard.press_and_release('q')
    print("In Stop ftn")
    objPlayer.stop_video()
    return

#Class for video to play, pause and stop
class MyPlayer:
    
    omx = subprocess.Popen(['omxplayer',('')], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
    def play_presentation(self):
        toPlay = mediaOptionVal_presentation.get()
        print(toPlay)
        name_vid = "/home/pi/Presentation/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu_info["state"] = DISABLED
        return
    def play_info(self):
        toPlay = mediaOptionVal_info.get()
        print(toPlay)
        name_vid = "/home/pi/Info/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu_info["state"] = DISABLED
        return
    def play_fitness(self):
        toPlay = mediaOptionVal_fitness.get()
        print(toPlay)
        name_vid = "/home/pi/Fitness/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu_fitness["state"] = DISABLED
        return
    def play_events(self):
        toPlay = mediaOptionVal_events.get()
        print(toPlay)
        name_vid = "/home/pi/Events/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu_events["state"] = DISABLED
        return
    def play_religious(self):
        toPlay = mediaOptionVal_religious.get()
        print(toPlay)
        name_vid = "/home/pi/Religious/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu_religious["state"] = DISABLED
        return
    def play_archive(self):
        toPlay = mediaOptionVal_archive.get()
        print(toPlay)
        name_vid = "/home/pi/Archive/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu_archive["state"] = DISABLED
        return
    def play_posters(self):
        toPlay = mediaOptionVal_posters.get()
        print(toPlay)
        name_vid = "/home/pi/Posters_Under_the_Dome/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu_archive["state"] = DISABLED
        return
    def pause_video(self):
        MyPlayer.omx.stdin.write(b'p')
        print("Pause Video")
        return
    def stop_video(self):
        MyPlayer.omx.stdin.write(b'q')
        print("Stop Video")
        return

#Object initialization of MyPlayer Class
objPlayer = MyPlayer()



    
#Checking the buttons if pressed
try:
    Btn_tab.when_pressed = tabBTN_ftn
    Btn_arrowUP.when_pressed = arrowUPBTN_ftn   
    Btn_pause.when_pressed = pauseBTN_ftn
    Btn_space.when_pressed = spaceBTN_ftn
    Btn_arrowDOWN.when_pressed = arrowDOWNBTN_ftn
    Btn_Q_Stop.when_pressed = stopBTN_ftn
except KeyboardInterrupt:
    print("\nEXIT")

#These are the functions for GUI Buttons
#Calls the Play function to play the videos

def show_presentation():
    to_show = mediaOptionVal_presentation.get()
    print(to_show)
    name_img = "/home/pi/Presentation/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    frame_presentation.pack()

def show_info():
    to_show = mediaOptionVal_info.get()
    print(to_show)
    name_img = "/home/pi/Info/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    frame_info.pack()
    
def show_fitness():
    to_show = mediaOptionVal_fitness.get()
    print(to_show)
    name_img = "/home/pi/Fitness/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    frame_fitness.pack()
    
def show_events():
    to_show = mediaOptionVal_events.get()
    print(to_show)
    name_img = "/home/pi/Events/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    frame_events.pack()
    
def show_religious():
    to_show = mediaOptionVal_religious.get()
    print(to_show)
    name_img = "/home/pi/Religious/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    frame_religious.pack()
    
def show_dining():
    to_show = mediaOptionVal_dining.get()
    print(to_show)
    name_img = "/home/pi/Dining/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    frame_dining.pack()
    
def show_archive():
    to_show = mediaOptionVal_archive.get()
    print(to_show)
    name_img = "/home/pi/Archive/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    mainFrame.pack_forget()
    frame_archive.pack()

def show_posters():
    to_show = mediaOptionVal_posters.get()
    print(to_show)
    name_img = "/home/pi/Posters_Under_the_Dome/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    frame_posters.pack()
def play_presentation():
    media= mediaOptionVal_presentation.get()
    if media[-3:] == "mp4":
        objPlayer.play_presentation()
        frame_presentation.pack()
    elif media[-3:] == "jpg":
        show_presentation()
    return

def play_info():
    media= mediaOptionVal_info.get()
    if media[-3:] == "mp4":
        objPlayer.play_info()
        frame_info.pack()
    elif media[-3:] == "jpg":
        show_info()
    return
def play_fitness():
    media= mediaOptionVal_fitness.get()
    print(media[-3:])
    if media[-3:] == "mp4":
        objPlayer.play_fitness()
        frame_fitness.pack()
    elif media[-3:] == "jpg":
        show_fitness()
    return
def play_events():
    media= mediaOptionVal_events.get()
    if media[-3:] == "mp4":
        objPlayer.play_events()
        frame_events.pack()
    elif media[-3:] == "jpg":
        show_events()
    return
def play_religious():
    media= mediaOptionVal_religious.get()
    if media[-3:] == "mp4":
        objPlayer.play_religious()
        frame_religious.pack()
    elif media[-3:] == "jpg":
        show_religious()
    return
def play_archive():
    media= mediaOptionVal_archive.get()
    if media[-3:] == "mp4":
        objPlayer.play_archive()
        frame_archive.pack()
    elif media[-3:] == "jpg":
        show_archive()
    return

def play_posters():
    media= mediaOptionVal_posters.get()
    if media[-3:] == "mp4":
        objPlayer.play_posters()
        frame_posters.pack()
    elif media[-3:] == "jpg":
        show_posters()
    return

#Function to go back
def back_presentation():
    frame_presentation.pack_forget()
    mainFrame.pack()
def back_info():
    frame_info.pack_forget()
    mainFrame.pack()
def back_fitness():
    frame_fitness.pack_forget()
    mainFrame.pack()

def back_events():
    frame_events.pack_forget()
    mainFrame.pack()
        
def back_religious():
    frame_religious.pack_forget()
    mainFrame.pack()
def back_dining():
    frame_dining.pack_forget()
    mainFrame.pack()
    
def back_archive():
    frame_archive.pack_forget()
    mainFrame.pack()

def back_posters():
    frame_posters.pack_forget()
    mainFrame.pack()

#GUI
welcome_mainFrame = Label(mainFrame, text = "Welcome!", font = ("Arial", 25))
welcome_mainFrame.grid(row = 1, column = 1, padx = 100, pady = (300, 10))

presentationBtn = ttk.Button(mainFrame, text = "Presentation", command = lambda: mainFrameFtn("presentation"))
presentationBtn.grid(row = 2, column = 1, padx = 100, pady = (10, 10))

infoNewStudentsBtn = ttk.Button(mainFrame, text = "Info for New Students/Course Ads", command = lambda: mainFrameFtn("info"))
infoNewStudentsBtn.grid(row = 3, column = 1, padx = 100, pady = (10, 10))

fitnessBtn = ttk.Button(mainFrame, text = "Fitness/Fitness Menu", command = lambda: mainFrameFtn("fitness"))
fitnessBtn.grid(row = 4, column = 1, padx = 100, pady = (10, 10))

eventsBtn = ttk.Button(mainFrame, text = "Events Around Campus", command = lambda: mainFrameFtn("events"))
eventsBtn.grid(row = 5, column = 1, padx = 100, pady = (10, 10))

religiousBtn = ttk.Button(mainFrame, text = "Religious/Volunteering Work Around Campus", command = lambda: mainFrameFtn("religious"))
religiousBtn.grid(row = 6, column = 1, padx = 100, pady = (10, 10))

diningBtn = ttk.Button(mainFrame, text = "Dining Menu", command = lambda: mainFrameFtn("dining"))
diningBtn.grid(row = 7, column = 1, padx = 100, pady = (10, 10))

archiveBtn = ttk.Button(mainFrame, text = "Archive", command = lambda: mainFrameFtn("archive"))
archiveBtn.grid(row = 8, column = 1, padx = 100, pady = (10, 10))

postersBtn = ttk.Button(mainFrame, text = "Posters Under the Dome", command = lambda: mainFrameFtn("posters"))
postersBtn.grid(row = 9, column = 1, padx = 100, pady = (10, 10))

#Presentation GUI
PLAY_vid_menu_presentation = ttk.Button(frame_presentation, text = "Play/Show", command = play_presentation)
PLAY_vid_menu_presentation.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_presentation = OptionMenu(frame_presentation, mediaOptionVal_presentation, *media_presentation)
MENU_vid_presentation.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_presentation = Label(frame_presentation, text = "Make Selection: ", font = ("Arial", 15))
LABEL_vid_presentation.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_presentation = ttk.Button(frame_presentation, text = "Back", command = back_presentation)
Back_vid_presentation.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))


#Info GUI

PLAY_vid_menu_info = ttk.Button(frame_info, text = "Play/Show", command = play_info)
PLAY_vid_menu_info.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_info = OptionMenu(frame_info, mediaOptionVal_info, *media_info)
MENU_vid_info.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_info = Label(frame_info, text = "Make Selection: ", font = ("Arial", 15))
LABEL_vid_info.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))


Back_vid_info = ttk.Button(frame_info, text = "Back", command = back_info)
Back_vid_info.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#fitness GUI

PLAY_vid_menu_fitness = ttk.Button(frame_fitness, text = "Play/Show", command = play_fitness)
PLAY_vid_menu_fitness.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_fitness = OptionMenu(frame_fitness, mediaOptionVal_fitness, *media_fitness)
MENU_vid_fitness.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_fitness = Label(frame_fitness, text = "Make Selection: ", font = ("Arial", 15))
LABEL_vid_fitness.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_fitness = ttk.Button(frame_fitness, text = "Back", command = back_fitness)
Back_vid_fitness.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))


#events GUI

PLAY_vid_menu_events = ttk.Button(frame_events, text = "Play/Show", command = play_events)
PLAY_vid_menu_events.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_events = OptionMenu(frame_events, mediaOptionVal_events, *media_events)
MENU_vid_events.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_events = Label(frame_events, text = "Make Selection: ", font = ("Arial", 15))
LABEL_vid_events.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_events = ttk.Button(frame_events, text = "Back", command = back_events)
Back_vid_events.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#religious GUI

PLAY_vid_menu_religious = ttk.Button(frame_religious, text = "Play/Show", command = play_religious)
PLAY_vid_menu_religious.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_religious = OptionMenu(frame_religious, mediaOptionVal_religious, *media_religious)
MENU_vid_religious.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_religious = Label(frame_religious, text = "Make Selection: ", font = ("Arial", 15))
LABEL_vid_religious.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_religious = ttk.Button(frame_religious, text = "Back", command = back_religious)
Back_vid_religious.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#dining GUI
PLAY_menu_img_dining = ttk.Button(frame_dining, text = "Show", command =show_dining)
PLAY_menu_img_dining.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img_dining = OptionMenu(frame_dining, mediaOptionVal_dining, *media_dining)
MENU_img_dining.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img_dining = Label(frame_dining, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img_dining.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img_dining = ttk.Button(frame_dining, text = "Back", command = back_dining)
BACK_img_dining.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#archive GUI

PLAY_vid_menu_archive = ttk.Button(frame_archive, text = "Play/Show", command = play_archive)
PLAY_vid_menu_archive.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_archive = OptionMenu(frame_archive, mediaOptionVal_archive, *media_archive)
MENU_vid_archive.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_archive = Label(frame_archive, text = "Make Selection: ", font = ("Arial", 15))
LABEL_vid_archive.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_archive = ttk.Button(frame_archive, text = "Back", command = back_archive)
Back_vid_archive.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#Posters Under the Dome GUI
PLAY_vid_menu_posters = ttk.Button(frame_posters, text = "Play/Show", command = play_posters)
PLAY_vid_menu_posters.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_posters = OptionMenu(frame_posters, mediaOptionVal_posters, *media_posters)
MENU_vid_posters.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_posters = Label(frame_posters, text = "Make Selection: ", font = ("Arial", 15))
LABEL_vid_posters.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_posters = ttk.Button(frame_posters, text = "Back", command = back_posters)
Back_vid_posters.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
guiWindow.mainloop()