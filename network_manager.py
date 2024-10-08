import subprocess
import logging
import random
import threading
import time

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enable_interface(interface):
    try:
        subprocess.run(['ip', 'link', 'set', interface, 'up'], check=True)
        logging.info(f"启用接口 {interface}。")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"启用接口 {interface} 失败: {e}")
        return False

def check_interface_cable_status(interface):
    if enable_interface(interface):
        try:
            result = subprocess.run(['ethtool', interface], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            if "Link detected: yes" in output:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"检测 {interface} 网线状态时出现错误：{e}")
            return False

def configure_eth1():
    try:
        # 使用 udhcpc 通过 DHCP 获取 IP 地址
        subprocess.run(['udhcpc', '-i', 'eth1'], check=True)
        logging.info("eth1 通过 DHCP 获取 IP 地址成功。")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"eth1 配置失败: {e}")
        return False
def load_kernel_module(module_name):
    try:
        subprocess.run(['modprobe', module_name], check=True)
        logging.info(f"加载内核模块 {module_name} 成功。")
    except subprocess.CalledProcessError as e:
        logging.error(f"加载内核模块 {module_name} 失败: {e}")

def check_kernel_modules():
    # modules = ['iptable_nat', 'nf_nat', 'nf_nat_ftp', 'nf_nat_ipv4', 'iptable_mangle', 'iptable_raw']
    modules = ['iptable_nat', 'nf_nat', 'nf_nat_ftp', 'iptable_mangle', 'iptable_raw']
    missing_modules = []
    for module in modules:
        result = subprocess.run(['lsmod'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        if module not in output:
            missing_modules.append(module)
    return missing_modules
def configure_eth2_as_lan(ip_address='192.168.110.8', subnet_mask='24', gateway='192.168.110.1'):
    try:
        # 检查缺少的内核模块并加载
        missing_modules = check_kernel_modules()
        for module in missing_modules:
            load_kernel_module(module)

        # 启用 eth2 接口
        enable_interface('eth2')

        # 设置 IP 地址和子网掩码
        correct_ip_and_subnet = f"{ip_address}/{subnet_mask}"
        result = subprocess.run(['ip', 'addr', 'show', 'eth2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        if correct_ip_and_subnet in output:
            subprocess.run(['ip', 'addr', 'del', correct_ip_and_subnet, 'dev', 'eth2'], check=True)
        subprocess.run(['ip', 'addr', 'add', correct_ip_and_subnet, 'dev', 'eth2'], check=True)

        # 开启 IP 转发
        with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
            f.write('1')

        # 设置 NAT 规则，将来自 eth2 的流量转发到 eth1
        subprocess.run(['iptables', '-t', 'nat', '-A', 'POSTROUTING', '-o', 'eth1', '-j', 'MASQUERADE'], check=True)

        # 设置 FORWARD 表的 ACCEPT 规则
        subprocess.run(['iptables', '-A', 'FORWARD', '-i', 'eth2', '-o', 'eth1', '-m', 'state', '--state', 'RELATED,ESTABLISHED', '-j', 'ACCEPT'], check=True)
        subprocess.run(['iptables', '-A', 'FORWARD', '-i', 'eth1', '-o', 'eth2', '-j', 'ACCEPT'], check=True)

        # 保存 iptables 规则
        save_iptables_rules()

        logging.info("eth2 配置为 LAN 口成功。")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"eth2 配置为 LAN 口失败: {e}")
        return False

def save_iptables_rules():
    try:
        # 将 iptables 规则保存到文件
        with open('/etc/iptables/rules.v4', 'w') as f:
            subprocess.run(['iptables-save'], stdout=f, check=True)
        logging.info("iptables 规则已保存。")
    except subprocess.CalledProcessError as e:
        logging.error(f"保存 iptables 规则失败: {e}")

def check_interface_connectivity(interface):
    hosts = ['www.baidu.com', 'www.taobao.com', 'www.huawei.com']
    host = random.choice(hosts)
    if interface == 'eth0':
        # 如果是 eth0，先进行特殊连接步骤
        try:
            subprocess.run(f'echo -e "ATE0\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
            subprocess.run(f'cat /dev/ttyUSB2 &', shell=True, check=True)
            subprocess.run(f'echo -e "AT+CGDCONT?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
            subprocess.run(f'echo -e "AT+CGDCONT?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
            subprocess.run(f'echo -e "AT+COPS?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
            subprocess.run(f'echo -e "AT+MDIALUP?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
            subprocess.run(f'echo -e "AT+MDIALUP=1,1\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
            subprocess.run(f'udhcpc -i eth0', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"eth0 连接设置失败: {e}")
            return False
    try:
        return subprocess.run(['ping', '-c', '1', host, '-I', interface], check=True)
    except subprocess.CalledProcessError:
        return False

def use_preferred_interface():
    if check_interface_cable_status('eth1') and configure_eth1() and check_interface_connectivity('eth1'):
        logging.info("使用 eth1 网络。")
        configure_eth2_as_lan()
        return 'eth1'
    elif check_interface_cable_status('eth0') and check_interface_connectivity('eth0'):
        logging.info("使用 eth0 网络。")
        return 'eth0'
    else:
        logging.error("没有可用的网络接口。")
        return None

network_status = False

def auto_check_network():
    global network_status
    while True:
        current_interface = use_preferred_interface()
        if current_interface == 'eth1':
            if check_interface_connectivity('eth1'):
                network_status = True
            else:
                logging.warning("eth1 网络连接异常，尝试切换到 4G。")
                # 这里添加切换到 4G 的代码（与前面 eth0 的连接方式类似）
                try:
                    subprocess.run(f'echo -e "ATE0\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
                    subprocess.run(f'cat /dev/ttyUSB2 &', shell=True, check=True)
                    subprocess.run(f'echo -e "AT+CGDCONT?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
                    subprocess.run(f'echo -e "AT+CGDCONT?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
                    subprocess.run(f'echo -e "AT+COPS?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
                    subprocess.run(f'echo -e "AT+MDIALUP?\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
                    subprocess.run(f'echo -e "AT+MDIALUP=1,1\\r\\n" > /dev/ttyUSB2', shell=True, check=True)
                    subprocess.run(f'udhcpc -i eth0', shell=True, check=True)
                    logging.info("成功切换到 4G 网络。")
                    network_status = True
                except subprocess.CalledProcessError as e:
                    logging.error(f"切换到 4G 网络失败: {e}")
                    network_status = False
        elif current_interface == 'eth0':
            network_status = True
        else:
            network_status = False
        time.sleep(30)  # 每隔 30 秒检查一次网络状态

def start_auto_check():
    threading.Thread(target=auto_check_network, daemon=True).start()

def get_network_status():
    return network_status

start_auto_check()
# auto_check_network