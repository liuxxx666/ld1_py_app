import os

TEST_DO = 'DO1'

def do_init(name):
    if name == 'DO1':
        try:
            os.system('echo 47 > /sys/class/gpio/export')
            os.system('echo out > /sys/class/gpio/gpio47/direction')
        except OSError:
            pass
    if name == 'DO2':
        try:
            os.system('echo 48 > /sys/class/gpio/export')
            os.system('echo out > /sys/class/gpio/gpio48/direction')
        except OSError:
            pass
    if name == 'DO3':
        try:
            os.system('echo 49 > /sys/class/gpio/export')
            os.system('echo out > /sys/class/gpio/gpio49/direction')
        except OSError:
            pass
    if name == 'DO4':
        try:
            os.system('echo 50 > /sys/class/gpio/export')
            os.system('echo out > /sys/class/gpio/gpio50/direction')
        except OSError:
            pass

def do_value_set(name, val):
    if name == 'DO1':
        try:
            os.system('echo %s > /sys/class/gpio/gpio47/value'%val)
        except OSError:
            raise SystemExit(0)
    if name == 'DO2':
        try:
            os.system('echo %s > /sys/class/gpio/gpio48/value'%val)
        except OSError:
            raise SystemExit(0)
    if name == 'DO3':
        try:
            os.system('echo %s > /sys/class/gpio/gpio49/value'%val)
        except OSError:
            raise SystemExit(0)
    if name == 'DO4':
        try:
            os.system('echo %s > /sys/class/gpio/gpio50/value'%val)
        except OSError:
            raise SystemExit(0)

def do_value_get(name):
    if name == 'DO1':
        try:
            value = os.popen('cat /sys/class/gpio/gpio47/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf
    if name == 'DO2':
        try:
            value = os.popen('cat /sys/class/gpio/gpio48/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf
    if name == 'DO3':
        try:
            value = os.popen('cat /sys/class/gpio/gpio49/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf
    if name == 'DO4':
        try:
            value = os.popen('cat /sys/class/gpio/gpio50/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf

def do_deinit(name):
    if name == 'DO1':
        try:
            os.system('echo 47 > /sys/class/gpio/unexport')
        except OSError:
            pass
    if name == 'DO2':
        try:
            os.system('echo 48 > /sys/class/gpio/unexport')
        except OSError:
            pass
    if name == 'DO3':
        try:
            os.system('echo 49 > /sys/class/gpio/unexport')
        except OSError:
            pass
    if name == 'DO4':
        try:
            os.system('echo 50 > /sys/class/gpio/unexport')
        except OSError:
            pass

if __name__ == '__main__':
    do_init(TEST_DO)
    do_value_set(TEST_DO, '0')
    print(do_value_get(TEST_DO))
    do_deinit(TEST_DO)

    
