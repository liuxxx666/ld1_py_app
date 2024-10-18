import os, time

def redcap_on():
    os.system('ifconfig usb0 up')
    os.system('stty -F /dev/ttyUSB1 -echo')
    os.system('cat /dev/ttyUSB1 &')
    os.system('echo -e \'ATE1\r\n\' > /dev/ttyUSB1')
    os.system('echo -e \'AT^NDISDUP=1,1\r\n\' > /dev/ttyUSB1')
    os.system('udhcpc -i usb0')

def redcap_off():
    os.system('ifconfig usb0 down')
    os.system('kill -9 $(ps | grep "cat /dev/ttyUSB1" | grep -v grep | awk \'{print $1}\')')
    os.system('echo 1 > /sys/class/gpio/gpio11/value')
    time.sleep(0.1)
    os.system('echo 0 > /sys/class/gpio/gpio11/value')
    time.sleep(0.1)

def get_imei():
    os.system('echo -e \'ATI\r\n\' > /dev/ttyUSB1')

def get_csq():
    os.system('echo -e \'AT+CSQ\r\n\' > /dev/ttyUSB1')

def get_iccid():
    os.system('echo -e \'AT^ICCID?\r\n\' > /dev/ttyUSB1')

redcap_on()
get_imei()
get_csq()
get_iccid()
time.sleep(30)
redcap_off()