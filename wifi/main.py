import os
import time 

SSID = '"szyyw"'
PWD = '"szyywdz501"'

def connect_wifi():
    with open('/etc/wpa_supplicant.conf', 'r') as f:
        lines = f.readlines()
        lines[3] = '  ssid=%s'%SSID + '\n'
        lines[4] = '  psk=%s'%PWD + '\n'
    with open('/etc/wpa_supplicant.conf', 'w') as f:
        f.writelines(lines)
    
    os.system('wpa_supplicant -D nl80211 -i wlan0 -c /etc/wpa_supplicant.conf -B')
    os.system('udhcpc -i wlan0')
    time.sleep(2)

def disconnect_wifi():
    os.system('ifconfig wlan0 down')
    os.system('killall udhcpc')
    os.system('killall wpa_supplicant')

connect_wifi()

disconnect_wifi()

#扫描热点信息
os.system('ifconfig wlan0 up')
os.system('iwlist wlan0 scan')
time.sleep(5)

#查看wifi通道及对应的频率
os.system('iwlist wlan0 channel')