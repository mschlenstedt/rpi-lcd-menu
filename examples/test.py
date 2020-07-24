import i2c_lcd
from time import *

mylcd = i2c_lcd.lcd()

mylcd.lcd_display_string("Hello World!", 1)