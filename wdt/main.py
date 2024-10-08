import ctypes
import fcntl
import sys
import termios
import os
import struct
import time

IOC_NONE = 0
IOC_WRITE = 1
IOC_READ = 2

IOC_NRBITS = 8
IOC_TYPEBITS = 8
IOC_SIZEBITS = 14
IOC_DIRBITS = 2

IOC_NRSHIFT = 0
IOC_TYPESHIFT = IOC_NRSHIFT + IOC_NRBITS
IOC_SIZESHIFT = IOC_TYPESHIFT + IOC_TYPEBITS
IOC_DIRSHIFT = IOC_SIZESHIFT + IOC_SIZEBITS

def IOC(dir_: int, type_: str, nr: int, size: int) -> int:
    return (dir_ << IOC_DIRSHIFT) \
        | (ord(type_) << IOC_TYPESHIFT) \
        | (nr << IOC_NRSHIFT) \
        | (size << IOC_SIZESHIFT)

def IOR(type_: str, nr: int, size: int) -> int:
    return IOC(IOC_READ, type_, nr, size)

def IOWR(type_: str, nr: int, size: int) -> int:
    return IOC(IOC_READ | IOC_WRITE, type_, nr, size)

class watchdog_info(ctypes.Structure):
    _fields_ = [
        ('options', ctypes.c_uint32),           # Options the card/driver supports
        ('firmware_version', ctypes.c_uint32),  # Firmware version of the card
        ('identity', ctypes.c_uint8 * 32),      # Identity of the board
    ]

struct_watchdog_info_size = ctypes.sizeof(watchdog_info)
int_size = ctypes.sizeof(ctypes.c_int)

WATCHDOG_IOCTL_BASE = 'W'
WDIOC_GETSUPPORT = IOR(WATCHDOG_IOCTL_BASE, 0, struct_watchdog_info_size)
WDIOC_GETSTATUS = IOR(WATCHDOG_IOCTL_BASE, 1, int_size)
WDIOC_GETBOOTSTATUS = IOR(WATCHDOG_IOCTL_BASE, 2, int_size)
WDIOC_GETTEMP = IOR(WATCHDOG_IOCTL_BASE, 3, int_size)
WDIOC_SETOPTIONS = IOR(WATCHDOG_IOCTL_BASE, 4, int_size)
WDIOC_KEEPALIVE = IOR(WATCHDOG_IOCTL_BASE, 5, int_size)
WDIOC_SETTIMEOUT = IOWR(WATCHDOG_IOCTL_BASE, 6, int_size)
WDIOC_GETTIMEOUT = IOR(WATCHDOG_IOCTL_BASE, 7, int_size)
WDIOC_SETPRETIMEOUT = IOWR(WATCHDOG_IOCTL_BASE, 8, int_size)
WDIOC_GETPRETIMEOUT = IOR(WATCHDOG_IOCTL_BASE, 9, int_size)
WDIOC_GETTIMELEFT = IOR(WATCHDOG_IOCTL_BASE, 10, int_size)

WDIOS_DISABLECARD = 0x0001	#Turn off the watchdog timer 
WDIOS_ENABLECARD = 0x0002	#Turn on the watchdog timer 
WDIOS_TEMPPANIC	 = 0x0004	#Kernel panic on temperature trip 

#四个看门狗  /dev/watchdog[0...3]
WDT_DEV="/dev/watchdog0"
fd = os.open(WDT_DEV, os.O_RDWR)

ptr = struct.pack('I', WDIOS_DISABLECARD)
fcntl.ioctl(fd, WDIOC_SETOPTIONS, ptr)

ptr = struct.pack('I', 10)
fcntl.ioctl(fd, WDIOC_SETTIMEOUT, ptr)

ptr = struct.pack('I', WDIOS_ENABLECARD)
fcntl.ioctl(fd, WDIOC_SETOPTIONS, ptr)

while True:
    fcntl.ioctl(fd, WDIOC_KEEPALIVE, '')
    time.sleep(8)


