import os

def get_vbat_val():
    try:
        raw_val = os.popen('cat /sys/devices/platform/soc/19251000.gpai/iio:device0/in_voltage6_raw')
        raw = int(raw_val.read())
        raw_val.close()
        return raw * (3300 / 4096)
    except OSError:
        pass   
    

if __name__ == '__main__':
    print(get_vbat_val())