'''
pyserial官方参考文档：https://pythonhosted.org/pyserial/

'''

import serial
import time

serial485_1 = '/dev/tty485_1'
baudrrate = 115200
write_data= 'hello world!'
read_data = []

if __name__ == '__main__':
    serial485_1 = serial.Serial(port=serial485_1, baudrate=baudrrate, timeout=0.1)
    
    for i in range(1, 5):
        serial485_1.write(write_data.encode(encoding='UTF-8'))
        time.sleep(1)
    
    start = time.time()
    while True:
        end = time.time()
        read_data = serial485_1.read(100)
        if read_data:
            print(read_data)
        if (end - start) > 10:
            break
    
    serial485_1.close()
    
