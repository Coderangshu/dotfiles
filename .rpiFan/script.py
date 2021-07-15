import os
import time
try:
    import RPi.GPIO as gp
except ModuleNotFoundError:
    os.system("sudo env CFLAGS=\"-fcommon\" pip install rpi.gpio")
    import RPi.GPIO as gp
try:
    from gpiozero import CPUTemperature as cput
except ModuleNotFoundError:
    os.system("sudo pacman -S python-gpiozero")
    try:
        from gpiozero import CPUTemperature as cput
    except ModuleNotFoundError:
        os.system("sudo pip install colorzero")
        from gpiozero import CPUTemperature as cput

ct = cput()
pin = 14
gp.setmode(gp.BCM)
gp.setup(pin,gp.OUT)
while(1!=0):
    temp = ct.temperature
    if temp>60:
        gp.output(pin,gp.HIGH)
    elif temp<55:
        gp.output(pin,gp.LOW)
    time.sleep(1)
