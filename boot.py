# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

# Add the Libs directory to the import path
import sys
sys.path.insert(0,"Libs")

# Enable power to the display Stemma QT connector and NEO-Pixel
from feathers3 import set_ldo2_power
set_ldo2_power(True)

# Setup the piins and turn on 5V power to the servos/NEO-Pixels
import Bot
Bot.BoostOn()
