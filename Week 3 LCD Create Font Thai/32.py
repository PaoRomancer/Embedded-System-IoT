import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()
row = 1
col = 0
font = [
	   [0x00, 0x08, 0x08, 0x08, 0x08, 0x0E, 0x09, 0x06], # Char 0 - Upper-left
	   [0x01, 0x09, 0x19, 0x09, 0x09, 0x09, 0x09, 0x0F], # Char 1 - Upper-middle
	   [0x00, 0x0C, 0x12, 0x02, 0x02, 0x02, 0x02, 0x02], # Char 2 - Upper-right
	   [0x1F, 0x10, 0x10, 0x1F, 0x01, 0x11, 0x11, 0x1F], # Char 3 - Lower-left
	   [0x1A, 0x1A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0F, 0x0B], # Char 4 - Lower-middle
	   [0x18, 0x1B, 0x0D, 0x09, 0x09, 0x09, 0x09, 0x09], # Char 5 - Lower-right
	   [0x1F, 0x10, 0x1F, 0x01, 0x01, 0x07, 0x05, 0x07]
	   ]
	   
mylcd.lcd_load_custom_chars(font) # create 6 custom characters
mylcd.lcd_clear()

while True:
	for pos in range(16):
		mylcd.lcd_clear()
		mylcd.lcd_write(0x8F-pos) # Write first three chars to row 1 directly
		mylcd.lcd_write_char(0) # write character 0
		mylcd.lcd_write_char(1) # write character 0
		mylcd.lcd_write_char(2) # write character 0
		mylcd.lcd_write(0xCF-pos) # Write next three chars to row 2 directly
		mylcd.lcd_write_char(3) # write character 0
		mylcd.lcd_write_char(4) # write character 0
		mylcd.lcd_write_char(5) # write character 
		mylcd.lcd_write_char(6)
		sleep(0.2)  

mylcd.sleep(0.5)

