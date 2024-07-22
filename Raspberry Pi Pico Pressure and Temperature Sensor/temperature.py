import machine
import utime
import RPi.GPIO as GPIO

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
threshold = 20
led_blue = 27           #GPIO 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_blue, GPIO.OUT)
GPIO.output(led_blue, GPIO.LOW)
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print("Temperature: {}".format(temperature))
    if temperature > threshold -1 && temperature < threshold + 1:
        GPIO.output(led_blue, GPIO.HIGH)
    else:
        GPIO.output(led_blue, GPIO.LOW)
    utime.sleep(2)
