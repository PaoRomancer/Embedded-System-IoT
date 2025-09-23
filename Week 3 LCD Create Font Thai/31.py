import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("LCD I2C", 1)
sleep(1)
mylcd.lcd_display_string(" ASCII CODE TEST", 2)
sleep(2)
mylcd.lcd_clear()
row = 1
col = 0
font = [
    [0x0E, 0x1B, 0x1F, 0x15, 0x1F, 0x0E, 0x0A, 0x00], # Char 0 - ??????+???
    [0x1C, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1C, 0x00], # Char 1 - ???+?????
    [0x00, 0x04, 0x0A, 0x11, 0x11, 0x0A, 0x04, 0x00], # Char 2 - ??????? (????)
    [0x04, 0x0E, 0x15, 0x11, 0x15, 0x0E, 0x04, 0x00], # Char 3 - ???+????
    [0x00, 0x04, 0x0A, 0x11, 0x11, 0x0A, 0x04, 0x00], # Char 4 - ??????? (????)
    [0x00, 0x04, 0x0E, 0x1F, 0x1F, 0x0E, 0x04, 0x00], # Char 5 - ???/??
    ]

mylcd.lcd_load_custom_chars(font) # create 6 custom characters
mylcd.lcd_clear()
sleep(0.5)

while True:
	for pos in range(15):  
		mylcd.lcd_write(0x80) # Write first three chars to row 1 directly
		mylcd.lcd_write_char(0) # write character 0
		mylcd.lcd_write_char(1) # write character 0
		mylcd.lcd_write_char(2) # write character 0
		mylcd.lcd_write(0xC0) # Write next three chars to row 2 directly
		mylcd.lcd_write_char(3) # write character 0
		mylcd.lcd_write_char(4) # write character 0
		mylcd.lcd_write_char(5) # write character 
		sleep(0.2)
