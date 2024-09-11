import os
import sys
import threading
import time

import periphery

DI1=56
DI2=57
DI3=58
DI4=59

gpio = periphery.GPIO(DI1, "in")

while True:
    level = gpio.read()
    print('level:%d'%level)
    time.sleep(1)