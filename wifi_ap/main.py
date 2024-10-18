import os, time

os.system('ifconfig wlan0 down')
os.system('hostapd /etc/hostapd.conf -B')
os.system('ifconfig wlan0 192.168.175.1')
os.system('udhcpd -fS /etc/udhcpd.conf &')

#路由转发
os.system('route add default gw  192.168.175.1')
os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
os.system('iptables -t nat -A POSTROUTING -s 192.168.175.0/24 -j MASQUERADE')
time.sleep(1)
os.system('ifconfig eth1 up')
os.system('udhcpc -i eth1')


