# LF Bot V2 NEO-Pixel Test

from machine import I2C
from feathers3 import get_battery_voltage, led_set, set_ldo2_power
import Bot
import ssd1306
import time

Bot.BoostOff()  # 5V not needed
led_set(0)  # Blue LED off
# Setup the display
disp = ssd1306.SSD1306_I2C(128,64,I2C(1))

while True:
    # Resetup the display and show the voltage
    set_ldo2_power(True)  # Power back up
    time.sleep(1)
    disp.init_display()
    disp.fill(0)
    disp.text("Zebra LF Bot V2",0,0)
    disp.text("Bat: {}V".format(get_battery_voltage()),0,18)
    disp.show()
    time.sleep(3)
    # Power down the display
    set_ldo2_power(False)
    time.sleep(10)

