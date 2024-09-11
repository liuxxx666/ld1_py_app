import time
import periphery

DO1=47
DO2=48
DO3=49
DO4=50

gpio = periphery.GPIO(DO1, "out")

while True:
    gpio.write(True)
    level = gpio.read()
    print('high level:%d'%level)
    time.sleep(1)
    gpio.write(False)
    level = gpio.read()
    print('low level:%d'%level)
    time.sleep(1)