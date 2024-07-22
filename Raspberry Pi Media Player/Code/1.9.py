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
mainFrame = Frame(guiWindow)
mainFrame.pack()

myFrame_info= Frame(guiWindow)
myFrame_info.pack_forget()
frame_video_info = Frame(guiWindow)
frame_video_info.pack_forget()
frame_images_info = Frame(guiWindow)
frame_images_info.pack_forget()

myFrame_fitness= Frame(guiWindow)
myFrame_fitness.pack_forget()
frame_video_fitness = Frame(guiWindow)
frame_video_fitness.pack_forget()
frame_images_fitness = Frame(guiWindow)
frame_images_fitness.pack_forget()

myFrame_events= Frame(guiWindow)
myFrame_events.pack_forget()
frame_video_events = Frame(guiWindow)
frame_video_events.pack_forget()
frame_images_events = Frame(guiWindow)
frame_images_events.pack_forget()

myFrame_religious= Frame(guiWindow)
myFrame_religious.pack_forget()
frame_video_religious = Frame(guiWindow)
frame_video_religious.pack_forget()
frame_images_religious = Frame(guiWindow)
frame_images_religious.pack_forget()


frame_images_dining = Frame(guiWindow)
frame_images_dining.pack_forget()

myFrame_archive= Frame(guiWindow)
myFrame_archive.pack_forget()
frame_video_archive = Frame(guiWindow)
frame_video_archive.pack_forget()
frame_images_archive = Frame(guiWindow)
frame_images_archive.pack_forget()

#Setting the guiWindow geometry
w, h = guiWindow.winfo_screenwidth(), guiWindow.winfo_screenheight()
guiWindow.geometry("%dx%d+0+0" % (w, h))
#Lists to store videos and images names
videosList_info = []
imagesList_info = []

videosList_fitness = []
imagesList_fitness = []

videosList_events = []
imagesList_events = []

videosList_religious = []
imagesList_religious = []

imagesList_dining = []

videosList_archive = []
imagesList_archive = []


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

def mainFrameFtn(option):
    if option == "info":
        mainFrame.pack_forget()
        myFrame.pack()
        
    elif option == "fitness":
        mainFrame.pack_forget()
        myFrame.pack()
        
    elif option == "events":
        mainFrame.pack_forget()
        myFrame.pack()
        
    elif option == "religious":
        mainFrame.pack_forget()
        myFrame.pack()
        
    elif option == "dining":
        mainFrame.pack_forget()
        myFrame.pack()
        
    elif option == "archive":
        mainFrame.pack_forget()
        myFrame.pack()
#Load videos and images
getStorageVideos()
getStrorageImages()

#Variables to store the option from option menu
ValueRAD = IntVar()
VideoOptionVal_info = StringVar(guiWindow)
VideoOptionVal_info.set(videosList_info[0])
ImageOptionVal_info = StringVar(guiWindow)
ImageOptionVal_info.set(imagesList_info[0])

VideoOptionVal_fitness = StringVar(guiWindow)
VideoOptionVal_fitness.set(videosList_fitness[0])
ImageOptionVal_fitness = StringVar(guiWindow)
ImageOptionVal_fitness.set(imagesList_fitness[0])

VideoOptionVal_events = StringVar(guiWindow)
VideoOptionVal_events.set(videosList_events[0])
ImageOptionVal_events = StringVar(guiWindow)
ImageOptionVal_events.set(imagesList_events[0])

VideoOptionVal_religious = StringVar(guiWindow)
VideoOptionVal.set(videosList_religious[0])
ImageOptionVal_religious = StringVar(guiWindow)
ImageOptionVal_religious.set(imagesList_religious[0])

ImageOptionVal_dining = StringVar(guiWindow)
ImageOptionVal_dining.set(imagesList_dining[0])

VideoOptionVal_archive = StringVar(guiWindow)
VideoOptionVal_archive.set(videosList_archive[0])
ImageOptionVal_archive = StringVar(guiWindow)
ImageOptionVal_archive.set(imagesList_archive[0])

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
welcome_mainFrame = Label(mainFrame, text = "Welcome!", font = ("Arial", 25))
welcome_mainFrame.grid(row = 1, column = 1, padx = 100, pady = (300, 10))
        
infoNewStudentsBtn = ttk.Button(mainFrame, text = "Info for New Students/Course Ads", command = lambda: mainFrameFtn("info"))
infoNewStudentsBtn.grid(row = 2, column = 1, padx = 100, pady = (10, 10))

fitnessBtn = ttk.Button(mainFrame, text = "Fitness/Fitness Menu", command = lambda: mainFrameFtn("fitness"))
fitnessBtn.grid(row = 3, column = 1, padx = 100, pady = (10, 10))

eventsBtn = ttk.Button(mainFrame, text = "Events Around Campus", command = lambda: mainFrameFtn("events"))
eventsBtn.grid(row = 4, column = 1, padx = 100, pady = (10, 10))

