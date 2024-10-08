import os
import sys
import threading
import time

import periphery

# DI1=56
# DI2=57
# DI3=58
# DI4=59

# gpio = periphery.GPIO(DI1, "in")

# while True:
#     level = gpio.read()
#     print('level:%d'%level)
#     time.sleep(1)

from periphery import GPIO

DI1=24
DI2=25
DI3=26
DI4=27

gpio_in = GPIO("/dev/gpiochip3", DI1, "in")
while True:
    level = gpio_in.read()
    print('level:%d'%level)
    time.sleep(1)