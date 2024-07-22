import RPi.GPIO as GPIO
import time
from machine import I2C
#i2c address
LPS22HB_I2C_ADDRESS   =  0x5C
#LED Connected to GPIO 17, GPIO 22 and GPIO 27
led_red = 17            #GPIO 17
led_green = 22          #GPIO 22
led_blue = 27           #GPIO 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.output(led_red, GPIO.LOW)
GPIO.output(led_green, GPIO.LOW)
thresholdPressure = 1000
LPS_ID                =  0xB1
#Register
LPS_INT_CFG           =  0x0B        #Interrupt register
LPS_THS_P_L           =  0x0C        #Pressure threshold registers
LPS_THS_P_H           =  0x0D
LPS_WHO_AM_I          =  0x0F        #Who am I
LPS_CTRL_REG1         =  0x10        #Control registers
LPS_CTRL_REG2         =  0x11
LPS_CTRL_REG3         =  0x12
LPS_FIFO_CTRL         =  0x14        #FIFO configuration register
LPS_REF_P_XL          =  0x15        #Reference pressure registers
LPS_REF_P_L           =  0x16
LPS_REF_P_H           =  0x17
LPS_RPDS_L            =  0x18        #Pressure offset registers
LPS_RPDS_H            =  0x19
LPS_RES_CONF          =  0x1A        #Resolution register
LPS_INT_SOURCE        =  0x25        #Interrupt register
LPS_FIFO_STATUS       =  0x26        #FIFO status register
LPS_STATUS            =  0x27        #Status register
LPS_PRESS_OUT_XL      =  0x28        #Pressure output registers
LPS_PRESS_OUT_L       =  0x29
LPS_PRESS_OUT_H       =  0x2A
LPS_TEMP_OUT_L        =  0x2B        #Temperature output registers
LPS_TEMP_OUT_H        =  0x2C
LPS_RES               =  0x33        #Filter reset register

class TrykkModul(object):
    def __init__(self,address=LPS22HB_I2C_ADDRESS):
        self._address = address
        self._bus = I2C(1)
        self.null_still()                         #Wait for reset to complete
        self._write_byte(LPS_CTRL_REG1 ,0x02)        #Low-pass filter disabled , output registers not updated until MSB and LSB have been read , Enable Block Data Update , Set Output Data Rate to 0
    def null_still(self):
        buf=self._read_u16(LPS_CTRL_REG2)
        buf|=0x04
        self._write_byte(LPS_CTRL_REG2,buf)               #SWRESET Set 1
        while buf:
            buf=self._read_u16(LPS_CTRL_REG2)
            buf&=0x04
    def les_data(self):
        buf=self._read_u16(LPS_CTRL_REG2)
        buf|=0x01                                         #ONE_SHOT Set 1
        self._write_byte(LPS_CTRL_REG2,buf)
    def les_byte(self,cmd):
        rec=self._bus.readfrom_mem(int(self._address),int(cmd),1)
        return rec[0]
    def _read_u16(self,cmd):
        LSB = self._bus.readfrom_mem(int(self._address),int(cmd),1)
        MSB = self._bus.readfrom_mem(int(self._address),int(cmd)+1,1)
        return (MSB[0] << 8 ) + LSB[0]
    def _write_byte(self,cmd,val):
        self._bus.writeto_mem(int(self._address),int(cmd),bytes([int(val)]))

if _name_ == '_main_':
    trykk_data = 0.0
    sensor_data=[0,0,0]
    print("\nPressure Sensor Test Program ...\n")
    min_trykk_modul=TrykkModul()

    while True:
        time.sleep(5)
        min_trykk_modul.les_data()

        if (min_trykk_modul.les_byte(LPS_STATUS)&0x01)==0x01:  # a new pressure data is generated
            sensor_data[0]=min_trykk_modul.les_byte(LPS_PRESS_OUT_XL)
            sensor_data[1]=min_trykk_modul.les_byte(LPS_PRESS_OUT_L)
            sensor_data[2]=min_trykk_modul.les_byte(LPS_PRESS_OUT_H)
            trykk_data=((sensor_data[2]<<16)+(sensor_data[1]<<8)+sensor_data[0])/4096.0
        if trykk < thresholdPressure:
            GPIO.output(led_red, GPIO.HIGH)
        elif trykk > thresholdPressure:
            GPIO.output(led_green, GPIO.HIGH)
        else:
            GPIO.output(led_red, GPIO.LOW)
        print("trykk =", round (trykk_data,2))
