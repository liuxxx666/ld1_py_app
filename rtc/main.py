
import os
import subprocess

#获取当前系统时间
current_time = subprocess.check_output("date")
print('当前系统时间：%s'%current_time)

#设置系统时间
new_time = "2022-01-01 00:00:00"
subprocess.check_call(["date", "-s", new_time])

#查看rtc时间
return_cmd = subprocess.run('hwclock --show', stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8',shell=True)
if return_cmd.returncode == 0:
    print('命令成功执行') 
    rtc_time = return_cmd.stdout
    print('rtc时间：%s'%rtc_time)

#系统时间同步到rtc
os.system('hwclock -w')

#再次获取rtc时间
return_cmd = subprocess.run('hwclock --show', stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8',shell=True)
if return_cmd.returncode == 0:
    print('命令成功执行') 
    rtc_time = return_cmd.stdout
    print('再次获取rtc时间：%s'%rtc_time)

#-------------------------------------------------
#设置系统时间
new_time = "2024-12-12 00:00:00"
subprocess.check_call(["date", "-s", new_time])

#获取当前系统时间
current_time = subprocess.check_output("date")
print('当前系统时间：%s'%current_time)

#rtc时间写入到系统
os.system('hwclock -s')

#获取当前系统时间
current_time = subprocess.check_output("date")
print('当前系统时间：%s'%current_time)