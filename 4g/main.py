import os, time

def cat1_on():
    os.system('echo -e \'ATE0\r\n\' > /dev/ttyUSB2')
    os.system('cat /dev/ttyUSB2 &')
    os.system('echo -e \'AT+CGDCONT?\r\n\' > /dev/ttyUSB2')
    os.system('echo -e \'AT+COPS?\r\n\' > /dev/ttyUSB2')
    os.system('echo -e \'AT+MDIALUP?\r\n\' > /dev/ttyUSB2')
    os.system('echo -e \'AT+MDIALUP=1,1\r\n\' > /dev/ttyUSB2')
    os.system('udhcpc -i eth0')

def cat1_off():
    os.system('ifconfig eth0 down')
    os.system('kill -9 $(ps | grep "cat /dev/ttyUSB2" | grep -v grep | awk \'{print $1}\')')
    os.system('echo 1 > /sys/class/gpio/gpio11/value')
    time.sleep(0.1)
    os.system('echo 0 > /sys/class/gpio/gpio11/value')
    time.sleep(0.1)

def get_imei():
    os.system('echo -e \'AT+CGSN=1\r\n\' > /dev/ttyUSB2')

def get_csq():
    os.system('echo -e \'AT+CSQ\r\n\' > /dev/ttyUSB2')

def get_iccid():
    os.system('echo -e \'AT+MCCID\r\n\' > /dev/ttyUSB2')

cat1_on()
get_imei()
get_csq()
get_iccid()
time.sleep(30)
cat1_off()