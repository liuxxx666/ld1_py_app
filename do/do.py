import time
import periphery
from periphery import GPIO

# DO1=47
# DO2=48
# DO3=49
# DO4=50

# gpio = periphery.GPIO(DO1, "out")

# while True:
#     gpio.write(True)
#     level = gpio.read()
#     print('high level:%d'%level)
#     time.sleep(1)
#     gpio.write(False)
#     level = gpio.read()
#     print('low level:%d'%level)
#     time.sleep(1)

from periphery import GPIO

DO1=15
DO2=16
DO3=17
DO4=18

gpio_out = GPIO("/dev/gpiochip3", DO1, "out")
for i in range(10):
    gpio_out.write(True)
    level = gpio_out.read()
    print('high level:%d'%level)
    time.sleep(1)
    gpio_out.write(False)
    level = gpio_out.read()
    print('low level:%d'%level)
    time.sleep(1)
gpio_out.close()