religiousBtn = ttk.Button(mainFrame, text = "Religious/Volunteering Work Around Campus", command = lambda: mainFrameFtn("religious"))
religiousBtn.grid(row = 5, column = 1, padx = 100, pady = (10, 10))

diningBtn = ttk.Button(mainFrame, text = "Dining Menu", command = lambda: mainFrameFtn("dining"))
diningBtn.grid(row = 6, column = 1, padx = 100, pady = (10, 10))

archiveBtn = ttk.Button(mainFrame, text = "Archive", command = lambda: mainFrameFtn("archivev"))
archiveBtn.grid(row = 7, column = 1, padx = 100, pady = (10, 10))

#Info GUI
vid_img_opt_info = Label(myFrame_info, text = "What do you want to play?", font=("Arial", 25))
vid_img_opt_info.grid(row = 0, column = 0, padx = 50, pady = (400,10))

BTNImg_info = ttk.Button(myFrame_info, text = "Images", command = lambda: ValBTN(1))
BTNImg_info.grid(row = 1, column = 0, padx = 100, pady = 10)

BTNVid_info = ttk.Button(myFrame_info, text = "Videos", command = lambda: ValBTN(2))
BTNVid_info.grid(row = 2, column = 0, padx = 100, pady = 10)

PLAY_vid_menu_info = ttk.Button(frame_video_info, text = "Play", command = play)
PLAY_vid_menu_info.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_info = OptionMenu(frame_video_info, VideoOptionVal_info, *videosList_info)
MENU_vid_info.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_info = Label(frame_video_info, text = "Choose Video: ", font = ("Arial", 15))
LABEL_vid_info.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))


