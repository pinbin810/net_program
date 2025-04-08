from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
server = ('127.0.0.1', 5555)

while True:
    msg = input('>> ')
    sock.sendto(msg.encode(), server)

    if msg == 'quit':
        break

    data, _ = sock.recvfrom(1024)
    print(data.decode())

sock.close()