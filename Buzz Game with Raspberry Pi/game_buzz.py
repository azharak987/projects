import RPi.GPIO as GPIO
from time import sleep
import vlc
GPIO.setwarnings(False)
sensor_1 = 22
sensor_2 = 23
sensor_3 = 24
sensor_4 = 25
sensorEND_1 = 2
sensorEND_2 = 3
sensorEND_3 = 4
sensorEND_4 = 5
alarm = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensor_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensor_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensor_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensorEND_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensorEND_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensorEND_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensorEND_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(alarm, GPIO.OUT)
GPIO.output(alarm, False)
p = vlc.MediaPlayer("/home/pi/Desktop/music.mp3")
class Player:
    relays = []
    lives = 0
    def __init__(self, relay_1, relay_2, relay_3, relay_4):
        self.relays = [relay_1, relay_2, relay_3, relay_4]
        self.lives = 4
        GPIO.setup(self.relays[0], GPIO.OUT)
        GPIO.setup(self.relays[1], GPIO.OUT)
        GPIO.setup(self.relays[2], GPIO.OUT)
        GPIO.setup(self.relays[3], GPIO.OUT)
        GPIO.output(self.relays[0], True)
        GPIO.output(self.relays[1], True)
        GPIO.output(self.relays[2], True)
        GPIO.output(self.relays[3], True)
    def dec_life(self):
        self.lives = self.lives-1
    def buzz():
        life = 4-self.lives
        GPIO.output(self.relays[life], True)
        sleep(0.1)
        GPIO.output(self.relays[life], False)
        sleep(0.1)
        GPIO.output(self.relays[life], True)
        sleep(0.1)
        GPIO.output(self.relays[life], False)
        sleep(0.1)
        GPIO.output(self.relays[life], True)
        sleep(0.1)
        GPIO.output(self.relays[life], False)
    def win(self):
        GPIO.output(self.relays[0], True)
        GPIO.output(self.relays[1], True)
        GPIO.output(self.relays[2], True)
        GPIO.output(self.relays[3], True)
        GPIO.output(alarm, True)
        sleep(0.1)
        GPIO.output(self.relays[0], False)
        GPIO.output(self.relays[1], False)
        GPIO.output(self.relays[2], False)
        GPIO.output(self.relays[3], False)
        GPIO.output(alarm, True)
        sleep(0.1)

        GPIO.output(self.relays[0], True)
        GPIO.output(self.relays[1], True)
        GPIO.output(self.relays[2], True)
        GPIO.output(self.relays[3], True)
        GPIO.output(alarm, True)
        sleep(0.1)
        GPIO.output(self.relays[0], False)
        GPIO.output(self.relays[1], False)
        GPIO.output(self.relays[2], False)
        GPIO.output(self.relays[3], False)
        GPIO.output(alarm, True)
        sleep(0.1)

        GPIO.output(self.relays[0], True)
        GPIO.output(self.relays[1], True)
        GPIO.output(self.relays[2], True)
        GPIO.output(self.relays[3], True)
        GPIO.output(alarm, True)
        sleep(0.1)
        GPIO.output(self.relays[0], False)
        GPIO.output(self.relays[1], False)
        GPIO.output(self.relays[2], False)
        GPIO.output(self.relays[3], False)
        GPIO.output(alarm, True)
        sleep(0.1)

        GPIO.output(self.relays[0], True)
        GPIO.output(self.relays[1], True)
        GPIO.output(self.relays[2], True)
        GPIO.output(self.relays[3], True)
        GPIO.output(alarm, True)
        sleep(0.1)
        GPIO.output(self.relays[0], False)
        GPIO.output(self.relays[1], False)
        GPIO.output(self.relays[2], False)
        GPIO.output(self.relays[3], False)
        GPIO.output(alarm, True)
        sleep(0.1)

        GPIO.output(self.relays[0], True)
        GPIO.output(self.relays[1], True)
        GPIO.output(self.relays[2], True)
        GPIO.output(self.relays[3], True)
        GPIO.output(alarm, True)
        sleep(0.1)
        GPIO.output(self.relays[0], False)
        GPIO.output(self.relays[1], False)
        GPIO.output(self.relays[2], False)
        GPIO.output(self.relays[3], False)
        GPIO.output(alarm, True)
        sleep(0.1)
#Relay Pins Passed to the Object
player_1 = Player(6, 7, 8, 9)
player_2 = Player(10, 11, 12, 13)
player_3 = Player(14, 15, 16, 17)
player_4 = Player(18, 19, 20, 21)


while(1):
    winner = None
    loser = []
    if sensor_1 == True:
        player_1.buzz()
        player_1.dec_life()

    if sensor_2 == True:
        player_2.buzz()
        player_2.dec_life()

    if sensor_3 == True:
        player_3.buzz()
        player_3.dec_life()

    if sensor_4 == True:
        player_4.buzz()
        player_4.dec_life()

    if player_2.lives == 0 and player_3.lives == 0 and player_4.lives == 0:
        winner = player_1
        break

    if player_1.lives == 0 and player_3.lives == 0 and player_4.lives == 0:
        winner = player_2
        break

    if player_1.lives == 0 and player_2.lives == 0 and player_44.lives == 0:
        winner = player_3
        break

    if player_1.lives == 0 and player_2.lives == 0 and player_3.lives == 0:
        winner = player_4
        break
winner.win()
print("END")
