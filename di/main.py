import os

TEST_DI = 'DI1'

def di_init(name):
    if name == 'DI1':
        try:
            os.system('echo 56 > /sys/class/gpio/export')
            os.system('echo in > /sys/class/gpio/gpio56/direction')
        except OSError:
            pass
    if name == 'DI2':
        try:
            os.system('echo 57 > /sys/class/gpio/export')
            os.system('echo in > /sys/class/gpio/gpio57/direction')
        except OSError:
            pass
    if name == 'DI3':
        try:
            os.system('echo 58 > /sys/class/gpio/export')
            os.system('echo in > /sys/class/gpio/gpio58/direction')
        except OSError:
            pass
    if name == 'DI4':
        try:
            os.system('echo 59 > /sys/class/gpio/export')
            os.system('echo in > /sys/class/gpio/gpio59/direction')
        except OSError:
            pass
        
def di_value_get(name):
    if name == 'DI1':
        try:
            value = os.popen('cat /sys/class/gpio/gpio56/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf
    if name == 'DI2':
        try:
            value = os.popen('cat /sys/class/gpio/gpio57/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf
    if name == 'DI3':
        try:
            value = os.popen('cat /sys/class/gpio/gpio58/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf
    if name == 'DI4':
        try:
            value = os.popen('cat /sys/class/gpio/gpio59/value')
        except OSError:
            value.close()
            raise SystemExit(0)
        buf = value.read()
        value.close()
        return buf

def di_deinit(name):
    if name == 'DI1':
        try:
            os.system('echo 56 > /sys/class/gpio/unexport')
        except OSError:
            pass
    if name == 'DI2':
        try:
            os.system('echo 57 > /sys/class/gpio/unexport')
        except OSError:
            pass
    if name == 'DI3':
        try:
            os.system('echo 58 > /sys/class/gpio/unexport')
        except OSError:
            pass
    if name == 'DI4':
        try:
            os.system('echo 59 > /sys/class/gpio/unexport')
        except OSError:
            pass

if __name__ == '__main__':
    di_init(TEST_DI)
    print(di_value_get(TEST_DI))
    di_deinit(TEST_DI)

    
