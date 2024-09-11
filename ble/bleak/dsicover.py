# import asyncio
# from bleak import BleakScanner
# import os 

# async def scan():
#     os.system('hciconfig hci0 up')
#     devices = await BleakScanner.discover()
#     for d in devices:   #d为类，其属性有：d.name为设备名称，d.address为设备地址
#         print(d)


# if __name__ == "__main__":
#     asyncio.run(scan())




import asyncio
from bleak import BleakScanner
import os 

def detection_callback(device, advertisement_data):
    print(device.address, "RSSI:", device.rssi, advertisement_data)

async def main():
    os.system('hciconfig hci0 up')
    scanner = BleakScanner(detection_callback)
    await scanner.start()
    await asyncio.sleep(10.0)
    await scanner.stop()

    for d in scanner.discovered_devices:
        print(d)

asyncio.run(main())