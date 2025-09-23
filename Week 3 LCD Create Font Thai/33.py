import I2C_LCD_driver
import RPi.GPIO as GPIO
from time import sleep

mylcd = I2C_LCD_driver.lcd()
button = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

font = [
   [0x00,0x08,0x08,0x08,0x08,0x0E,0x09,0x06], # Char 0
   [0x01,0x09,0x19,0x09,0x09,0x09,0x09,0x0F], # Char 1
   [0x00,0x0C,0x12,0x02,0x02,0x02,0x02,0x02], # Char 2
   [0x1F,0x10,0x10,0x1F,0x01,0x11,0x11,0x1F], # Char 3
   [0x1A,0x1A,0x0A,0x0A,0x0A,0x0A,0x0F,0x0B], # Char 4
   [0x18,0x1B,0x0D,0x09,0x09,0x09,0x09,0x09], # Char 5
   [0x1F,0x10,0x1F,0x01,0x01,0x07,0x05,0x07]  # Char 6
]

mylcd.lcd_load_custom_chars(font)
mylcd.lcd_clear()

try:
    print("Hold button to reverse direction.")
    pos = 0
    direction = 1   
    lcd_width = 16  

    while True:
        direction = -1 if GPIO.input(button) == 0 else 1

        mylcd.lcd_clear()
        mylcd.lcd_write(0x8C - pos)
        mylcd.lcd_write_char(0)
        mylcd.lcd_write_char(1)
        mylcd.lcd_write_char(2)

        mylcd.lcd_write(0xCC - pos)
        mylcd.lcd_write_char(3)
        mylcd.lcd_write_char(4)
        mylcd.lcd_write_char(5)
        mylcd.lcd_write_char(6)

        pos += direction

        if direction == 1 and pos > lcd_width - 4:
            pos = 0
        elif direction == -1 and pos < 0:
            pos = lcd_width - 4

        sleep(0.1)

except:
    GPIO.cleanup()

