# Import file for Explorers Bot defs

__version__ = "1.1"
from machine import Pin, ADC
import time

# NEO-Pixel oin
NEOpixelPin = const(7)

# Input button pins
But0Pin = const(10)
But1Pin = const(11)
But2Pin = const(36)
BootPin = const(0)

# Servo pins
S0Pin = const(14)  # Control signal for Servo 0
S1Pin = const(18)  # Control signal for Servo 1
S2Pin = const(12)  # Control signal for Servo 2
S3Pin = const(17)  # Control signal for Servo 3
BoostEnPin = const(33)  # Enable signal for 5V power to servos/NeoPixel

# Reflectance sensor pins
LSctrlPin = const(38)
LS1Pin = const(5)
LS2Pin = const(6)
LS3Pin = const(1)
LS4Pin = const(3)

# Setup the line sensors
LS1 = ADC(Pin(LS1Pin))
LS1.atten(ADC.ATTN_11DB)
LS2 = ADC(Pin(LS2Pin))
LS2.atten(ADC.ATTN_11DB)
LS3 = ADC(Pin(LS3Pin))
LS3.atten(ADC.ATTN_11DB)
LS4 = ADC(Pin(LS4Pin))
LS4.atten(ADC.ATTN_11DB)

# Setup the switches
SelButton = Pin(But2Pin, Pin.IN, Pin.PULL_UP)
UpButton = Pin(But0Pin, Pin.IN, Pin.PULL_UP)
DwnButton = Pin(But1Pin, Pin.IN, Pin.PULL_UP)
BootButton = Pin(BootPin, Pin.IN, Pin.PULL_UP)

# Setup the boost enable
BoostEnb = Pin(BoostEnPin,Pin.OUT) # Setup pin

def BoostOn():
    BoostEnb.value(1) # Power on

def BoostOff():
    BoostEnb.value(0) # Power off

# Class to control the reflectance sensor emitters
class LSctrl:
    # Init the emitter control stuff
    def __init__(self):
        self.ctrl = Pin(LSctrlPin,Pin.OUT)  # Setup control pin
        self.ResetBrightness()  # Set to full on

    # Set emitter brightness to "level"
    # Level can be 0-31 where 0 is full on and 31 is the lowest level
    def SetBrightness(self,new_level):
        self.ResetBrightness()  # Start from the top
        if new_level < 0 or new_level > 31:  # Chek for valid brightness
            raise ValueError("Emitter brightness must be from0 to 31")
        while self.level != new_level:
            self.ctrl.value(0)  # Do a > .5us pulse low and then high > .5us
            time.sleep_us(1)
            self.ctrl.value(1)
            time.sleep_us(1)
            self.level = self.level + 1
        return (self.level)

    # Return the current brightness level
    def GetBrightness(self):
        return (self.level)

    # Go to the next level
    def NextBrightness(self):
        self.ctrl.value(0)  # Do a > .5us pulse low and then high > .5us
        time.sleep_us(1)
        self.ctrl.value(1)
        time.sleep_us(1)
        self.level = self.level + 1
        if self.level >= 32:
            self.level = 0
        return (self.level)

    # Reset emitters to default full on level
    def ResetBrightness(self):
        self.ctrl.value(1)  # Set to high and wait a bit_length
        time.sleep_ms(2)
        # Generate a >1ms low pulse to reset to max brightness
        self.ctrl.value(0)
        time.sleep_ms(2)
        self.ctrl.value(1)
        time.sleep_ms(2)
        self.level = 0  # Set current level to full on

