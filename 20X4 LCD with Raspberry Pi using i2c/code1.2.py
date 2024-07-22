
import smbus
import time

# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address, Check the address on terminal by 
LCD_WIDTH = 20   # Set to your LCD Width i.e 20

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

#Defining LCD Lines
#You can control columns by using these addresses
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1


#Initializing the LCD
def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

#To turn ON the LCD
def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)


#Function to Print a string on the LCD
def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def lcd_scroll(message, line):
    str_pad = " " * 20
    my_long_string = message
    my_long_string = str_pad + my_long_string
    for i in range (0, len(my_long_string)):
            lcd_text = my_long_string[i:(i+20)]
            lcd_string(lcd_text,line)
            time.sleep(0.4)
            lcd_string(str_pad,line)
            
#Main Function
def main():
  # Main program block

  # Initialise display
  lcd_init()
  #To print a temperature value.
  #This can be a temperature value from a sensor 
  myTemp = 25
  #First I have converted the integer to string by str() function and then I concatenated it with a string "Temperature: "
  myString = "Temperature: " + str(myTemp)    #str() converts integer to string
  while True:
    # Change the text
    lcd_scroll(myString,LCD_LINE_1)
    lcd_scroll("Brando", LCD_LINE_2)
    lcd_scroll("Brando", LCD_LINE_3)
    lcd_scroll("Brando", LCD_LINE_4)
    time.sleep(3)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)

