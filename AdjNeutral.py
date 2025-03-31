# Explorer LFbot V2
# Calibrate the servo Neutrals

from machine import I2C
import ssd1306
import time
from Bot import S0Pin, S1Pin, S2Pin, S3Pin, BoostOn
from Bot import NEOpixelPin, SelButton, UpButton, DwnButton
from CRservo import CRservo
import Neutrals

BoostOn()  # 5V needed for servos

# Setup display
disp = ssd1306.SSD1306_I2C(128,64,I2C(1))

# Get initial values
Net = [Neutrals.S0,Neutrals.S1,Neutrals.S2,Neutrals.S3]

# Setup servos
Motor0 = CRservo(S0Pin,False)
Motor1 = CRservo(S1Pin,False)
Motor2 = CRservo(S2Pin,False)
Motor3 = CRservo(S3Pin,False)

# Startup servos
Motor0.SetNeutral(Net[0])
Motor0.Off()
Motor1.SetNeutral(Net[1])
Motor1.Off()
Motor2.SetNeutral(Net[2])
Motor2.Off()
Motor3.SetNeutral(Net[3])
Motor3.Off()

Current = 0  # Set current value to be adjusted
Motor0.On()

while True:
    disp.fill(0)
    disp.text("Netural Calibrate",0,0)
    disp.text(">",0,20+12*Current)
    disp.text("S0",8,20);
    disp.text(str(int(Net[0]/1000)),32,20)
    disp.text("S1",8,32);
    disp.text(str(int(Net[1]/1000)),32,32)
    disp.text("S2",8,44);
    disp.text(str(int(Net[2]/1000)),32,44)
    disp.text("S3",8,56);
    disp.text(str(int(Net[3]/1000)),32,56)
    disp.show()

    # Check for buttons
    if not SelButton.value():  # Hit select, next value or save
        cnt = 0
        while not SelButton.value():  # Wait for release
            cnt = cnt + 1
            time.sleep(.05)
            if cnt > 40:
                break
        if cnt > 40:  # Held for at least 2 seconds
            # Save current values
            f = open('Libs/Neutrals.py', 'w')  # Open Neutrals file
            # Write out file data
            f.write('# Netural settings for servos\n')
            for cnt in range(0,4):
                f.write('S')
                f.write(str(cnt))
                f.write(' = ')
                f.write(str(Net[cnt]))
                f.write('\n')
            f.close()
            disp.fill(0)
            disp.text("Settings Saved!",0,0)
            disp.show()
            time.sleep(4)
        else:  # Not long press, just go to next one
            Motor0.Off()  # All off
            Motor1.Off()
            Motor2.Off()
            Motor3.Off()
            Current = Current + 1
            if Current > 3:
                Current = 0
            if Current == 0:  # Turn on current motor
                Motor0.On()
            elif Current == 1:
                Motor1.On()
            elif Current == 2:
                Motor2.On()
            else:
                Motor3.On()
            time.sleep(.2)

    if not UpButton.value():  # Hit Up, increase value
        Net[Current] = Net[Current] + 1000

    if not DwnButton.value():  # Hit down, decrease value
        Net[Current] = Net[Current] - 1000

    # Set servos to new values
    Motor0.SetNeutral(Net[0])
    Motor1.SetNeutral(Net[1])
    Motor2.SetNeutral(Net[2])
    Motor3.SetNeutral(Net[3])

    time.sleep(.15)

