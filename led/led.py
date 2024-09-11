import time
import periphery

TEST_LED='led2'
led = periphery.LED(TEST_LED, 0)
print('led_max_brightness:%d'%led.max_brightness)

while True:
    led.write(True)
    level = led.read()
    print('high level:%d'%level)
    time.sleep(1)

    led.write(False)
    level = led.read()
    print('low level:%d'%level)
    time.sleep(1)