Back_vid_info = ttk.Button(frame_video_info, text = "Back", command = lambda: back("v_info"))
Back_vid_info.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
PLAY_menu_img_info = ttk.Button(frame_images_info, text = "Show", command = show_info)
PLAY_menu_img_info.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img_info = OptionMenu(frame_images_info, ImageOptionVal_info, *imagesList_info)
MENU_img_info.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img_info = Label(frame_images_info, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img_info.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img_info = ttk.Button(frame_images_info, text = "Back", command = lambda: back("i_info"))
BACK_img_info.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#fitness GUI
vid_img_opt_fitness = Label(myFrame_fitness, text = "What do you want to play?", font=("Arial", 25))
vid_img_opt_fitness.grid(row = 0, column = 0, padx = 50, pady = (400,10))

BTNImg_fitness = ttk.Button(myFrame_fitness, text = "Images", command = lambda: ValBTN(1))
BTNImg_fitness.grid(row = 1, column = 0, padx = 100, pady = 10)

BTNVid_fitness = ttk.Button(myFrame_fitness, text = "Videos", command = lambda: ValBTN(2))
BTNVid_fitness.grid(row = 2, column = 0, padx = 100, pady = 10)

PLAY_vid_menu_fitness = ttk.Button(frame_video_fitness, text = "Play", command = play)
PLAY_vid_menu_fitness.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_fitness = OptionMenu(frame_video_fitness, VideoOptionVal_fitness, *videosList_fitness)
MENU_vid_fitness.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_fitness = Label(frame_video_fitness, text = "Choose Video: ", font = ("Arial", 15))
LABEL_vid_fitness.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_fitness = ttk.Button(frame_video_fitness, text = "Back", command = lambda: back("v_fitness"))
Back_vid_fitness.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
PLAY_menu_img_fitness = ttk.Button(frame_images_fitness, text = "Show", command = show_fitness)
PLAY_menu_img_fitness.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img_fitness = OptionMenu(frame_images_fitness, ImageOptionVal_fitness, *imagesList_fitness)
MENU_img_fitness.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img_fitness = Label(frame_images_fitness, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img_fitness.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img_fitness = ttk.Button(frame_images_fitness, text = "Back", command = lambda: back("i_fitness"))
BACK_img_fitness.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#events GUI
vid_img_opt_events = Label(myFrame_events, text = "What do you want to play?", font=("Arial", 25))
vid_img_opt_events.grid(row = 0, column = 0, padx = 50, pady = (400,10))

BTNImg_events = ttk.Button(myFrame_events, text = "Images", command = lambda: ValBTN(1))
BTNImg_events.grid(row = 1, column = 0, padx = 100, pady = 10)

BTNVid_events = ttk.Button(myFrame_events, text = "Videos", command = lambda: ValBTN(2))
BTNVid_events.grid(row = 2, column = 0, padx = 100, pady = 10)

PLAY_vid_menu_events = ttk.Button(frame_video_events, text = "Play", command = play)
PLAY_vid_menu_events.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_events = OptionMenu(frame_video_events, VideoOptionVal_events, *videosList_events)
MENU_vid_events.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_events = Label(frame_video_events, text = "Choose Video: ", font = ("Arial", 15))
LABEL_vid_events.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_events = ttk.Button(frame_video_events, text = "Back", command = lambda: back("v_events"))
Back_vid_events.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
PLAY_menu_img_events = ttk.Button(frame_images_events, text = "Show", command = show_events)
PLAY_menu_img_events.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img_events = OptionMenu(frame_images_events, ImageOptionVal_events, *imagesList_events)
MENU_img_events.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img_events = Label(frame_images_events, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img_events.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img_events = ttk.Button(frame_images_events, text = "Back", command = lambda: back("i_events"))
BACK_img_events.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#religious GUI
vid_img_opt_religious = Label(myFrame_religious, text = "What do you want to play?", font=("Arial", 25))
vid_img_opt_religious.grid(row = 0, column = 0, padx = 50, pady = (400,10))

BTNImg_religious = ttk.Button(myFrame_religious, text = "Images", command = lambda: ValBTN(1))
BTNImg_religious.grid(row = 1, column = 0, padx = 100, pady = 10)

BTNVid_religious = ttk.Button(myFrame_religious, text = "Videos", command = lambda: ValBTN(2))
BTNVid_religious.grid(row = 2, column = 0, padx = 100, pady = 10)

PLAY_vid_menu_religious = ttk.Button(frame_video_religious, text = "Play", command = play)
PLAY_vid_menu_religious.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_religious = OptionMenu(frame_video_religious, VideoOptionVal_religious, *videosList_religious)
MENU_vid_religious.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_religious = Label(frame_video_religious, text = "Choose Video: ", font = ("Arial", 15))
LABEL_vid_religious.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_religious = ttk.Button(frame_video_religious, text = "Back", command = lambda: back("v_religious"))
Back_vid_religious.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
PLAY_menu_img_religious = ttk.Button(frame_images_religious, text = "Show", command = show_religious)
PLAY_menu_img_religious.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img_religious = OptionMenu(frame_images_religious, ImageOptionVal_religious, *imagesList_religious)
MENU_img_religious.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img_religious = Label(frame_images_religious, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img_religious.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img_religious = ttk.Button(frame_images_religious, text = "Back", command = lambda: back("i_religious"))
BACK_img_religious.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#dining GUI
PLAY_menu_img_dining = ttk.Button(frame_images_dining, text = "Show", command = show_dining)
PLAY_menu_img_dining.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img_dining = OptionMenu(frame_images_dining, ImageOptionVal_dining, *imagesList_dining)
MENU_img_dining.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img_dining = Label(frame_images_dining, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img_dining.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img_dining = ttk.Button(frame_images_dining, text = "Back", command = lambda: back("i_dining"))
BACK_img_dining.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

#archive GUI
vid_img_opt_archive = Label(myFrame_archive, text = "What do you want to play?", font=("Arial", 25))
vid_img_opt_archive.grid(row = 0, column = 0, padx = 50, pady = (400,10))

BTNImg_archive = ttk.Button(myFrame_archive, text = "Images", command = lambda: ValBTN(1))
BTNImg_archive.grid(row = 1, column = 0, padx = 100, pady = 10)

BTNVid_archive = ttk.Button(myFrame_archive, text = "Videos", command = lambda: ValBTN(2))
BTNVid_archive.grid(row = 2, column = 0, padx = 100, pady = 10)

PLAY_vid_menu_archive = ttk.Button(frame_video_archive, text = "Play", command = play)
PLAY_vid_menu_archive.grid(row = 2, column = 2, padx = 10, pady = (100, 10))

MENU_vid_archive = OptionMenu(frame_video_archive, VideoOptionVal_archive, *videosList_archive)
MENU_vid_archive.grid(row = 1, column = 3, padx = 10, pady = (10,10))

LABEL_vid_archive = Label(frame_video_archive, text = "Choose Video: ", font = ("Arial", 15))
LABEL_vid_archive.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

Back_vid_archive = ttk.Button(frame_video_archive, text = "Back", command = lambda: back("v_archive"))
Back_vid_archive.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))
PLAY_menu_img_archive = ttk.Button(frame_images_archive, text = "Show", command = show_archive)
PLAY_menu_img_archive.grid(row = 2, column = 2, padx = 10, pady = (100, 10))
MENU_img_archive = OptionMenu(frame_images_archive, ImageOptionVal_archive, *imagesList_archive)
MENU_img_archive.grid(row = 1, column = 3, padx = 10, pady = (10,10))
LABEL_img_archive = Label(frame_images_archive, text = "Choose Image: ", font = ("Arial", 15))
LABEL_img_archive.grid(row = 1, column = 1, padx = (100, 20), pady = (10,10))

BACK_img_archive = ttk.Button(frame_images_archive, text = "Back", command = lambda: back("i_archive"))
BACK_img_archive.grid(row = 0, column = 0, padx = 10, pady = (300 ,10))

guiWindow.mainloop()