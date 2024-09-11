import os

TEST_LED = 'led2'

def led_get_value(name):
    if name == 'led2' or name == 'led3' or name == 'led4'or name == 'led5':
        try:
            p = os.popen('cat /sys/devices/platform/leds/leds/%s/brightness'%name)
            val = p.read()
            p.close()
            return val
        except OSError:
            pass   

def led_set_value(name, val):
    if name == 'led2' or name == 'led3' or name == 'led4'or name == 'led5':
        try:
            os.system('echo %s > /sys/devices/platform/leds/leds/%s/brightness'%(val, name))
        except OSError:
            pass

if __name__ == '__main__':
    print(led_get_value(TEST_LED))
    led_set_value(TEST_LED, '1')
    print(led_get_value(TEST_LED))

    






