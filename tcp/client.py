
from socket import *
# 1.创建套接字
 
tcp_socket = socket(AF_INET,SOCK_STREAM)
 
# 2.准备连接服务器，建立连接
serve_ip = input("请输入服务器ip:")
serve_port = int(input("请输入对应的端口号:"))  # 端口要是int类型，所有要转换
 
tcp_socket.connect((serve_ip, serve_port))  # 连接服务器，建立连接,参数是元组形式
 
# 3.准备需要传送的数据
send_data = input("请输入要发送的数据：")
tcp_socket.send(send_data.encode("gbk"))  #用的是send方法，不是sendto
 
#4.从服务器接收数据
tcp_remsg = tcp_socket.recv(1024) #注意这个1024byte，大小根据需求自己设置
print(tcp_remsg.decode("gbk"))  #如果要乱码可以使用tcp_remsg.decode("gbk")
 
#4.关闭连接
tcp_socket.close()
