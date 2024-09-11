from pymodbus.client import ModbusSerialClient as ModbusClient
client = ModbusClient(method='rtu', port='/dev/tty485_1', baudrate=9600, timeout=1)

if client.connect():
    print("Modbus RTU Client Connected")
else:
    print("Failed to connect to Modbus RTU Client")

#读取保持寄存器
response = client.read_holding_registers(1, 10, slave=1)
if not response.isError():
    print("Register Values: ", response.registers)
else:
    print("Failed to read registers")

#写单个寄存器数据
write_response = client.write_register(address=1, value=25, unit=1)
if not write_response.isError():
    print("Written successfully")
else:
    print("Failed to write register")

#写多个寄存器
values = [20, 40, 60, 80, 100]
write_response = client.write_registers(address=1, values=values, unit=1)
if not write_response.isError():
    print("Multiple registers written successfully")
else:
    print("Failed to write multiple registers")

client.close()
print("Modbus RTU Client Connection Closed")
