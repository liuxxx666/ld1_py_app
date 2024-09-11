import os

TEST_AI = 'AI1'

def ai_get_value(name):
    if name == 'AI1':
        try:
            raw_val = os.popen('cat /sys/devices/platform/soc/19251000.gpai/iio:device0/in_voltage2_raw')
            raw = int(raw_val.read())
            raw_val.close()
            return raw * (3000 / 4096) / 140
        except OSError:
            pass   
    if name == 'AI2':
        try:
            raw_val = os.popen('cat /sys/devices/platform/soc/19251000.gpai/iio:device0/in_voltage3_raw')
            raw = int(raw_val.read())
            raw_val.close()
            return raw * (3000 / 4096) / 140
        except OSError:
            pass 
    if name == 'AI3':
        try:
            raw_val = os.popen('cat /sys/devices/platform/soc/19251000.gpai/iio:device0/in_voltage4_raw')
            raw = int(raw_val.read())
            raw_val.close()
            return raw * (3000 / 4096) * 4
        except OSError:
            pass 
    if name == 'AI4':
        try:
            raw_val = os.popen('cat /sys/devices/platform/soc/19251000.gpai/iio:device0/in_voltage5_raw')
            raw = int(raw_val.read())
            raw_val.close()
            return raw * (3000 / 4096) * 4
        except OSError:
            pass 

if __name__ == '__main__':
    print(ai_get_value(TEST_AI))

    




