import keyboard
import glob2
import subprocess
from tkinter import *
from tkinter.ttk import *
from gpiozero import Button
#Making GUI guiWindow
guiWindow = Tk()
#Making three Frames
#.pack() show the myFrame, .pack_forget() hides the myFrame.
myFrame= Frame(guiWindow)
myFrame.pack()
frame_video = Frame(guiWindow)
frame_video.pack_forget()
frame_images = Frame(guiWindow)
frame_images.pack_forget()

#Setting the guiWindow geometry
guiWindow.geometry("1280x720")

#Lists to store videos and images names
videosList = []
imagesList = []

#Function to load videos from the storage and store their names in the list
#Place your videos in /home/pi/Videos

def getStorageVideos():
    myVideos = []
    #You can change the location of videos to any other here
    for file in glob2.glob("/home/pi/Videos/*.mp4"):
        myVideos.append(file)
    for items in myVideos:
        x = re.split("\/", items, 4)
        videosList.append(x[4])
    videosList.append(videosList[0])
    print(videosList)
    
#Function to load images from the storage and store their names in the list
#Place your images in /home/pi/Pictures
def getStrorageImages():
    myImages = []
    
    #You can change the location of images to any other here
    for file in glob2.glob("/home/pi/Pictures/*.jpg"):
        myImages.append(file)
    for items in myImages:
        x = re.split("\/", items, 4)
        imagesList.append(x[4])
        imagesList.append(imagesList[0])
    print(imagesList)

#Load videos and images
getStorageVideos()
getStrorageImages()

#Variables to store the option from option menu
ValueRAD = IntVar()
VideoOptionVal = StringVar(guiWindow)
VideoOptionVal.set(videosList[0])
ImageOptionVal = StringVar(guiWindow)
ImageOptionVal.set(imagesList[0])

#Buttons, the arguments to the button function shows to which GPIO pin the button is connected
Btn_tab = Button(2)
Btn_arrowUP = Button(3)
Btn_pause = Button(4)
Btn_space = Button(17)
Btn_arrowDOWN = Button(27)
Btn_Q_Stop = Button(22)

def enableButton():
    PLAY_vid_menu["state"] = NORMAL


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
    def play_video(self):
        toPlay = VideoOptionVal.get()
        print(toPlay)
        name_vid = "/home/pi/Videos/"+toPlay
        MyPlayer.omx = subprocess.Popen(['omxplayer',(name_vid)], stdin =subprocess.PIPE, stdout= None, stderr=None, bufsize=0)
        PLAY_vid_menu["state"] = DISABLED
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
#Function to get the Radio Buttons Values
def ValBTN(ValueRAD):
    if ValueRAD == 1:
        myFrame.pack_forget()
        frame_images.pack()
    elif ValueRAD == 2:
        myFrame.pack_forget()
        frame_video.pack()
    else:
        print(ValueRAD.get())

#These are the functions for GUI Buttons
#Calls the Play function to play the videos
def play():
    objPlayer.play_video()
    frame_video.pack()
    myFrame.pack_forget()
    return

#Show images
def show():
    to_show = ImageOptionVal.get()
    print(to_show)
    name_img = "/home/pi/Pictures/"+to_show
    subprocess.call("feh -F "+name_img+" &", shell=True)
    myFrame.pack_forget()
    frame_images.pack()

#Function to go back 
def back(val):
    if val == 'i':
        frame_images.pack_forget()
        myFrame.pack()
    elif val == 'v':
        frame_video.pack_forget()
        myFrame.pack()
        
        
#GUI
vid_img_opt = Label(myFrame, text = "What do you want to play?", font=("Arial", 25))
vid_img_opt.grid(row = 0, column = 0, padx = 50, pady = (400,10))

BTNImg = ttk.Button(myFrame, text = "Images", command = lambda: ValBTN(1))
BTNImg.grid(row = 1, column = 0, padx = 100, pady = 10)

BTNVid = ttk.Button(myFrame, text = "Videos", command = lambda: ValBTN(2))
BTNVid.grid(row = 2, column = 0, padx = 100, pady = 10)

PLAY_vid_menu = ttk.Button(frame_video, text = "Play", command = play)
PLAY_vid_menu.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid = OptionMenu(frame_video, VideoOptionVal, *videosList)
MENU_vid.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid = Label(frame_video, text = "Choose Video: ", font = ("Arial", 15))
LABEL_vid.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))



Back_vid = ttk.Button(frame_video, text = "Back", command = lambda: back('v'))
Back_vid.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
PLAY_menu_img = ttk.Button(frame_images, text = "Show", command = show)
PLAY_menu_img.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img = OptionMenu(frame_images, ImageOptionVal, *imagesList)
MENU_img.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img = Label(frame_images, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img = ttk.Button(frame_images, text = "Back", command = lambda: back('i'))
BACK_img.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
guiWindow.mainloop()