# Explorer LFbot V2
# Built in ADC inputs Test

from machine import I2C
import ssd1306
import time
from feathers3 import get_battery_voltage, get_amb_light, get_vbus_present
import Bot

Bot.BoostOff()  # 5V not needed

disp = ssd1306.SSD1306_I2C(128,64,I2C(1))

while True:
    disp.fill(0)
    disp.text("Zebra LF Bot V2",0,0)
    disp.text("Bat: {}V".format(get_battery_voltage()),0,20)    
    disp.text("Light: {}".format(get_amb_light()),0,32)    
    disp.text("VBUS: {}".format(get_vbus_present()),0,44)
    disp.show()
    time.sleep(1)

