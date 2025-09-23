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
	 [0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10], # Char 0 - Upper-left
	 [0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00], # Char 1 - Upper-middle
	 [0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01], # Char 2 - Upper-right
	 [0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00], # Char 3 - Lower-left
	 [0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00], # Char 4 - Lower-middle
	 [0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00] # Char 5 - Lower-right
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
