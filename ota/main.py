import time
import requests

for i in range(5):
    print('ota test')
    time.sleep(1)

r = requests.get('http://192.168.3.200/files/test.txt')
print(r.text)
with open(r'/main.py', 'wb') as f:
    f.write(r.text.encode())

print('done')

