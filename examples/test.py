from rpilcdmenu.i2c_lcd_driver import i2c_lcd_driver
from time import *

mylcd = i2c_lcd_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)