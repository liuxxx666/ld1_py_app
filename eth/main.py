import os

TEST_ETH = 'eth2'

def eth_up(eth_x, ip):
    try:
        os.system('ifconfig %s up'%eth_x)
        if None == ip:
            os.system('udhcpc -i %s'%eth_x)
        else:
            os.system('ifconfig %s %s'%(eth_x, ip))
    except OSError:
        pass

if __name__ == '__main__':
    eth_up(TEST_ETH, '192.168.1.123')